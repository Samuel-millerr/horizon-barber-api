from datetime import datetime
from typing import Optional

from pydantic import BaseModel as SCBaseModel
from sqlalchemy import null


class UserGetSchema(SCBaseModel):
    id: int
    username: str
    number: str
    url_photo: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


class UserRegisterSchema(SCBaseModel):
    username: str
    password: str
    number: str
    url_photo: Optional[str] = None

    class Config:
        from_attributes = True


class UserLoginrSchema(SCBaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True
