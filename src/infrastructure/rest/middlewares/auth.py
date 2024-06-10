import base64
from gettext import gettext

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.base import RequestResponseEndpoint
from starlette.responses import Response

from application.config import settings
from domain.base.exception import BusinessException
from domain.utils.auth import send_access_req


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        raise Exception("Not implemented")
        if request.url.path.startswith("/api/v1/"):
            auth_header = request.headers.get("Authorization")
            service = request.url.path.split("/")[3]

            if not auth_header:
                raise BusinessException(401, "Invalid token")

            scheme, credentials = auth_header.split()

            if scheme.lower() != 'basic':
                raise BusinessException(401, "Invalid token")

            decoded = base64.b64decode(credentials).decode("utf-8")
            username, password = decoded.split(":")

            has_permission = send_access_req(
                settings.AUTH_SERVICE_URL,
                settings.PROJECT_NAME,
                service,
                username,
                password
            )

            if not has_permission:
                raise BusinessException(
                    403,
                    gettext("You don't have permission to access this service")
                )

        return await call_next(request)
