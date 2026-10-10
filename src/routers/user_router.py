

from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.data.users_data import users
from jose import jwt


user_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def encode_token(payload: dict) -> str:
    token = jwt.encode(payload, "my_secret", algorithm="HS256")
    return token

def decode_token(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    data = jwt.decode(token, "my_secret", algorithms=["HS256"])
    user = users.get(data["username"])
    return user


@user_router.post('/login', tags=['Auth'])
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> dict:
    user = users.get(form_data.username)
    if not user or form_data.password != user["password"]:
        raise HTTPException(status_code=400, detail="Incorrect credentials")
    token = encode_token({"username": user['username'], "email": user["email"]})
    return {"access_token": token}
    
@user_router.post('/users/profile', tags=['Users'])
def profile(my_user: Annotated[dict, Depends(decode_token)]) -> dict:
    return my_user

