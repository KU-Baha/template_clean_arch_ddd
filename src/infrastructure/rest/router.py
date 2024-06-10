from fastapi import APIRouter

from application.auth.controllers import auth_router
from application.users.controllers import user_router


def add_routes(app):
    api_router = APIRouter(prefix='/api/v1')

    api_router.include_router(auth_router)
    api_router.include_router(user_router)

    app.include_router(api_router)
    return app
