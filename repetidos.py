#dada la lista de numeros, quitar los repetidos.
[1, 2, 2, 3, 2, 1]

#dada la lista de numeros, juntar los repetidos y mostrar cuantos hay de cada uno
[1, 2, 2, 2, 3, 2, 1]

lista1 = [1, 2, 2, 3, 2, 1]
lista2 = [1, 2, 2, 2, 3, 2, 1]

def quitar(lista):
    return list(set(lista))
print(quitar(lista1))

def repetidos(lista):
    return {i: lista.count(i) for i in lista}
print(repetidos(lista2))