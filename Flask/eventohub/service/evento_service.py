from entity.evento import Evento
from repository.evento_repository import EventoRepository

class EventoService:

    @staticmethod
    def buscar_todos():
        return EventoRepository.get_all()
    
    @staticmethod
    def create(evento):
        return EventoRepository.create(evento)
