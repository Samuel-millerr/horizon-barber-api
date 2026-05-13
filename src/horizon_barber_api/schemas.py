from datetime import datetime

from pydantic import BaseModel as SCBaseModel
from typing import Optional

class UserGetSchema(SCBaseModel):
    id: int
    username: str
    number: str
    url_photo:str
    created_at: datetime

    class Config:
        from_attributes = True

class UserPostSchema(SCBaseModel):
    username: Optional[str] = None
    number: Optional[str] = None
    url_photo: Optional[str] = None

    class Config:
        from_attributes = True
