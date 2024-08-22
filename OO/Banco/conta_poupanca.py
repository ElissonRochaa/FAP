from conta_bancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, senha, saldo=0):
        super().__init__(titular, senha, saldo)
        
    def detalhar_conta(self):
        return f"{self.titular} {self._ContaBancaria__saldo}"

    def render_juros(self, porcentagem):
        rendimento = self._ContaBancaria__saldo * (porcentagem/100)
        self._ContaBancaria__saldo += rendimento   