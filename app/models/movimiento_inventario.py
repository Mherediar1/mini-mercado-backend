from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.config.database import Base
from datetime import date

class MovimientoInventario(Base):
    __tablename__ = "movimientos_inventario"

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, default=date.today)
    tipo_movimiento = Column(String(20))  # ENTRADA / SALIDA
    sku_producto = Column(String, ForeignKey("productos.sku"))
    cantidad = Column(Integer)