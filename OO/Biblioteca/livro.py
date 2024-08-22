class Livro:
    #Meu Construtor
    def __init__(self, titulo, autor, ano, editora="Não informado"):
        #Atributos
        #Os atributos obrigatorios precisam tá nos
        #parametros sem valor predefinido, como é o caso do
        #titulo, autor e ano.
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        #O atributo opcional precisa ta nos parametros com um
        #valor predefinido, como é o caso da editora. 
        self.editora = editora
        #O atributo que sempre será o mesmo valor, não se coloca
        #nos parametros, como é o caso do disponivel
        self.disponivel = True

    def __del__(self):
        print("Delentando um livro...")

    def __str__(self):
        return f"Livro: {self.titulo} e {self.ano}"

    def exibir_infos(self):
        print("-"*30)
        print("Livro:")
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ano: {self.ano}")
        print(f"editora: {self.editora}")
        if self.disponivel:
            print("Livro disponivel para emprestimo")
        else:
            print("Livro não disponivel para emprestimo")
        print("-"*30)
    
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        else:
            return False
    
    def devolver(self):
        if self.disponivel == False:
            self.disponivel = True
            return True
        else:
            return False