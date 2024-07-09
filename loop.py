###for
# def main():

#     print("Iniciando...")
#     for i in range(10):
#         if i % 2 == 0:
#             print(i)
    
#     print("Acabou")

#     for i in range(10, -1, -2):
#         print(i)

#while
def main():
    i = 0
    # while i < 5:
    #     print(i)
    #     i = i + 1

    contador = 1
    condicao = True
    while condicao:
        print(contador)
        opcao = input("Digite 0 para finalizar o programa: ")
        if opcao == '0':
            condicao = False
        else:
            contador = contador+1

main()