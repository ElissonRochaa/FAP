## Vamos criar um programa de cadastro de produtos

def cadastro_produto():
    ### Nome, valor_venda, valor_compra, codigo_barra
    print("Cadastrando um novo produto:")
    nome = input("Digite o nome do novo produto: ")
    valor_compra = float(input(f"Digite o valor de compra do produto {nome}"))
    valor_venda = float(input(f"Digite o valor de venda do produto {nome}"))
    codigo_barra = float(input(f"Digite o codigo de barra do produto {nome}"))

    produto = {
        'Nome':nome, 
        'Valor_compra':valor_compra, 
        'Valor_venda':valor_venda, 
        'codigo_barra':codigo_barra
        }
    return produto

def menu():
    print("Bem vindo ao mercado FAP")
    print("Menu:")
    print("1-Cadastrar Produto novo")
    print("2-Listar Produtos")
    print("3-Sair")

def main():
    lista_produtos = []
    while True:
        menu()
        
        opcao = int(input("Digite a opcao desejada: "))

        if opcao == 1:
            produto = cadastro_produto()
            lista_produtos.append(produto)
        if opcao == 2:
            for produto in lista_produtos:
                print("Produto:")
                print(produto['Nome'])
                print(produto['Valor_venda'])
                print()
        if opcao == 3:
            break
    
    print("Finalizando o codigo")
    print("Tentando usar o git no vscode")

main()