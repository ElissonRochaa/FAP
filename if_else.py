valor_a_sacar = 18
valor_em_conta = 20
valor_em_caixa = 15

condicao = valor_a_sacar <= valor_em_conta
if condicao:
    print("Primeira etapa okay, tem dinheiro em conta")
    if valor_a_sacar <= valor_em_caixa:
        print("Saque realizado")
        valor_em_conta = valor_em_conta - valor_a_sacar
        print("Valor atualizado com sucesso")
    else:
        print("Valor em caixa insuficiente")
else:
    print("Saldo insuficiente")

print("Encerrando atendimento")