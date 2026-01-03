from sqlalchemy import Column, String, Integer, Float
from app.config.database import Base

class Producto(Base):
    __tablename__ = "productos"

    sku = Column(String, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)      
    stock_actual = Column(Integer, nullable=False)

