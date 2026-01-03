from fastapi import FastAPI
from app.config.database import Base, engine
from app.controllers.usuario_controller import router as usuario_router
from app.controllers.producto_controller import router as producto_router
from app.controllers.venta_controller import router as venta_router
from app.controllers.categoria_controller import router as categoria_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mini Mercado API")

app.include_router(usuario_router)
app.include_router(producto_router)
app.include_router(venta_router)
app.include_router(categoria_router)