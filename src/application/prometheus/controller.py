from fastapi import APIRouter
from starlette.responses import Response
from prometheus_client import generate_latest, REGISTRY, CollectorRegistry

from infrastructure.prometheus.metric import metrics

prometheus_router = APIRouter(prefix='/metrics', tags=['metrics'])


@prometheus_router.get("/")
def metrics_endpoint():
    registry = CollectorRegistry()

    for metric_group in metrics.values():
        for metric in metric_group.values():
            registry.register(metric)

    return Response(generate_latest(registry), media_type="text/plain")
