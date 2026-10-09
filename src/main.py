from __future__ import annotations
from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse, Response
from src.routers.movie_router import movie_router 
# from src.utils.http_error_handler import HttpErrorHandler

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
   



@app.get('/', tags=['home'])
def home():
    return "Hola mundooooooo!"

app.include_router(prefix='/movies', router = movie_router)