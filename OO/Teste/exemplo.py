from Exception.nomes_iguais_error import NomesIguaisError

class Exemplo:
    def __init__(self, nome):
        self.nome = nome
    
    def retornar_nome_mais_outro_nome(self, outro_nome):
        
        if isinstance(outro_nome, str):
            if self.nome == outro_nome:
                raise NomesIguaisError("Nomes iguais")
            return self.nome + outro_nome
        else:
            raise ValueError("Tipo só pode ser String")
