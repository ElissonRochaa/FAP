###
# 5x4x3x2x1
# 5x4 = 20
# 20x3 = 60 
# 60x2 = 120
# 120x1 = 120


def fatorial(valor, show=False):
    if valor < 0:
        return -1
    if valor == 0:
        return 1
    
    resultado = 1
    for n in range(valor, 0, -1):
        resultado = resultado*n
        if show:
            if n == 1:
                print(f'{n} = {resultado}')
            else:
                print(f'{n} x ',end='')

    return resultado

def main():
    try:
        numero = int(input("Digite um numero para o calculo de fatorial: "))
        resultado = fatorial(numero, show=True)
        if resultado == -1:
            print("Fatorial não existe")
        else:
            print(f"O fatorial de {numero} é {resultado}")
    except ValueError:
        print("O valor digitado não é um numero")


main()

