from conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, senha, limite, saldo=0):
        super().__init__(titular, senha, saldo)
        self.limite = limite

    def detalhar_conta(self):
        return f"{self.titular} {self._ContaBancaria__saldo} {self.limite}"

    def sacar(self, valor):
        if valor < self._ContaBancaria__saldo + self.limite:
            self._ContaBancaria__saldo -= valor
            return True
        return False
