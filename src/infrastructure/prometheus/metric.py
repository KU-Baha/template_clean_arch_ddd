import re
from typing import Iterable

from prometheus_client import Summary, Counter, Gauge, Histogram

metrics = {}


def sanitize_metric_name(name):
    return re.sub(r'[^a-zA-Z0-9_]', '_', name).replace('__', '_')


def initialize_metrics(routes: Iterable):
    for route in routes:
        for method in route.methods:
            endpoint = f"{method.lower()}_{route.path}"
            sanitized_endpoint = sanitize_metric_name(endpoint)
            if sanitized_endpoint not in metrics:
                metrics[sanitized_endpoint] = {
                    'summary': Summary(f'{sanitized_endpoint}_summary', f'Time spent processing {endpoint}'),
                    'counter': Counter(f'{sanitized_endpoint}_counter', f'Total requests for {endpoint}'),
                    'gauge': Gauge(f'{sanitized_endpoint}_gauge', f'Current in-progress requests for {endpoint}'),
                    'histogram': Histogram(f'{sanitized_endpoint}_histogram', f'Request duration for {endpoint}')
                }
