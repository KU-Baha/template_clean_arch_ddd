import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from prometheus_client import Counter, Gauge, Summary, Histogram, CollectorRegistry

from infrastructure.prometheus.metric import sanitize_metric_name, metrics


class MetricsMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, registry=None):
        super().__init__(app)
        self.registry = registry or CollectorRegistry()
        self._init_metrics()

    def _init_metrics(self):
        for metric_key, metric_info in metrics.items():
            metrics[metric_key]['counter'] = Counter(
                f"{metric_key}_total",
                f"Total count of {metric_key} requests",
                registry=self.registry
            )
            metrics[metric_key]['gauge'] = Gauge(
                f"{metric_key}_in_progress",
                f"In-progress requests for {metric_key}",
                registry=self.registry
            )
            metrics[metric_key]['summary'] = Summary(
                f"{metric_key}_duration_seconds",
                f"Duration summary of {metric_key} requests in seconds",
                registry=self.registry
            )
            metrics[metric_key]['histogram'] = Histogram(
                f"{metric_key}_duration_seconds_histogram",
                f"Duration histogram of {metric_key} requests in seconds",
                registry=self.registry
            )

    async def dispatch(self, request: Request, call_next):
        method = request.method
        endpoint = request.url.path
        metric_key = sanitize_metric_name(f"{method.lower()}_{endpoint}")

        if metric_key in metrics:
            metrics[metric_key]['counter'].inc()  # Increment request count
            metrics[metric_key]['gauge'].inc()  # Increment in-progress request gauge

            start_time = time.time()
            response = await call_next(request)
            elapsed_time = time.time() - start_time

            metrics[metric_key]['summary'].observe(elapsed_time)  # Observe request time for summary
            metrics[metric_key]['histogram'].observe(elapsed_time)  # Observe request time for histogram

            metrics[metric_key]['gauge'].dec()  # Decrement in-progress request gauge
        else:
            response = await call_next(request)

        return response
