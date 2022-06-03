from datetime import datetime
from pydantic import BaseModel


class Service(BaseModel):
    date: datetime.date
