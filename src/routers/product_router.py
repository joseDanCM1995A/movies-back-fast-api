from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.models.product_model import Product


product_router = APIRouter()

@product_router.get('/', tags=['Products'])
def products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@product_router.get('/{id}', tags=['Products'])
def products(db: Session = Depends(get_db), id: int = Path(ge=0)):
    prod = db.query(Product).filter(Product.id == id).first()
    if prod is None:
        raise HTTPException(status_code=404, detail="product not found")
    return prod
