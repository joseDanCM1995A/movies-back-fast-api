from __future__ import annotations
from fastapi import FastAPI, status, Depends
from fastapi.requests import Request
from fastapi.responses import JSONResponse, Response
from src.routers.movie_router import movie_router 
from src.routers.user_router import user_router 
from src.data.users_data import users

app = FastAPI()

@app.middleware('http')
async def http_error_handler(request: Request, call_next) -> Response | JSONResponse:
    print('middleware is running')
    try:
        return await call_next(request)
    except Exception as e:
        content = f'exc: {str(e)}'
        status_code =status.HTTP_500_INTERNAL_SERVER_ERROR
        return JSONResponse(content = content, status_code = status_code)

app.include_router(router = user_router)

app.include_router(prefix='/movies', router = movie_router)