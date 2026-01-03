from sqlalchemy import Column, Integer, String, Enum
from app.config.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    username = Column(String, unique=True)
    password = Column(String)
    rol = Column(String)