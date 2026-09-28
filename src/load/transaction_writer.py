import logging
import os
from datetime import datetime
from typing import List, Dict, Any, Optional
from decimal import Decimal
import hashlib
import json

import pandas as pd
from sqlalchemy import create_engine, text, inspect
from sqlalchemy.engine import Engine
from sqlalchemy.pool import QueuePool

from conf.config_loader import load_config


logger = logging.getLogger(__name__)


class TransactionWriter:
    """Escritor de transacciones procesadas en PostgreSQL con idempotencia y particionado."""

    def __init__(self, connection_string: str, partition_date: str):
        self.engine = create_engine(
            connection_string,
            poolclass=QueuePool,
            pool_size=10,
            max_overflow=20,
            pool_pre_ping=True,
            isolation_level='REPEATABLE READ'
        )
        self.partition_date = partition_date
        self.config = load_config()
        self.min_amount = self.config.get('quality_rules', {}).get('min_amount', 0.01)
        self.max_amount = self.config.get('quality_rules', {}).get('max_amount', 1000000.00)
        self._ensure_partition(partition_date)

    def _ensure_partition(self, partition_date: str) -> None:
        """Crea la partición mensual si no existe."""
        year, month = partition_date.split('-')[:2]
        table_name = f'transactions_{year}_{month}'
        
        with self.engine.connect() as conn:
            conn.execute(text(f"""
                DO $$
                BEGIN
                    IF NOT EXISTS (
                        SELECT 1 FROM pg_tables 
                        WHERE tablename = '{table_name}'
                    ) THEN
                        CREATE TABLE {table_name} (
                            LIKE transactions INCLUDING DEFAULTS INCLUDING CONSTRAINTS
                        );
                        ALTER TABLE {table_name} ADD CONSTRAINT 
                            chk_{table_name}_date CHECK (transaction_date >= '{partition_date}-01' AND transaction_date < '{partition_date}-01'::date + INTERVAL '1 month');
                    END IF;
                END $$;
            """))
            conn.commit()
        logger.info(f"Partición {table_name} verificada/creada")

    def _generate_transaction_id(self, record: Dict[str, Any]) -> str:
        """Genera ID único idempotente basado en atributos de la transacción."""
        key_fields = f"{record.get('source_account')}{record.get('target_account')}{record.get('amount')}{record.get('timestamp')}"
        return hashlib.sha256(key_fields.encode()).hexdigest()[:16]

    def _validate_record(self, record: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Valida que el registro cumpla las reglas de calidad."""
        try:
            amount = Decimal(str(record.get('amount', 0)))
            if amount < Decimal(str(self.min_amount)):
                logger.warning(f"Monto {amount} menor al mínimo {self.min_amount}")
                return None
            if amount > Decimal(str(self.max_amount)):
                logger.warning(f"Monto {amount} mayor al máximo {self.max_amount}")
                return None
            if not record.get('source_account') or not record.get('target_account'):
                logger.warning("Cuentas origen/destino requeridas")
                return None
            record['transaction_id'] = self._generate_transaction_id(record)
            return record
        except Exception as e:
            logger.error(f"Error validando registro: {e}")
            return None

    def _prepare_upsert_sql(self, table_name: str) -> str:
        """Genera SQL de upsert con ON CONFLICT para idempotencia."""
        return f"""
        INSERT INTO {table_name} (
            transaction_id, source_account, target_account, amount,
            transaction_type, transaction_date, status, metadata
        ) VALUES (
            :transaction_id, :source_account, :target_account, :amount,
            :transaction_type, :transaction_date, :status, :metadata
        )
        ON CONFLICT (transaction_id) DO UPDATE SET
            status = EXCLUDED.status,
            metadata = EXCLUDED.metadata,
            updated_at = CURRENT_TIMESTAMP
        WHERE transactions.status != EXCLUDED.status
        """

    def write_batch(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Escribe lote de transacciones con validación, upsert y estadísticas."""
        if not records:
            return {'inserted': 0, 'updated': 0, 'rejected': 0}

        validated_records = []
        for record in records:
            validated = self._validate_record(record)
            if validated:
                validated_records.append(validated)

        rejected = len(records) - len(validated_records)
        if not validated_records:
            return {'inserted': 0, 'updated': 0, 'rejected': rejected}

        year, month = self.partition_date.split('-')[:2]
        table_name = f'transactions_{year}_{month}'

        df = pd.DataFrame(validated_records)
        df['transaction_date'] = pd.to_datetime(df.get('transaction_date', self.partition_date))
        df['metadata'] = df.get('metadata', '{}').apply(lambda x: json.dumps(x) if isinstance(x, dict) else x)
        df['amount'] = df['amount'].astype(float)

        inserted = 0
        updated = 0

        with self.engine.begin() as conn:
            for _, row in df.iterrows():
                result = conn.execute(
                    text(self._prepare_upsert_sql(table_name)),
                    {
                        'transaction_id': row['transaction_id'],
                        'source_account': row['source_account'],
                        'target_account': row['target_account'],
                        'amount': row['amount'],
                        'transaction_type': row.get('transaction_type', 'TRANSFER'),
                        'transaction_date': row['transaction_date'],
                        'status': row.get('status', 'COMPLETED'),
                        'metadata': row.get('metadata', '{}')
                    }
                )
                if result.row_count > 0:
                    if result.row_count == 1:
                        inserted += 1
                    else:
                        updated += 1

        logger.info(f"Escritura completada: {inserted} insertados, {updated} actualizados, {rejected} rechazados")
        return {'inserted': inserted, 'updated': updated, 'rejected': rejected}

    def write_to_parquet(self, records: List[Dict[str, Any]], output_path: str) -> str:
        """Exporta transacciones a formato columnar Parquet para analítica."""
        if not records:
            return ''

        validated = [r for r in records if self._validate_record(r)]
        if not validated:
            return ''

        df = pd.DataFrame(validated)
        df['transaction_date'] = pd.to_datetime(df.get('transaction_date', self.partition_date))
        df['amount'] = df['amount'].astype(float)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_parquet(output_path, engine='fastparquet', compression='snappy')
        logger.info(f"Parquet escrito en {output_path}: {len(df)} registros")
        return output_path

    def close(self) -> None:
        """Cierra el pool de conexiones."""
        self.engine.dispose()