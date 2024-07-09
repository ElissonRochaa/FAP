## Trabalhando com listas
## Criar uma lista com 5 elementos
lista_frutas = ['Maça', 'Limão', 'Laranja', 'Mamão', 'Manga']
print(lista_frutas)

### Imprimir o terceiro elemento da lista
### Laranja
print(lista_frutas[2])

### Modificar o segundo elemento por 'Banana'
lista_frutas[1] = 'bAnaNA'
print(lista_frutas)

## Adicionar abacate ao final da lista
lista_frutas.append('Abacate')
#lista_frutas.insert(len(lista_frutas), 'Abacate')
print(lista_frutas)

## Remover a terceira fruta da lista
del lista_frutas[2]
#lista_frutas.pop(2)
print(lista_frutas)

### Remover e imprimir a ultima fruta
fruta_removida = lista_frutas.pop(-1)
print("Fruta removida: ", fruta_removida)
print(lista_frutas)

### imprimir o tamanho da lista
print("Tamanho da lista: ", len(lista_frutas))

### imprimir todas as frutas menos a banana
#print(lista_frutas)
for fruta in lista_frutas:
    if fruta.lower != 'banana':
        print(fruta)

