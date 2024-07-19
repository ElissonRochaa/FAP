
def verificar_par(numero):
    if numero % 2 == 0:
        return 'par'
    return 'impar'

def verificar_positivo(numero):
    if numero >= 0:
        return 'positivo'
    return 'negativo'

def verificar_inteiro(numero):
    if numero == round(numero):
    #if numero == int(numero)
        return 'inteiro'
    return 'decimal'

def realizar_operacao(numero1, numero2, operador):
    if operador == 1:
        return numero1 + numero2
    elif operador == 2:
        return numero1 - numero2
    elif operador == 3:
        return numero1 * numero2
    else:
        return numero1 / numero2

def menu_operador():
    print("Escolha a operação:")
    print("1-somar")
    print("2-subtrair")
    print("3-multiplicar")
    print("4-dividir")

def solicitar_numero(texto):
    return float(input(f"Digite o {texto} numero: "))

def main():
    numero1 = solicitar_numero("primeiro")
    numero2 = solicitar_numero("segundo")
    condicao = True
    menu_operador()
    while condicao:
        operador = int(input("Digite sua escolha: "))

        if operador >= 1 and operador <= 4:
            condicao = False

    if operador >= 1 and operador <=4:
        resultado = realizar_operacao(numero1=numero1, numero2=numero2, operador=operador)

        numero_par = verificar_par(resultado)
        numero_positivo = verificar_positivo(resultado)
        numero_inteiro = verificar_inteiro(resultado)

        print(f"O resultado foi {resultado} onde ele é {numero_par}, ",
              f"{numero_positivo} e {numero_inteiro}")
    else:
        print("Operador não reconhecido...")
        

main()