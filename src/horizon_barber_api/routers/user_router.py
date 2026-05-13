from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.future import select

from horizon_barber_api.database import get_session
from horizon_barber_api.schemas import UserPostSchema, UserGetSchema
from horizon_barber_api.models import User

user_router = APIRouter()

@user_router.post("", response_model=UserPostSchema, status_code=201)
def create(request: UserPostSchema, session: Session = Depends(get_session)):
    query = select(User).filter(User.username == request.username)
    user = session.execute(query).scalar_one_or_none()

    if user:
        raise HTTPException(status_code=409, detail="User already exists")

    new_user = User(
        username=request.username,
        number=request.number,
        url_photo=request.url_photo,
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user

@user_router.get("", response_model=UserGetSchema, status_code=200)
def get_user_by_username(username: str, session: Session = Depends(get_session)):
    query = session.query(User).filter(User.username == username)
    user = session.execute(query).scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user