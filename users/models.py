from datetime import date
from typing import Optional

from sqlmodel import SQLModel


class UserCreate(SQLModel):
    email: str
    first_name: str
    last_name: str
    patronymic: str
    phone: str


class UserUpdate(SQLModel):
    first_name: str
    last_name: str
    patronymic: str
    phone: str


class UserRead(SQLModel):
    email: str
    first_name: str
    last_name: str
    patronymic: str
    phone: str
    birth_date: Optional[date]


class User(SQLModel):
    email: str
    first_name: str
    last_name: str
    patronymic: str
    phone: str
    password: str
    birth_date: Optional[date]


class UserCredentials(SQLModel):
    email: str
    password: str
