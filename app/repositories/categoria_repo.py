from sqlalchemy.orm import Session
from app.models.categoria import Categoria

class CategoriaRepository:

    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        return self.db.query(Categoria).all()

    def crear(self, categoria: Categoria):
        self.db.add(categoria)
        self.db.commit()
        self.db.refresh(categoria)
        return categoria