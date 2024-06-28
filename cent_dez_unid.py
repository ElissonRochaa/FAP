numero = input('Digite um numero inteiro até 1000: ')
numero = int(numero)

if numero > 0 and numero < 1000:
    centenas = numero // 100
    resto_centena = numero % 100
    dezena = resto_centena // 10
    unidade = resto_centena % 10
    if centenas > 0:
        print(f"Centenas: {centenas}, dezenas: {dezena} e unidades: {unidade}")
    elif dezena > 0:
        print(f"Dezenas: {dezena} e unidades: {unidade}")
    else:
        print(f"Unidades: {unidade}")
else:
    print("Numero invalido")
    