from app.repositories.producto_repo import ProductoRepository
from app.models.producto import Producto

class ProductoService:
    def __init__(self, db):
        self.repo = ProductoRepository(db)

    def listar(self):
        return self.repo.find_all(Producto)

    def crear(self, producto_data):
        producto = Producto(**producto_data.dict())
        return self.repo.crear(producto)