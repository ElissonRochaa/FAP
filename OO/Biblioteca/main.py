from livro import Livro
from biblioteca import Biblioteca

def pegar_emprestado(livro):
    print("Pegando o livro emprestrado")
    foi_emprestado = livro.emprestar()
    if foi_emprestado:
        print("emprestimo realizado com sucesso")
    else:
        print("Emprestimo não realizado, livro não disponivel")

def main():
    #Cadastrando um Livro
    meu_livro = Livro(titulo="Antes que o café esfrie",
                      autor="Toshikazu Kawaguchi", ano="2022", 
                      editora="Valentina")
    
    meu_livro3 = Livro(ano=2024, titulo="Antes que o café esfrie 3", 
                       autor="Toshikazu Kawaguchi")
    meu_livro2 = Livro("Antes que o café esfrie 2",
                      "Toshikazu Kawaguchi", 2023, "Valentina")

    del meu_livro3

    print(meu_livro)

    biblioteca = Biblioteca("Biblioteca FAP")

    biblioteca.adicionar_livro(meu_livro)
    biblioteca.adicionar_livro(meu_livro2)
    #biblioteca.adicionar_livro(meu_livro3)

    print(biblioteca)
    #biblioteca.exibir()

    # meu_livro.exibir_infos()

    # #Pegando emprestado
    # pegar_emprestado(meu_livro)
    # #meu_livro.exibir_infos()

    # #Pegando emprestado
    # pegar_emprestado(meu_livro)

    # #Devolvendo
    # meu_livro.devolver()
    # meu_livro.exibir_infos()

main()