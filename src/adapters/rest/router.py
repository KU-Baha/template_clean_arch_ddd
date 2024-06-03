from application.apps.auth.controllers import auth_router
from application.apps.users.controllers import user_router


def add_routes(app):
    app.include_router(auth_router)
    app.include_router(user_router)
    return app
