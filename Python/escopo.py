def teste():
    resultado = 10
    print("resultado (teste): ", resultado)
    return resultado

def main():
    resultado = 20
    print("resultado (main): ", resultado)
    resultado = teste()
    print("resultado (main): ", resultado)


#main()