from sqlalchemy import Column, BigInteger, String, Float, Integer
from src.config.db import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)      
    quantity = Column(Integer, nullable=False)  