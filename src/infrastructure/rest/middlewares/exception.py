import logging
import traceback
from gettext import gettext

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.base import RequestResponseEndpoint
from starlette.responses import Response
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError


class ExceptionHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        try:
            response = await call_next(request)
            return response
        except StarletteHTTPException as exc:
            return JSONResponse(
                status_code=exc.status_code,
                content={"detail": exc.detail},
            )
        except RequestValidationError as exc:
            return JSONResponse(
                status_code=422,
                content={"detail": exc.errors()},
            )

        except Exception as exc:
            error_message = traceback.format_exc()
            logging.error(f"An error occurred:\n{error_message}")
            return JSONResponse(
                status_code=500,
                content={"detail": gettext("An internal server error occurred.")},
            )
