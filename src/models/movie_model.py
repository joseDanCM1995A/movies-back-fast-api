from pydantic import BaseModel, Field
from typing import Optional
import datetime

class Movie(BaseModel):
    id: Optional[int]
    title: str = Field(min_length=5, max_length=100)
    overview: str  = Field(min_length=10, max_length=500)
    year: int = Field(le=datetime.date.today().year, ge=1900)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=5, max_length=20)

    model_config = {
        'json_schema_extra': {
            'example': {
                'id': 0,
                'title': 'My movie',
                'overview': 'Esta pelicula habla acerca de...',
                'year': 2026,
                'rating': 2,
                'category': 'Comedia',
            }
        }
    }
