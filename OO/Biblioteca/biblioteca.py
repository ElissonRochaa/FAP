
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.lista_livros = []
    
    def adicionar_livro(self, livro):
        self.lista_livros.append(livro)

    def __str__(self):
        return "Minha biblioteca"

    def exibir(self):
        print(self.nome)
        print(self.lista_livros)
        # for livro in self.lista_livros:
        #     livro.exibir_infos()