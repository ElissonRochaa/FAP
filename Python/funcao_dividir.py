

def main():
    while True:
        try:
            numerador = int(input("Digite o numerador: "))
            denominador = int(input("Digite o denominador: "))
            break
        except ValueError:
            print("Infelizmente eu não consegui transformar o que você digitou em inteiro")
            print("Por favor Digite novamente")
    try:
        resultado = numerador/denominador
        print("O Resultado é ", resultado)
    except ZeroDivisionError:
        print("O denominador não pode ser 0")
    except Exception:
        print("Ocorreu um erro interno, fale com o suporte...")

main()