from fastapi import APIRouter, Depends, HTTPException
from pwdlib import PasswordHash
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from horizon_barber_api.database import get_session
from horizon_barber_api.models import User
from horizon_barber_api.schemas import UserRegisterSchema, UserGetSchema, UserLoginSchema

user_router = APIRouter()
pwd_context = PasswordHash.recommended()


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


@user_router.post("/register", response_model=UserGetSchema, status_code=201)
def register(request: UserRegisterSchema, session: Session = Depends(get_session)):
    query = select(User).filter(User.username == request.username)
    user = session.execute(query).scalar_one_or_none()

    if user:
        raise HTTPException(status_code=409, detail="User already exists")

    new_user = User(
        username=request.username,
        hashed_password=get_password_hash(request.password),
        number=request.number,
        url_photo=request.url_photo,
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


@user_router.post("/login", response_model=UserGetSchema, status_code=200)
def login(request: UserLoginSchema, session: Session = Depends(get_session)):
    user: User = get_user_by_username(request.username, session)

    if not pwd_context.verify(request.password, user.hashed_password):
        raise HTTPException(status_code=403, detail="Incorrect credentials")
    return user


@user_router.get("", response_model=UserGetSchema, status_code=200)
def get_user_by_username(username: str, session: Session = Depends(get_session)):
    query = session.query(User).filter(User.username == username)
    user = session.execute(query).scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
