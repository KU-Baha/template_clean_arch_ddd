from fastapi import FastAPI

from adapters.di.container import Container
from adapters.rest.router import add_routes


def create_app():
    container = Container()

    app = FastAPI()

    app.container = container
    add_routes(app)

    return app
