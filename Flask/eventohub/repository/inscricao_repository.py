from entity.inscricao import Inscricao
from app import db

class InscricaoRepository:

    @staticmethod
    def get_all():
        return Inscricao.query.all()
    
    @staticmethod
    def create(inscricao):

        try:
            db.session.add(inscricao)
            db.session.commit()
            return inscricao
        except Exception as e:
            db.session.rollback()
            raise e