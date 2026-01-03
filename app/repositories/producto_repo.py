from app.models.producto import Producto

class ProductoRepository:
    def __init__(self, db):
        self.db = db

    def find_all(self):
        return self.db.query(Producto).all()

    def obtener_por_sku(self, sku: str):
        return (
            self.db.query(Producto)
            .filter(Producto.sku == sku)
            .first()
        )

    def crear(self, producto: Producto):
        self.db.add(producto)
        self.db.commit()
        self.db.refresh(producto)
        return producto
