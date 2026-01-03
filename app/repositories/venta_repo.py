class VentaRepository:
    def __init__(self, db):
        self.db = db

    def crear(self, venta):
        self.db.add(venta)
        self.db.commit()
        self.db.refresh(venta)
        return venta