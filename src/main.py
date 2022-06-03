import logging

from fastapi import FastAPI
from fastapi.logger import logger

from domain import Router, api_meta
from settings import get_settings


async def shutdown_event():
    logger.warn("shutting down service")


FORMAT = "%(levelname)-9s %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
app = FastAPI(
    title="Jethro",
    responses=api_meta.RESTFUL_ERROR_RESPONSES,
    on_shutdown=[shutdown_event],
)
web_app = FastAPI(
    title="Jethro API",
    openapi_tags=api_meta.WEB_DOMAIN_TAGS_METADATA,
    redoc_url=None,
)

Router.include_cors_middleware(web_app)

Router.set_exception_handler(web_app)

Router.web_router(web_app)

app.mount("/api", web_app)
