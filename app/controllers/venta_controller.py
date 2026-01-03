from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.services.venta_service import VentaService
from app.schemas.venta_schema import VentaCreate, VentaResponse

router = APIRouter(prefix="/ventas")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=VentaResponse)
def crear_venta(venta: VentaCreate, db: Session = Depends(get_db)):
    return VentaService(db).crear(venta)