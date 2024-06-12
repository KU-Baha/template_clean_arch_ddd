from fastapi import FastAPI

from infrastructure.prometheus.metric import initialize_metrics


def add_events(app: FastAPI):
    @app.on_event("startup")
    async def startup_event():
        initialize_metrics(app.routes)

    @app.on_event("shutdown")
    async def shutdown_event():
        pass
