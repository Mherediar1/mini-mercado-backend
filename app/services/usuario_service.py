from app.repositories.usuario_repo import UsuarioRepository
from app.models.usuario import Usuario

class UsuarioService:
    def __init__(self, db):
        self.repo = UsuarioRepository(db)

    def listar(self):
        return self.repo.find_all(Usuario)