
def bem_vindo():
    print("-------------------------------------")
    print("           FAMILY PETSHOP            ")
    print("-------------------------------------")
    print("--- Aqui seu animal é bem cuidado ---")
    print()
    print("--------------------------------------")
    print("Seja muito bem vindo")
    print("--------------------------------------")

def menu():
    print("Menu:")
    print("1-Valor a pagar")
    print("2-cadastrar")
    opcao = int(input("digite a opcao escolhida: "))
    return opcao

def calcular_servico(quant_servicos, quant_horas, valor_pago_hora=10):
    pagar = quant_horas*quant_servicos*valor_pago_hora
    desconto = pagar * 0.1
    return pagar, desconto


def main():
    bem_vindo()
    opcao = menu()

    if opcao == 1:
        q_serv = int(input("quantos servicos foram realizados: "))
        q_hor = float(input("quantas horas meu funcionario trabalhou: "))
        q_hor = round(q_hor,2)
        cobrar, desconto = calcular_servico(quant_horas=q_hor, quant_servicos=q_serv)
        #print("O usuario precisará pagar o valor de ", cobrar)
        print(f"O usuario solicitou {q_serv} serviços e meu funcionario precisou trabalhar {q_hor} horas, logo o usuario precisará pagar o valor de {cobrar-desconto}")

    # else:
    #     print("Escolheu a opcao 2")

main()