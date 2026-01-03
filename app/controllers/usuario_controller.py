from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services.usuario_service import UsuarioService
from app.repositories.usuario_repo import UsuarioRepository

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.get("/")
def listar_usuarios(db: Session = Depends(get_db)):
    service = UsuarioService(UsuarioRepository(db))
    return service.listar()