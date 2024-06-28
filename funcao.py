def somar(a=0, b=0):
    resultado = a + b
    return resultado


def somar2(numeros:list):
    soma = 0
    for numero in numeros:
        soma = soma + numero
    return soma


def main():
    numero1 = 5
    numero2 = 7
    resultado = somar(numero1, numero2)
    print(resultado)

if __name__ == "__main__":
    main()