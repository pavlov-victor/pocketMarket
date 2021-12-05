from fastapi import Depends, FastAPI

from dependences import get_query_token
from routers import users

app = FastAPI()

app.include_router(users.router)

