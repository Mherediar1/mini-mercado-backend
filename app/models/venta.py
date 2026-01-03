from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app.config.database import Base

class Venta(Base):
    __tablename__ = "ventas"

    id_venta = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, default=datetime.utcnow)  
    metodo_pago = Column(String)
    estado = Column(String)
    total_venta = Column(Float)
    impuestos = Column(Float)
    id_cliente = Column(Integer)

    detalles = relationship(
        "DetalleVenta",
        back_populates="venta",
        cascade="all, delete-orphan"
    )
