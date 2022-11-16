string = "Hola Mundo, soy Brais"

for iterador, caracter in enumerate(string):
    print(iterador, caracter)

lista1 = [1, 2, 3, "f", 4, 5]
lista2 = ["a", "b", "c", "d", "e"]

for i, j in zip(lista1, lista2):
    print(i, j)


array_prueba = [letra for letra in string if letra != " "]

print(array_prueba)

array_prueba = [i for i in range(11)]
print(array_prueba)

array_prueba = [[(j + 1 + i * 3) for j in range(3)] for i in range(3)]
print(array_prueba)

array_prueba = [[], [], []]
for i in range(3):
    for j in range(3):
        array_prueba[i].append(j + 1 + i * 3)
print(array_prueba)

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tupla[0])
tupla = (1,)
print(tupla)

set = {9, 2, 3, 3, 4, 4, 4, 5}
print(set)

set.add(6)
print(set)

set.pop()  # Elimina el primer elemento por orden ascendente
print(set)

print(4 in set)

set2 = {4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

print(set | set2)  # Union
print(set & set2)  # Interseccion

diccionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(diccionario)
print(diccionario["a"])
print(diccionario.keys())
print(diccionario.values())

for tupla in diccionario.items():
    print(tupla)

for clave, valor in diccionario.items():
    print(clave, valor)