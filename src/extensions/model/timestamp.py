from datetime import datetime
from typing import TypeVar

from beanie import Insert, Replace, SaveChanges, before_event

DocType = TypeVar("DocType", bound="Document")


class TimestampMixin:
    @before_event([Insert, Replace, SaveChanges])
    async def set_timestamp(self: DocType):
        if self.created_at is None:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
