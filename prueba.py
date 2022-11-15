string = "Hola Mundo, soy Brais"

for iterador, caracter in enumerate(string):
    print(iterador, caracter)

lista1 = [1, 2, 3,"f", 4, 5]
lista2 = ["a", "b", "c", "d", "e" ]

for i, j in zip(lista1, lista2):
    print(i, j)