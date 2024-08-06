
def verificar_fibonacci(penultimo, ultimo, numero):
    if numero == ultimo:
        return True
    elif numero < ultimo:
        return False
    return verificar_fibonacci(penultimo=ultimo, ultimo=penultimo+ultimo, 
                        numero=numero)

def fibonacci(numero):
    return verificar_fibonacci(0, 1, numero)

# def fibonacci(numero):
#     ## Inicia no valor 0 e 1
#     penultimo = 0
#     ultimo = 1
#     while True:
#         proximo = penultimo + ultimo
#         if proximo == numero:
#             return True
#         elif proximo > numero:
#             return False
#         penultimo = ultimo
#         ultimo = proximo


def main():
    while True:
        try:
            numero = int(input("Digite o numero para verificar se faz parte da sequencia de fibonacci: "))
            if fibonacci(numero):
                print("Faz parte")
            else:
                print("Não faz parte")
        except ValueError:
            print("Só pode ser digitado numeros inteiros")
        except Exception as e:
            print(f"Erro inesperado: {e}")


main()