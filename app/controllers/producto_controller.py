from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.schemas.producto_schema import ProductoCreate, ProductoResponse
from app.services.producto_service import ProductoService

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)


@router.get("/", response_model=list[ProductoResponse])
def listar(db: Session = Depends(get_db)):
    return ProductoService(db).listar()


@router.post("/", response_model=ProductoResponse)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    return ProductoService(db).crear(producto)