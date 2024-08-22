
class Carro:
    #Caracteristicas - Atributo - Variavel
    def __init__(self, marca, modelo, ano, velocidade_maxima=150):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade_maxima = velocidade_maxima
        self.__velocidade = 0

    #Comportamentos - métodos -> funções
    def exibir_infos(self):
        print(f"{self.marca} {self.modelo} {self.ano}")
    
    def get_velocidade_atual(self):
        return self.__velocidade

    def acelerar(self):
        self.__velocidade += 15
        if self.__velocidade > self.velocidade_maxima:
            self.__velocidade = self.velocidade_maxima

    def frear(self):
        self.__velocidade -= 15
        if self.__velocidade < 0:
            self.__velocidade = 0
