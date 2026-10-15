from __future__ import annotations
from fastapi import Cookie, Depends, Header, Path, Query, APIRouter, Response
from typing import Annotated, List, Optional

from src.models.movie_model import Movie
from src.services import movie_service
from src.utils.jwt_handler import encode_token, decode_token



movie_router = APIRouter()


@movie_router.get('/', tags=['laboratory'])
def get_movies(
    response: Response, 
    current_user: Annotated[dict, Depends(decode_token)],
    username: Annotated[Optional[str], Cookie()] = None,
    acces_token: Annotated[Optional[str], Header()] = None,
    ) -> List[Movie]:
    print(f"Usuario {current_user['username']} está creando una película")
    print("cookieeee received", username    )
    response.headers["user-status"] = 'active'
    response.set_cookie('username', 'dan')
    return movie_service.get_all()


@movie_router.get('/filters', tags=['laboratory'])
def get_movie_by_filter(category: str = Query(min_length=5, max_length=20))  -> Movie:
    return movie_service.find_by_category(category)
    
@movie_router.post('/', tags=['laboratory'])
def create_movie(movie: Movie, current_user: Annotated[dict, Depends(decode_token)]) -> List[Movie]:
  print(f"Usuario {current_user['username']} está creando una película")
  return movie_service.create_movie(movie)


@movie_router.get('/{id}', tags=['laboratory'])
def get_movie_by_id(id: int = Path(gt=0)) -> Movie:
    return movie_service.find_by_id(id)


@movie_router.put('/{id}', tags=['laboratory'])
def update_movie(current_user: Annotated[dict, Depends(decode_token)], new_movie: Movie, id: int = Path(ge=0)) -> List[Movie]:
    print(f"Usuario {current_user['username']} está creando una película")
    return movie_service.update_values(id, new_movie)

@movie_router.delete('/{id}', tags=['laboratory'])
def delete_movie(current_user: Annotated[dict, Depends(decode_token)], id: int = Path(ge=0)) -> List[Movie]:
    print(f"Usuario {current_user['username']} está creando una película")
    return movie_service.delete_by_id(id)


