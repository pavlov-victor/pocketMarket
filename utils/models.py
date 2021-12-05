from datetime import datetime

from pydantic import BaseModel


class TokenOutput(BaseModel):
    access: str
    refresh: str
    expired: datetime


class SuccessModel(BaseModel):
    status: bool
