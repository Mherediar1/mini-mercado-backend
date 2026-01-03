class UsuarioRepository:
    def __init__(self, db):
        self.db = db

    def find_all(self, model):
        return self.db.query(model).all()