from fastapi import FastAPI

from infrastructure.di.container import Container
from infrastructure.rest.router import add_routes


def create_app():
    container = Container()

    app = FastAPI()

    app.container = container
    add_routes(app)

    return app
