
def solicitar_numero():
    condicao = True
    numero = 0
    while condicao:
        numero = input('Digite um numero inteiro entre 1 e 999 (0 para encerrar):')
        numero = int(numero)
        if numero >= 0 and numero < 1000:
            condicao = False
    return numero

def calcular_divisao_inteira_e_resto(valor, denominador):
    divisao = valor // denominador
    resto = valor % denominador

    return divisao, resto

def main():
    condicao = True
    while condicao:
        numero = solicitar_numero()

        if numero == 0:
            break

        # centenas = numero // 100
        # resto_centena = numero % 100
        # dezena = resto_centena // 10
        # unidade = resto_centena % 10
        centenas, resto_centena = calcular_divisao_inteira_e_resto(numero, 100)
        dezena, unidade = calcular_divisao_inteira_e_resto(resto_centena, 10)
        
        if centenas > 0:
            print(f"Centenas: {centenas}, dezenas: {dezena} e unidades: {unidade}")
        elif dezena > 0:
            print(f"Dezenas: {dezena} e unidades: {unidade}")
        else:
            print(f"Unidades: {unidade}")
    
    ### MOSTRAR NA TELA TODOS OS NUMEROS CONSULTADOS
    ### print(LISTA)

main()