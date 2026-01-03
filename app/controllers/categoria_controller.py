from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services.categoria_service import CategoriaService
from app.repositories.categoria_repo import CategoriaRepository

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.get("/")
def listar_categorias(db: Session = Depends(get_db)):
    service = CategoriaService(CategoriaRepository(db))
    return service.obtener_todas()

@router.post("/")
def crear_categoria(nombre: str, descripcion: str, db: Session = Depends(get_db)):
    service = CategoriaService(CategoriaRepository(db))
    return service.crear(nombre, descripcion)