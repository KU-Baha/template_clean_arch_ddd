from prometheus_client import CollectorRegistry
from starlette.middleware.cors import CORSMiddleware

from application.config import cors_config
from infrastructure.rest.middlewares.auth import AuthMiddleware
from infrastructure.rest.middlewares.exception import ExceptionHandlingMiddleware
from infrastructure.rest.middlewares.prometheus import MetricsMiddleware


def add_middlewares(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_config.ALLOW_ORIGINS,
        allow_credentials=cors_config.ALLOW_CREDENTIALS,
        allow_methods=cors_config.ALLOW_METHODS,
        allow_headers=cors_config.ALLOW_HEADERS,
    )
    app.add_middleware(AuthMiddleware)
    app.add_middleware(MetricsMiddleware)
    app.add_middleware(ExceptionHandlingMiddleware)
    return app
