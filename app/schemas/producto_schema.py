from pydantic import BaseModel

class ProductoCreate(BaseModel):
    sku: str
    nombre: str
    precio: float
    stock_actual: int

class ProductoResponse(BaseModel):
    sku: str
    nombre: str
    precio: float
    stock_actual: int

    class Config:
        orm_mode = True