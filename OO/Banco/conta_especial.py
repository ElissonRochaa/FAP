from conta_corrente import ContaCorrente

class ContaEspecial(ContaCorrente):
    def __init__(self, titular, senha, saldo, limite, data):
        super().__init__(titular, senha, limite, saldo)
        self.data = data