import os
from typing import Optional

from beanie import PydanticObjectId
from fastapi import Depends, Request
from fastapi.logger import logger
from fastapi_users import BaseUserManager, FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)
from fastapi_users.db import BeanieUserDatabase, ObjectIDIDMixin

from domain.user import User, get_user_db
from settings import settings


class UserManager(ObjectIDIDMixin, BaseUserManager[User, PydanticObjectId]):
    reset_password_token_secret = settings.FASTAPI_USER_SECRET
    verification_token_secret = settings.FASTAPI_USER_SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        logger.info(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        logger.info(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        logger.info(
            f"Verification requested for user {user.id}. Verification token: {token}"
        )


async def get_user_manager(user_db: BeanieUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


on_gae = os.environ.get("GAE_VERSION", None) is not None
cookie_transport = CookieTransport(
    cookie_max_age=86400,
    cookie_secure=on_gae,
    cookie_name="amtool",
)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.FASTAPI_USER_SECRET, lifetime_seconds=86400)


auth_backend = AuthenticationBackend(
    name="amtool",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, PydanticObjectId](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
