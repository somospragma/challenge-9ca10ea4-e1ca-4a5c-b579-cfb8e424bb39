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