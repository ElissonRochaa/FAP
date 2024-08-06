
class Carro:
    #Caracteristicas - Atributo - Variavel
    def __init__(self, marca, modelo, ano, velocidade_maxima=150):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade_maxima = velocidade_maxima
        self.velocidade = 0

    #Comportamentos - métodos -> funções
    def exibir_infos(self):
        print(f"{self.marca} {self.modelo} {self.ano}")
    
    def acelerar(self):
        self.velocidade += 5
        if self.velocidade > self.velocidade_maxima:
            self.velocidade = self.velocidade_maxima

    def frear(self):
        self.velocidade -= 5
        if self.velocidade < 0:
            self.velocidade = 0
