from fastapi import FastAPI

from domain.base.logger import config_logging
from infrastructure.di.container import Container
from infrastructure.rest.events import add_events
from infrastructure.rest.middleware import add_middlewares
from infrastructure.rest.router import add_routes


def create_app():
    container = Container()
    config_logging()

    app = FastAPI()

    app.container = container
    add_middlewares(app)
    add_routes(app)
    add_events(app)

    return app
