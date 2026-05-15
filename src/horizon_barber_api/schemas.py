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


class UserLoginSchema(SCBaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True


class UserUpdateSchema(SCBaseModel):
    number: Optional[str] = None
    photoUrl: Optional[str] = None

    class Config:
        from_attributes = True


class BarberServiceGetSchema(SCBaseModel):
    id: int
    name: str
    description: str
    price: float
    duration_minutes: int
    icon: str

    class Config:
        from_attributes = True


class AppointmentGetSchema(SCBaseModel):
    id: int
    service_name: str
    service_icon: str
    barber_name: str
    observation: str

    class Config:
        from_attributes = True


class AppointmentPostSchema(SCBaseModel):
    username: str
    service_id: int
    observation: str

    class Config:
        from_attributes = True
