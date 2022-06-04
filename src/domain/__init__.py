import traceback

from awesome_exception.exceptions import HTTPException
from fastapi.logger import logger
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from fastapi.responses import JSONResponse


class Router:
    @staticmethod
    def set_exception_handler(app):
        @app.exception_handler(HTTPException)
        async def http_exception_handler(request: Request, exc: HTTPException):
            logger.error(traceback.format_exc())
            return JSONResponse(
                status_code=exc.status_code,
                content={"detail": exc.detail, "error_code": exc.error_code},
            )

    @staticmethod
    def include_cors_middleware(app):
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[
                # "http://localhost",
                # "http://localhost:8000",
            ],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    @staticmethod
    def web_router(app):
        from domain.service import route as service_route
        from domain.user import route as user_route

        for route in [service_route, user_route]:
            app.include_router(route.router)
