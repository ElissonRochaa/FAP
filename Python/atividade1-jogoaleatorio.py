import random

def main():
    continuar = True
    while continuar:
        numero_aleatorio = random.randint(1,100)
        numero_usuario = 0
        #cont = 0
        lista_numeros = []

        print("\nUm número inteiro aleatório de 1 a 100 foi gerado, tente adivinhar.\n")

        while numero_usuario != numero_aleatorio:

            numero_usuario = int(input("Dê o seu palpite: "))
            
            if numero_usuario > numero_aleatorio:
                print("O número informado é maior, tente um número menor.")
            elif(numero_usuario < numero_aleatorio):
                print("O número informado é menor, tente um número maior.")
            elif(numero_usuario < 1 or numero_usuario > 100):
                print("O número gerado é >= 1 e <= 100. Tente novamente.")
            
            lista_numeros.append(numero_usuario)
            
            #cont += 1

        print(f"\nParabéns! O número foi encontrado e era o número {numero_aleatorio}.")
        print(f"Quantidade de tentativas: {len(lista_numeros)}")
        print(f"Todos os números digitados nas tentativas: {lista_numeros}")

        valor = input('digite 0 para sair...')
        if valor == '0':
            continuar = False

main()
