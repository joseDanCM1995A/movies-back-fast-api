
from fastapi import Path, Query, APIRouter
from typing import List

from src.models.movie_model import Movie
from src.services import movie_service
movie_router = APIRouter()


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado pandora viven los Na'vi ...",
        "year": 2009,
        "rating": 7.8,
        "category": "Accion",
    },
    {
        "id": 2,
        "title": "Titanic",
        "overview": "Un joven artista se enamora de una pasajera de primera clase a bordo del ...",
        "year": 1997,
        "rating": 7.9,
        "category": "Romance",
    },
    {
        "id": 3,
        "title": "Inception",
        "overview": "Un ladrón que roba secretos a través de la tecnología de sueños ...",
        "year": 2010,
        "rating": 8.8,
        "category": "Ciencia Ficcion",
    },
    {
        "id": 4,
        "title": "The Dark Knight",
        "overview": "Batman enfrenta al Joker, un criminal que siembra el caos en Gotham ...",
        "year": 2008,
        "rating": 9.0,
        "category": "Accion",
    },
    {
        "id": 5,
        "title": "Interstellar",
        "overview": "Un grupo de exploradores viaja a través de un agujero de gusano ...",
        "year": 2014,
        "rating": 8.6,
        "category": "Ciencia Ficcion",
    },
    {
        "id": 6,
        "title": "El Señor de los Anillos",
        "overview": "Un hobbit debe destruir un anillo poderoso para salvar la Tierra Media ...",
        "year": 2001,
        "rating": 8.8,
        "category": "Fantasia",
    },
    {
        "id": 7,
        "title": "Pulp Fiction",
        "overview": "Las vidas de dos sicarios, un boxeador y un gánster se entrelazan ...",
        "year": 1994,
        "rating": 8.9,
        "category": "Crimen",
    },
    {
        "id": 8,
        "title": "Toy Story",
        "overview": "Un vaquero de juguete y un guardián espacial aprenden a convivir ...",
        "year": 1995,
        "rating": 8.3,
        "category": "Animacion",
    },
    {
        "id": 9,
        "title": "Matrix",
        "overview": "Un hacker descubre que la realidad es una simulación creada por máquinas ...",
        "year": 1999,
        "rating": 8.7,
        "category": "Ciencia Ficcion",
    },
    {
        "id": 10,
        "title": "Gladiator",
        "overview": "Un general romano traicionado busca venganza como gladiador ...",
        "year": 2000,
        "rating": 8.5,
        "category": "Accion",
    },
]


@movie_router.get('/', tags=['laboratory'])
def get_movies() -> List[Movie]:
    return movie_service.get_all()


@movie_router.get('/filters', tags=['laboratory'])
def get_movie_by_filter(category: str = Query(min_length=5, max_length=20))  -> Movie:
    return movie_service.find_by_category(category)
    
@movie_router.post('/', tags=['laboratory'])
def create_movie(movie: Movie) -> List[Movie]:
  return movie_service.create_movie(movie)


@movie_router.get('/{id}', tags=['laboratory'])
def get_movie_by_id(id: int = Path(gt=0)) -> Movie:
    return movie_service.find_by_id(id)


@movie_router.put('/{id}', tags=['laboratory'])
def update_movie(new_movie: Movie, id: int = Path(ge=0)) -> List[Movie]:
    return movie_service.update_values(id, new_movie)

@movie_router.delete('/{id}', tags=['laboratory'])
def delete_movie(id: int = Path(ge=0)) -> List[Movie]:
    return movie_service.delete_by_id(id)


