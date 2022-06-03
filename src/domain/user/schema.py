from typing import List

from beanie import Indexed, PydanticObjectId
from fastapi_users import schemas
from fastapi_users_db_beanie import BeanieBaseUser
from pymongo import IndexModel
from pymongo.collation import Collation

from domain.iam.schema import IAMRole


class User(BeanieBaseUser[PydanticObjectId]):
    name: Indexed(str, unique=True)
    # TODO: remove this default role before production
    roles: List[IAMRole] = [IAMRole.ADMIN]

    def has_role(self, role: IAMRole):
        roles_strings = [r.value for r in self.roles]
        return role.value in roles_strings

    def summary(self) -> "UserRead":
        return UserRead.parse_obj(self.dict())

    class Settings:
        name = "user"
        email_collation = Collation("en", strength=2)
        indexes = [
            IndexModel("email", unique=True),
            IndexModel(
                "email", name="case_insensitive_email_index", collation=email_collation
            ),
        ]


class UserRead(schemas.BaseUser[PydanticObjectId]):
    name: str
    roles: List[IAMRole]


class UserCreate(schemas.BaseUserCreate):
    name: str
    roles: List[IAMRole] = [IAMRole.ADMIN]


class UserUpdate(schemas.BaseUserUpdate):
    name: str
    roles: List[IAMRole] = [IAMRole.ADMIN]
