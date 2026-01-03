from pydantic import BaseModel, EmailStr
from typing import Optional


# ----------- ENTRADA (CREATE) -----------
class UsuarioCreate(BaseModel):
    nombre: str
    username: str
    password: str
    rol: str
    email: Optional[EmailStr] = None


# ----------- SALIDA (RESPONSE) -----------
class UsuarioResponse(BaseModel):
    id_usuario: int
    nombre: str
    username: str
    rol: str
    email: Optional[EmailStr] = None
    estado: str

    class Config:
        from_attributes = True  # Pydantic v2