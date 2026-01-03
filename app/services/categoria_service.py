from app.models.categoria import Categoria
from app.repositories.categoria_repo import CategoriaRepository

class CategoriaService:

    def __init__(self, repo: CategoriaRepository):
        self.repo = repo

    def obtener_todas(self):
        return self.repo.listar()

    def crear(self, nombre: str, descripcion: str):
        categoria = Categoria(nombre=nombre, descripcion=descripcion)
        return self.repo.crear(categoria)