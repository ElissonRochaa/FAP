from entity.usuario import Usuario
from db import db

class UsuarioRepository:

    #def buscar_todos():
    @staticmethod
    def get_all():
        return Usuario.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)
    
    @staticmethod
    def get_by_email(email):
        return Usuario.query.filter_by(email=email).first()

    @staticmethod
    def create(usuario):
        db.session.add(usuario)
        db.session.commit()
        return usuario