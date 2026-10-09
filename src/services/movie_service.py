from fastapi import HTTPException
from src.models.movie_model import Movie
from src.data.movies_data import movies



def get_all() -> list[dict]:
    return movies

def find_by_id(id):
    for movie in movies:
        if movie["id"] == id:
            return movie
    
    raise HTTPException(status_code=404, detail=f"Película con id {id} no encontrada")

def find_by_category(movie_cat):
    for movie in movies:
        if movie["category"] == movie_cat:
            return movie
    
    raise HTTPException(status_code=404, detail=f"Película con 'categoria' {movie_cat}")

def create_movie(new_movie: Movie):
    movies.append(new_movie.model_dump())
    return movies

def delete_by_id(id):
    if id < 0 or id >= len(movies):
        raise HTTPException(status_code=404, detail=f"Película con índice {id} no encontrada")
    
    movies.pop(id)

    return movies

def update_values(id: int, new_movie: Movie):
    idx = next((i for i, m in enumerate(movies) if m["id"] == id), None)
    if idx is None:
        raise HTTPException(status_code=404, detail=f"Película con id {id} no encontrada")
    
    movies[idx] = new_movie.model_dump()

    return movies

