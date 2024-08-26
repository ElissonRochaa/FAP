from abc import abstractmethod, ABC

##Classe vai ser abstrata
class ContaBancaria(ABC):
    def __init__(self, titular, senha, saldo=0):
        self.titular = titular
        self.__senha = senha
        self.__saldo = saldo

    @abstractmethod
    def detalhar_conta(self):
        pass

    def get_saldo(self):
        return self.__saldo

    def validar_senha(self, senha):
        if self.__senha == senha:
            return True
        return False

    def alterar_senha(self, senha:str) -> None:
        self.__senha = senha

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False

    def sacar(self, valor):
        if valor < self.__saldo:
            self.__saldo -= valor
            return True
        return False
  