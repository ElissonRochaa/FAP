from carro import Carro

def main():
    meu_carro = Carro("Fiat", "Uno", 2000)
    meu_carro.exibir_infos()
    print(meu_carro.velocidade)
    meu_carro.acelerar()
    meu_carro.acelerar()
    meu_carro.acelerar()
    print(meu_carro.velocidade)
    meu_carro.frear()
    print(meu_carro.velocidade)
    #exibir_infos()

if __name__ == "__main__":
    main()