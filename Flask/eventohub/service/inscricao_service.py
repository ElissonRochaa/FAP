from entity.inscricao import Inscricao
from repository.inscricao_repository import InscricaoRepository


class InscricaoService:

    @staticmethod
    def buscar_todos():
        return InscricaoRepository.get_all()
    
    @staticmethod
    def criar_inscricao(inscricao):
        return InscricaoRepository.create(inscricao)