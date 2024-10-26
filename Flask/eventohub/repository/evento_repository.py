from db import db
from entity.evento import Evento

class EventoRepository:

    @staticmethod
    def get_all():
        return Evento.query.all()
    
    @staticmethod
    def create(evento):
        try:
            db.session.add(evento)
            db.session.commit()
            return evento
        except Exception as e:
            db.session.rollback()
            raise e
