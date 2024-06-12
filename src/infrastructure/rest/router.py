from fastapi import APIRouter

from application.prometheus.controller import prometheus_router
from application.users.controllers import user_router


def add_routes(app):
    api_router = APIRouter(prefix='/api/v1')

    api_router.include_router(user_router)

    app.include_router(api_router)
    app.include_router(prometheus_router)
    return app
