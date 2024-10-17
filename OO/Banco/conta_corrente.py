from conta_bancaria import ContaBancaria
from Exception.negative_value_error import NegativeValueError

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, senha, limite, saldo=0):
        super().__init__(titular, senha, saldo)
        self.limite = limite

    def detalhar_conta(self):
        return f"{self.titular} {self._ContaBancaria__saldo} {self.limite}"

    def sacar(self, valor:int) -> bool:
        '''
        Essa função é para sacar o valor que ta na variavel tal...
        '''
        if isinstance(valor, int):
            if valor < 0:
                raise NegativeValueError("O valor do saque é negativo")
            if valor < self._ContaBancaria__saldo + self.limite:
                self._ContaBancaria__saldo -= valor
                return True
            return False
        else:
            raise ValueError("Valor não é inteiro")
