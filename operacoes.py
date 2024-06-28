numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

print("Menu de operadores:")
print("1- Adição")
print("2- Subtração")
#print("3- Multiplicação")
#print("4- Divisão")
opcao = int(input('Escolha a opção desejada: '))

resultado = 0
if opcao == 1:
    resultado = numero1 + numero2
elif opcao == 2:
    resultado = numero1 - numero2
else:
    print("Opção Invalida")

par = False
positivo = False 
if resultado > -1:
    positivo = True

if resultado % 2 == 0:
    par = True


print("Resultado eh: ", resultado)
if par:
    print("O resultado é um numero par")
else:
    print("O resultado é um numero impar")
if positivo:
    print("O resultado é um numero positivo")
else:
    print("O resultado é um numero negativo")