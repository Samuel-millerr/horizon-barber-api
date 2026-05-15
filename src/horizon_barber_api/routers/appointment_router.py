from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from sqlalchemy.future import select

from horizon_barber_api.database import get_session
from horizon_barber_api.routers.user_router import get_user_by_username
from horizon_barber_api.routers.barber_service_router import get_by_id
from horizon_barber_api.schemas import AppointmentGetSchema, AppointmentPostSchema
from horizon_barber_api.models import Appointment, User, BarberService

appointment_router = APIRouter()


@appointment_router.post("", response_model=AppointmentGetSchema, status_code=201)
def create(request: AppointmentPostSchema, session: Session = Depends(get_session)):
    user = get_user_by_username(request.username, session)

    new_appointment = Appointment(
        service_id=request.service_id,
        user_id=user.id,
        observation=request.observation,
    )

    session.add(new_appointment)
    session.commit()
    session.refresh(new_appointment)

    service: BarberService = get_by_id(new_appointment.service_id, session)

    appointment_response = AppointmentGetSchema(
        id=new_appointment.id,
        service_name=service.name,
        service_icon=service.icon,
        barber_name=new_appointment.barber_name,
        observation=new_appointment.observation
    )

    return appointment_response


@appointment_router.get("", response_model=List[AppointmentGetSchema], status_code=200)
def get_all(username: str, session: Session = Depends(get_session)):
    user: User = get_user_by_username(username, session)

    query = select(Appointment).filter(Appointment.user_id == user.id)
    appointments = session.execute(query).scalars().all()

    appointment_response = []

    for appointment in appointments:
        service: BarberService = get_by_id(appointment.service_id, session)

        appointment_response.append(
            AppointmentGetSchema(
                id=appointment.id,
                service_name=service.name,
                service_icon=service.icon,
                barber_name=appointment.barber_name,
                observation=appointment.observation
            )
        )

    return appointment_response

@appointment_router.delete("/{id}", status_code=204)
def delete(id: int, session: Session = Depends(get_session)):
    query = select(Appointment).filter(Appointment.id == id)
    appointment = session.execute(query).scalars().one_or_none()

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")


    session.delete(appointment)
    session.commit()

    return