from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from sqlalchemy.future import select

from horizon_barber_api.database import get_session
from horizon_barber_api.schemas import BarberServiceGetSchema
from horizon_barber_api.models import BarberService

barber_servicer_router = APIRouter()

@barber_servicer_router.get("", response_model=List[BarberServiceGetSchema], status_code=200)
def get_all(session: Session = Depends(get_session)):
    query = select(BarberService)
    barber_services = session.execute(query).scalars()

    return barber_services