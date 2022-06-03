from fastapi_users.db import BeanieUserDatabase

from domain.user.schema import User


async def get_user_db():
    yield BeanieUserDatabase(User)
