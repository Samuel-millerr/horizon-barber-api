from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from horizon_barber_api.settings import settings


class User(settings.DBBaseModel):
    __tablename__ = "user"

    id: int = Column(Integer, primary_key=True)
    username: str = Column(String, unique=True)
    hashed_password: str = Column(String)
    number: str = Column(String)
    url_photo: str = Column(String)
    created_at: datetime = Column(DateTime, server_default=func.now())

    appointment = relationship(
        "Appointment", back_populates="user", cascade="all, delete-orphan"
    )


class Appointment(settings.DBBaseModel):
    __tablename__ = "appointment"

    id: int = Column(Integer, primary_key=True)
    service_id: int = Column(Integer, ForeignKey("service.id"))
    user_id: int = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="appointment")
    service = relationship("Service", back_populates="appointment")


class Service(settings.DBBaseModel):
    __tablename__ = "service"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, unique=True)
    description: str = Column(String)
    price: float = Column(Float)
    duration_minutes: int = Column(Integer)
    icon: str = Column(String)

    appointment = relationship("Appointment", back_populates="service")
