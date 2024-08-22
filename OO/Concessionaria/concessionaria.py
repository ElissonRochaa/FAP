from carro import Carro

def main():
    marca = input("Digite a marca do carro: ")
    modelo = input("Digite o modelo: ")
    ano = int(input("Digite o ano: "))

    meu_carro = Carro(marca, modelo, ano)

    while True:
        print("Menu:")
        print("1-Acelerar")
        print("2-Frear")
        print("3-Exibir informações")
        print("4-burlando o sistema")
        opcao = int(input("Digite a opção: "))

        if opcao == 1:
            meu_carro.acelerar()
        elif opcao == 2:
            meu_carro.frear()
        elif opcao == 3:
            meu_carro.exibir_infos()
            print("Velocidade Atual: ", meu_carro.get_velocidade_atual())
        elif opcao == 4:
            meu_carro.__velocidade = 500
        else:
            print("opcao invalida")

main()