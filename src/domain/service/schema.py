from datetime import date
from pydantic import BaseModel


class Service(BaseModel):
    date: date
