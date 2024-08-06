

def acelerar(velocidade):
    nova_velocidade = velocidade + 5
    return nova_velocidade if nova_velocidade < 150 else 150

def frear(velocidade):
    nova_velocidade = velocidade - 5
    return nova_velocidade if nova_velocidade > 0 else 0

def exibir_infos(marca, modelo, ano, velocidade):
    print(marca, modelo, ano, velocidade)

def main():
    
    acelerar(5)

    marca = input("Digite a marca do carro: ")
    modelo = input("Digite o modelo: ")
    ano = int(input("Digite o ano: "))

    velocidade_atual = 0

    while True:
        print("Menu:")
        print("1-Acelerar")
        print("2-Frear")
        print("3-Exibir informações")
        opcao = int(input("Digite a opção: "))

        if opcao == 1:
            velocidade_atual = acelerar(velocidade_atual)
        elif opcao == 2:
            velocidade_atual = frear(velocidade_atual)
        elif opcao == 3:
            exibir_infos(marca, modelo, ano, velocidade_atual)
        else:
            print("opcao invalida")

main()