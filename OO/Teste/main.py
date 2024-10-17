from exemplo import Exemplo
from Exception.nomes_iguais_error import NomesIguaisError
a = Exemplo("Elisson")

try:
    resultado = a.retornar_nome_mais_outro_nome(10)
    print(resultado)
except ValueError:
    print("Veja, você tem que passar uma string para esse metodo")
except NomesIguaisError:
    print("O nome não pode ser igual ao nome que está na classe")
except Exception:
    print("Erro inesperado....")
