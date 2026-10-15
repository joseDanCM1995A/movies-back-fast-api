

from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.data.users_data import users

from src.utils.jwt_handler import encode_token, decode_token


user_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@user_router.post('/login', tags=['Auth'])
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> dict:
    user = users.get(form_data.username)
    if not user or form_data.password != user["password"]:
        raise HTTPException(status_code=400, detail="Incorrect credentials")
    token = encode_token({"username": user['username'], "email": user["email"]})
    return {"access_token": token, "token_type": "bearer"}
    
@user_router.post('/users/profile', tags=['Users'])
def profile(my_user: Annotated[dict, Depends(decode_token)]) -> dict:
    return my_user

