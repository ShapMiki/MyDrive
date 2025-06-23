from fastapi import APIRouter, Request, Depends, HTTPException, Response
from fastapi.responses import RedirectResponse

from user.schemas import SUserRegistrate, SUserLogin
from user.dao import UserDAO
from user.auth import *
from user.dependencies import *
from exceptions import *



router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("/registrate")
async def register(responce: Response, user_data: SUserRegistrate):

    existing_user = await UserDAO.find_one_or_none(email=user_data.email)

    if existing_user:
        raise UserAlreadyExists

    hashed_password = get_password_hash(user_data.password)

    await UserDAO.add_one(password=hashed_password)#TODO:сделать

    user = await UserDAO.find_one_or_none(nickname=user_data.nickname)
    access_token = create_access_token(data={"sub": str(user.id)})
    responce.set_cookie(key="user_access_token", value=access_token, httponly=True)

@router.post("/login_api")
async def login(responce: Response, user_data: SUserLogin):
    user = await authenticate_user(user_data.namespace, user_data.password)

    if not user:
        raise IncorrectEmailOrPassword

    access_token = create_access_token(data={"sub": str(user.id)})
    responce.set_cookie(key="user_access_token", value=access_token, httponly=True, max_age=259200)
