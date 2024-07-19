

def main():

    quantidade = 5
    soma = 0
    maior = 0
    for i in range(quantidade):
        numero = int(input(f"Digite o {i+1}º numero: "))
        soma = soma + numero
        if i == 0:
            maior = numero

        if numero > maior:
            maior = numero

        #soma += numero
    media = soma/quantidade

    print("Soma: ", soma)
    print("Media: ", media)
    print("Maior numero digitado: ", maior)



main()