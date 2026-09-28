# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener un ZIP con el proyecto completo y arrancable.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Lo que le falta a este proyecto

Esto NO lo tenes que adivinar: salio de comparar el proyecto contra la arquitectura declarada del reto y de un analisis estatico del codigo. Completalo TODO.

### Archivos que la arquitectura del reto declara y no estan

Creálos con implementacion real, en la capa que les corresponde:

- `dags/oltp_etl_pipeline.py`
- `src/extract/transaction_reader.py`
- `src/transform/transaction_processor.py`
- `sql/schema.sql`
- `sql/transactions.sql`
- `tests/test_transaction_processor.py`

### Referencias colgando en el codigo que si esta

Cada una rompe la compilacion:

- `requirements.txt` — `airflow-prometheus-exporter@0.2.0`: airflow-prometheus-exporter declara la version 0.2.0, pero PyPI respondio que esa version no existe. Es una version inventada: reemplazala por una version publicada real, o si no se conoce con certeza, usa el mecanismo centralizado del ecosistema (BOM/parent/platform/version catalog) y no declares una version individual.
- `requirements.txt` — `decouple@1.7`: decouple declara la version 1.7, pero PyPI respondio que esa version no existe. Es una version inventada: reemplazala por una version publicada real, o si no se conoce con certeza, usa el mecanismo centralizado del ecosistema (BOM/parent/platform/version catalog) y no declares una version individual.

## Como saber que terminaste

```bash
pip install -r requirements.txt && pytest -q
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Perfil
Chapter Ciencia de Datos, Especialidad Ingeniero de Datos, Seniority Senior

### Brecha de conocimiento
Implementa bases de datos OLTP. El objetivo es que el candidato domine la implementación y optimización de bases de datos orientadas a transacciones en línea, incluida la configuración, diseño de esquemas, indexación, gestión de transacciones y monitoreo de rendimiento.

### Misión / candidato
Candidato con experiencia como Senior en ingeniería de datos.

### Reto
- Tema: implementacion-bases-de-datos-oltp
- Seniority: senior-l2
- Tipo: practical
- Título: Optimización de Bases de Datos OLTP
- Tiempo estimado: 20 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Configuración Inicial — objetivo: Establecer la configuración básica de la base de datos para soportar transacciones financieras. — entregable (NO resolver): Configuración inicial de la base de datos documentada.
- Fase 2: Diseño del Esquema — objetivo: Diseñar un esquema de base de datos que soporte las transacciones financieras con alta consistencia y disponibilidad. — entregable (NO resolver): Esquema de base de datos diseñado y documentado.
- Fase 3: Gestión de Transacciones — objetivo: Implementar la gestión de transacciones para asegurar la integridad de los datos y la consistencia. — entregable (NO resolver): Gestión de transacciones implementada y documentada.
- Fase 4: Monitoreo de Rendimiento — objetivo: Implementar un sistema de monitoreo para evaluar el rendimiento de la base de datos y identificar áreas de mejora. — entregable (NO resolver): Sistema de monitoreo implementado y documentado.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (ZIP).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: requirements.txt ===
apache-airflow==2.10.0
psycopg2-binary==2.9.9
pandas==2.2.1
pytest==8.1.1
prometheus-client==0.20.0
python-dotenv==1.0.1
SQLAlchemy==2.0.29

# Dependencias adicionales para monitoreo y calidad de datos
apache-airflow-providers-postgres==5.7.0
airflow-prometheus-exporter==0.2.0
python-json-logger==2.0.7
jsonschema==4.21.1

# Para manejo de particiones y formatos columnares
pyarrow==15.0.2
fastparquet==2024.2.0

# Para orquestación y manejo de configuraciones
decouple==1.7

# Dependencias para testing avanzado
pytest-cov==4.1.0
pytest-mock==3.12.0
freezegun==1.4.0

# Versiones coordinadas para evitar conflictos
numpy==1.26.4


// === ARCHIVO: src/load/transaction_writer.py ===
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


// === ARCHIVO: src/monitoring/performance_tracker.py ===
import time
import logging
from datetime import datetime
from typing import Dict, Any, Optional, Callable
from functools import wraps
from collections import deque
import threading

from prometheus_client import Counter, Histogram, Gauge, CollectorRegistry, push_to_gateway

from conf.config_loader import load_config


logger = logging.getLogger(__name__)


class PerformanceTracker:
    """Sistema de monitoreo de rendimiento con métricas Prometheus y Airflow."""

    def __init__(self, job_name: str = 'oltp_etl_pipeline'):
        self.job_name = job_name
        self.config = load_config()
        self.registry = CollectorRegistry()
        
        self._setup_metrics()
        self._setup_in_memory_stats()
        self.push_gateway = self.config.get('monitoring', {}).get('push_gateway', 'localhost:9091')
        self.alert_threshold_latency = self.config.get('monitoring', {}).get('latency_threshold_ms', 50)
        self.alert_threshold_error_rate = self.config.get('monitoring', {}).get('error_rate_threshold', 0.05)

    def _setup_metrics(self) -> None:
        """Configura métricas Prometheus."""
        self.counter_transactions = Counter(
            'oltp_transactions_total',
            'Total de transacciones procesadas',
            ['status', 'phase'],
            registry=self.registry
        )
        self.histogram_latency = Histogram(
            'oltp_transaction_latency_seconds',
            'Latencia de procesamiento de transacciones',
            ['phase'],
            buckets=[0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0],
            registry=self.registry
        )
        self.gauge_active_jobs = Gauge(
            'oltp_active_jobs',
            'Jobs ETL activos',
            registry=self.registry
        )
        self.counter_errors = Counter(
            'oltp_errors_total',
            'Total de errores por tipo',
            ['error_type', 'phase'],
            registry=self.registry
        )

    def _setup_in_memory_stats(self) -> None:
        """Inicializa estadísticas en memoria para cálculos en tiempo real."""
        self.stats_lock = threading.Lock()
        self.throughput_window = deque(maxlen=60)
        self.errors_window = deque(maxlen=60)
        self.latency_window = deque(maxlen=100)
        self.start_time = time.time()

    def record_transaction(self, phase: str, status: str = 'success') -> None:
        """Registra una transacción procesada."""
        self.counter_transactions.labels(phase=phase, status=status).inc()
        with self.stats_lock:
            self.throughput_window.append((time.time(), 1))

    def record_latency(self, phase: str, latency_seconds: float) -> None:
        """Registra latencia de una operación."""
        self.histogram_latency.labels(phase=phase).observe(latency_seconds)
        with self.stats_lock:
            self.latency_window.append(latency_seconds)
        if latency_seconds * 1000 > self.alert_threshold_latency:
            logger.warning(f"Latencia alta en {phase}: {latency_seconds*1000:.2f}ms")

    def record_error(self, error_type: str, phase: str) -> None:
        """Registra un error."""
        self.counter_errors.labels(error_type=error_type, phase=phase).inc()
        with self.stats_lock:
            self.errors_window.append((time.time(), 1))

    def calculate_throughput(self) -> float:
        """Calcula throughput (transacciones por segundo) en ventana móvil."""
        with self.stats_lock:
            if not self.throughput_window:
                return 0.0
            now = time.time()
            window_start = now - 60
            recent = sum(count for ts, count in self.throughput_window if ts >= window_start)
            return recent / 60.0

    def calculate_error_rate(self) -> float:
        """Calcula tasa de errores en ventana móvil."""
        with self.stats_lock:
            if not self.errors_window:
                return 0.0
            now = time.time()
            window_start = now - 60
            recent_errors = sum(count for ts, count in self.errors_window if ts >= window_start)
            recent_total = sum(count for ts, count in self.throughput_window if ts >= window_start)
            return recent_errors / max(recent_total, 1)

    def calculate_avg_latency(self) -> float:
        """Calcula latencia promedio en ventana actual."""
        with self.stats_lock:
            if not self.latency_window:
                return 0.0
            return sum(self.latency_window) / len(self.latency_window)

    def get_current_stats(self) -> Dict[str, Any]:
        """Obtiene estadísticas actuales del tracker."""
        return {
            'throughput_tps': round(self.calculate_throughput(), 2),
            'error_rate': round(self.calculate_error_rate() * 100, 2),
            'avg_latency_ms': round(self.calculate_avg_latency() * 1000, 2),
            'uptime_seconds': int(time.time() - self.start_time),
            'timestamp': datetime.utcnow().isoformat()
        }

    def check_alerts(self) -> Dict[str, Any]:
        """Verifica condiciones de alerta."""
        stats = self.get_current_stats()
        alerts = []
        
        if stats['avg_latency_ms'] > self.alert_threshold_latency:
            alerts.append({
                'type': 'high_latency',
                'message': f"Latencia {stats['avg_latency_ms']}ms exceeds threshold {self.alert_threshold_latency}ms",
                'severity': 'warning'
            })
        
        if stats['error_rate'] > self.alert_threshold_error_rate * 100:
            alerts.append({
                'type': 'high_error_rate',
                'message': f"Error rate {stats['error_rate']}% exceeds threshold {self.alert_threshold_error_rate*100}%",
                'severity': 'critical'
            })
        
        return {'stats': stats, 'alerts': alerts}

    def push_metrics(self) -> None:
        """Envía métricas a Prometheus Push Gateway."""
        try:
            push_to_gateway(
                self.push_gateway,
                job=self.job_name,
                registry=self.registry
            )
            logger.debug("Métricas enviadas a Push Gateway")
        except Exception as e:
            logger.warning(f"Error enviando métricas: {e}")

    def track_time(self, phase: str) -> Callable:
        """Decorador para medir tiempo de ejecución de funciones."""
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs):
                start = time.time()
                try:
                    result = func(*args, **kwargs)
                    self.record_transaction(phase, 'success')
                    return result
                except Exception as e:
                    self.record_transaction(phase, 'error')
                    self.record_error(type(e).__name__, phase)
                    raise
                finally:
                    elapsed = time.time() - start
                    self.record_latency(phase, elapsed)
            return wrapper
        return decorator

    def get_prometheus_metrics(self) -> str:
        """Exporta métricas en formato Prometheus."""
        from prometheus_client import generate_latest
        return generate_latest(self.registry).decode('utf-8')


// === ARCHIVO: conf/config.json ===
{
  "environments": {
    "development": {
      "database": {
        "host": "localhost",
        "port": 5432,
        "database": "oltp_banking_dev",
        "user": "oltp_user",
        "password_env": "DB_PASSWORD",
        "connection_pool": {
          "min_size": 5,
          "max_size": 20,
          "max_overflow": 10,
          "pool_timeout": 30,
          "pool_recycle": 3600,
          "echo": false
        },
        "isolation_level": "REPEATABLE READ",
        "statement_timeout": 45000,
        "lock_timeout": 30000,
        "idle_in_transaction_session_timeout": 60000
      },
      "processing": {
        "batch_size": 5000,
        "parallel_workers": 4,
        "chunk_size": 1000,
        "retry_attempts": 3,
        "retry_delay_seconds": 5,
        "enable_checkpointing": true,
        "checkpoint_interval": 10000
      },
      "partitioning": {
        "strategy": "by_date",
        "date_format": "%Y_%m",
        "retention_days": 90,
        "compression": "snappy"
      },
      "quality_thresholds": {
        "min_amount": 0.01,
        "max_amount": 1000000.00,
        "max_null_percentage": 0.05,
        "duplicate_check_enabled": true,
        "schema_validation_strict": true
      },
      "monitoring": {
        "prometheus_enabled": true,
        "prometheus_port": 9090,
        "metrics_interval_seconds": 30,
        "slow_query_threshold_ms": 100,
        "alert_on_quality_failure": true,
        "log_level": "DEBUG"
      },
      "s3": {
        "bucket": "oltp-banking-dev",
        "region": "us-east-1",
        "prefix": "dev/transactions/",
        "format": "parquet"
      }
    },
    "production": {
      "database": {
        "host": "oltp-prod.cluster-abc123.us-east-1.rds.amazonaws.com",
        "port": 5432,
        "database": "oltp_banking_prod",
        "user": "oltp_service_account",
        "password_env": "DB_PASSWORD_PROD",
        "connection_pool": {
          "min_size": 20,
          "max_size": 100,
          "max_overflow": 50,
          "pool_timeout": 30,
          "pool_recycle": 1800,
          "echo": false
        },
        "isolation_level": "REPEATABLE READ",
        "statement_timeout": 45000,
        "lock_timeout": 30000,
        "idle_in_transaction_session_timeout": 60000
      },
      "processing": {
        "batch_size": 10000,
        "parallel_workers": 8,
        "chunk_size": 2000,
        "retry_attempts": 5,
        "retry_delay_seconds": 10,
        "enable_checkpointing": true,
        "checkpoint_interval": 25000
      },
      "partitioning": {
        "strategy": "by_date",
        "date_format": "%Y_%m",
        "retention_days": 365,
        "compression": "gzip"
      },
      "quality_thresholds": {
        "min_amount": 0.01,
        "max_amount": 1000000.00,
        "max_null_percentage": 0.01,
        "duplicate_check_enabled": true,
        "schema_validation_strict": true
      },
      "monitoring": {
        "prometheus_enabled": true,
        "prometheus_port": 9090,
        "metrics_interval_seconds": 15,
        "slow_query_threshold_ms": 50,
        "alert_on_quality_failure": true,
        "log_level": "INFO"
      },
      "s3": {
        "bucket": "oltp-banking-prod",
        "region": "us-east-1",
        "prefix": "prod/transactions/",
        "format": "parquet"
      }
    }
  },
  "performance_targets": {
    "throughput_tps": 5000,
    "max_latency_ms": 50,
    "p99_latency_ms": 100,
    "max_concurrent_connections": 150,
    "replication_lag_ms": 50,
    "checkpoint_interval_transactions": 50000
  },
  "quality_rules": {
    "transaction_amount": {
      "type": "range",
      "min": 0.01,
      "max": 1000000.00,
      "reject_on_violation": true
    },
    "transaction_timestamp": {
      "type": "not_null",
      "reject_on_violation": true
    },
    "account_reference": {
      "type": "foreign_key",
      "reference_table": "accounts",
      "reference_column": "account_id",
      "reject_on_violation": true
    },
    "transaction_type": {
      "type": "enum",
      "allowed_values": ["DEPOSIT", "WITHDRAWAL", "TRANSFER", "PAYMENT", "REFUND"],
      "reject_on_violation": true
    },
    "duplicate_detection": {
      "type": "unique_constraint",
      "columns": ["transaction_id"],
      "reject_on_violation": true,
      "strategy": "upsert"
    }
  },
  "airflow": {
    "default_args": {
      "owner": "dataengineering",
      "depends_on_past": false,
      "email_on_failure": true,
      "email_on_retry": false,
      "retries": 3,
      "retry_delay": {
        "minutes": 5
      }
    },
    "schedule_interval": "*/15 * * * *",
    "max_active_runs": 1,
    "catchup": false,
    "execution_timeout": {
      "hours": 2
    }
  },
  "logging": {
    "format": "json",
    "date_format": "%Y-%m-%d %H:%M:%S",
    "log_fields": ["timestamp", "level", "message", "transaction_id", "duration_ms"],
    "output": {
      "console": {
        "enabled": true,
        "level": "DEBUG"
      },
      "file": {
        "enabled": true,
        "path": "/var/log/oltp/pipeline.log",
        "max_bytes": 104857600,
        "backup_count": 10,
        "level": "INFO"
      }
    }
  }
}
// === ARCHIVO: README.md ===
# Pipeline ETL de Transacciones OLTP - Banca Digital

Este proyecto implementa un pipeline de extracción, transformación y carga (ETL) para el procesamiento de transacciones financieras en un entorno OLTP de banca digital. El sistema está diseñado para manejar un throughput de 5,000 transacciones por segundo con una latencia máxima de 50ms.

## Requisitos del Sistema

- Python 3.13+
- PostgreSQL 16
- Apache Airflow 2.10.0
- AWS S3 (para almacenamiento de datos columnares)

## Estructura del Proyecto

```
oltp-etl-pipeline/
├── conf/
│   └── config.json              # Configuración por ambiente
├── dags/
│   └── oltp_etl_pipeline.py     # Orquestación principal de Airflow
├── src/
│   ├── extract/
│   │   └── transaction_reader.py    # Lectura de transacciones fuente
│   ├── transform/
│   │   └── transaction_processor.py # Transformaciones y validación
│   ├── load/
│   │   └── transaction_writer.py    # Escritura a PostgreSQL y S3
│   └── monitoring/
│       └── performance_tracker.py   # Métricas y monitoreo
├── sql/
│   ├── schema.sql               # Definición de tablas
│   └── transactions.sql         # Datos de prueba
├── tests/
│   └── test_transaction_processor.py
├── requirements.txt
└── README.md
```

## Instalación

1. Clonar el repositorio y navegar al directorio:

```bash
cd oltp-etl-pipeline
```

2. Crear un entorno virtual (recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

4. Configurar las variables de entorno:

Crear un archivo `.env` en la raíz del proyecto:

```bash
# Desarrollo
DB_PASSWORD=your_dev_password
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key

# Producción (usar Secrets Manager en entornos reales)
DB_PASSWORD_PROD=your_prod_password
```

5. Configurar la base de datos:

Ejecutar los scripts SQL para crear el esquema:

```bash
psql -h localhost -U oltp_user -d oltp_banking_dev -f sql/schema.sql
psql -h localhost -U oltp_user -d oltp_banking_dev -f sql/transactions.sql
```

6. Inicializar Airflow:

```bash
airflow db init
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com

# Iniciar el scheduler y webserver
airflow scheduler &
airflow webserver --port 8080 &
```

## Ejecución del Pipeline

### Desarrollo

Establecer el ambiente:

```bash
export ENV=development
```

Ejecutar el DAG manualmente:

```bash
airflow dags trigger oltp_etl_pipeline
```

O ejecutar las etapas directamente con Python:

```bash
# Extracción
python -c "from src.extract.transaction_reader import TransactionReader; r = TransactionReader(); print(r.read_batch(limit=1000))"

# Transformación
python -c "from src.transform.transaction_processor import TransactionProcessor; p = TransactionProcessor(); print(p.process_batch([]))"

# Carga
python -c "from src.load.transaction_writer import TransactionWriter; w = TransactionWriter(); print(w.write_batch([]))"
```

### Producción

```bash
export ENV=production
airflow dags trigger oltp_etl_pipeline
```

## Métricas de Referencia - Entorno OLTP

### Objetivos de Rendimiento

| Métrica | Objetivo | Umbral de Alerta |
|---------|----------|------------------|
| Throughput | 5,000 TPS | < 4,500 TPS |
| Latencia P50 | 25 ms | > 35 ms |
| Latencia P99 | 100 ms | > 150 ms |
| Conexiones concurrentes | 100 | > 130 |
| Lag de replicación | 50 ms | > 100 ms |

### Métricas de Calidad de Datos

| Regla | Umbral | Acción |
|-------|--------|--------|
| Monto mínimo | 0.01 | Rechazar |
| Monto máximo | 1,000,000.00 | Rechazar |
| Porcentaje nulos | < 1% | Alerta |
| Duplicados | 0% | Upsert |
| Validación de esquema | Estricta | Rechazar |

### Monitoreo

El pipeline exporta métricas a Prometheus en el puerto 9090. Métricas clave:

- `oltp_transactions_processed_total` - Total de transacciones procesadas
- `oltp_transactions_failed_total` - Total de transacciones fallidas
- `oltp_processing_duration_seconds` - Duración del procesamiento
- `oltp_batch_size` - Tamaño del lote procesado
- `oltp_quality_violations` - Violaciones de reglas de calidad

Verificar métricas:

```bash
curl http://localhost:9090/metrics | grep oltp
```

## Configuración por Ambiente

La configuración se gestiona en `conf/config.json` con soporte para:

- **development**: Configuración local con pools pequeños y logging detallado
- **production**: Configuración optimizada con alta concurrencia y compresión

Parámetros clave configurables:

- `connection_pool.min_size/max_size`: Control de conexiones
- `batch_size`: Tamaño de lotes de procesamiento
- `isolation_level`: REPEATABLE READ para consistencia
- `partitioning`: Particionado por fecha en formato Parquet

## Particionado y Formato Columnar

El sistema utiliza particionado mensual para las tablas de transacciones:

- Formato: Parquet con compresión Snappy (dev) / Gzip (prod)
- Convenciones de nomenclatura: `transactions_2024_01`
- Retención: 90 días (dev) / 365 días (prod)

## Patrones de Diseño Implementados

1. **Idempotencia**: Upserts con `ON CONFLICT` en PostgreSQL
2. **Checkpointing**: Guardado de progreso cada 10,000-25,000 transacciones
3. **Reintentos**: Estrategia exponencial con backoff configurable
4. **Calidad**: Validación en múltiples capas (schema, rango, unicidad)
5. **Monitoreo**: Métricas en tiempo real con alertas configurables

## Pruebas

Ejecutar las pruebas unitarias:

```bash
pytest -q
```

Con cobertura:

```bash
pytest --cov=src --cov-report=html
```

## Mantenimiento

### Limpieza de Particiones Antiguas

```bash
# En PostgreSQL
DELETE FROM transactions WHERE transaction_date < NOW() - INTERVAL '90 days';
```

### Reconstrucción de Índices

```bash
# PostgreSQL
REINDEX TABLE transactions;
ANALYZE transactions;
```

## Troubleshooting

### Problemas de Conexión

Verificar configuración en `conf/config.json` y variables de entorno:

```bash
python -c "from decouple import config; print(config('DB_PASSWORD'))"
```

### Alto Uso de Memoria

Reducir `batch_size` en la configuración del ambiente.

### Latencia Elevada

1. Verificar índices en `sql/schema.sql`
2. Ajustar `connection_pool.max_size`
3. Revisar métricas en Prometheus
4. Verificar logs en `/var/log/oltp/pipeline.log`

## Licencia

Propiedad de la organización - Uso interno únicamente.

```
