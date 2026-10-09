from fastapi import FastAPI
from src.routers.movie_router import movie_router 

app = FastAPI()

@app.get('/', tags=['home'])
def home():
    return "Hola mundooooooo!"

app.include_router(prefix='/movies', router = movie_router)