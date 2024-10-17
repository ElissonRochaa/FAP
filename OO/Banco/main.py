from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
from conta_especial import ContaEspecial
import random

def main():
    minha_conta = ContaCorrente('Elisson', '1234', 1000)
    minha_conta_poupanca = ContaPoupanca('Elisson', '1234')
    mc_especial = ContaEspecial("Bruno", '123', 0, 500, '12/12/2000')


    print("Conta Corrente")
    print("limite: ", minha_conta.limite)
    print("Meu saldo:", minha_conta.get_saldo())
    minha_conta.depositar(500)
    print("Meu saldo:", minha_conta.get_saldo())
    retorno = minha_conta.sacar(700)
    if retorno:
        print("Saque realizado com sucesso")
    else:
        print("Saque não realizado")
    print("Meu saldo:", minha_conta.get_saldo())

    retorno = minha_conta.sacar(2000)
    if retorno:
        print("Saque realizado com sucesso")
    else:
        print("Saque não realizado")
    print("Meu saldo:", minha_conta.get_saldo())
    print(minha_conta.detalhar_conta())


    print("Conta Poupança")
    print("Meu saldo:", minha_conta_poupanca.get_saldo())
    minha_conta_poupanca.depositar(200)
    print("Meu saldo:", minha_conta_poupanca.get_saldo())
    retorno = minha_conta_poupanca.sacar(300)
    if retorno:
        print("Saque realizado com sucesso")
    else:
        print("Saque não realizado")
    print("Meu saldo:", minha_conta_poupanca.get_saldo())
    minha_conta_poupanca.render_juros(10)
    print("Meu saldo:", minha_conta_poupanca.get_saldo())
    print(minha_conta_poupanca.detalhar_conta())

    print("Listas...")
    lista_contas = [minha_conta, minha_conta_poupanca]
    for conta in lista_contas:
        print(conta.detalhar_conta())


    print("Conta Especial")
    print(mc_especial.get_saldo())
    mc_especial.depositar(1000)
    print(mc_especial.detalhar_conta())

main()