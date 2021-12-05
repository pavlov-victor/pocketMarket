import datetime

from fastapi import APIRouter

from users.models import UserCreate, UserCredentials, UserRead
from utils.models import SuccessModel, TokenOutput

router = APIRouter()


@router.post('/users/register', tags=['users'], response_model=SuccessModel)
async def register_user(user: UserCreate):
    return SuccessModel(status=True)


@router.post('/users/login', tags=['users'], response_model=TokenOutput)
async def register_user(credentials: UserCredentials):
    return TokenOutput(access='1', refresh='2', expired=datetime.datetime.now())


@router.get("/users/me", tags=["users"], response_model=UserRead)
async def read_user_me():
    return UserRead(
        first_name='',
        last_name='',
        patronymic='',
        phone='',
        email='',
        birth_date='2021-12-12'
    )
