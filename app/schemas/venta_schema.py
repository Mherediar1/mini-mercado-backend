from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# ----------- DETALLE DE VENTA -----------
class DetalleVentaCreate(BaseModel):
    sku_producto: str
    cantidad: int
    precio_unitario: float
    descuento: float = 0


# ----------- ENTRADA (CREATE) -----------
class VentaCreate(BaseModel):
    metodo_pago: str
    id_cliente: Optional[int] = None
    detalles: List[DetalleVentaCreate]


# ----------- SALIDA (RESPONSE) -----------
class VentaResponse(BaseModel):
    id_venta: int
    fecha: datetime
    total_venta: float
    impuestos: float
    metodo_pago: str
    estado: str

    class Config:
        from_attributes = True  # Pydantic v2