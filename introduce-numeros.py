# Un programa en el que se introducen numeros y se imprime la lista de numeros introducidos


def pedirNumeros():
    lista = []
    while True:
        numero = input('Introduce un numero(-1 para salir): ')
        if numero == "":
            break
        elif numero.isdigit():
            lista.append(int(numero))
        else:
            print('No es un numero')
    return lista


def mediana(lista):
    lista.sort()
    if len(lista) % 2 == 0:
        return (lista[len(lista)//2] + lista[len(lista)//2 - 1])/2

    return lista[len(lista)//2]


def varianza(lista):
    media = sum(lista)/len(lista)
    varianza = 0
    for i in lista:
        varianza += (i - media)**2
    return varianza/len(lista)


def desviacionTipica(lista):
    return varianza(lista)**0.5


def count(lista, elemento):
    contador = 0
    for i in lista:
        if i == elemento:
            contador += 1
    return contador


def moda(lista):
    elemento_mas_repetido = lista[0]
    for i in lista:
        if count(lista, i) > count(lista, elemento_mas_repetido):
            elemento_mas_repetido = i
    return elemento_mas_repetido


def estadisticas(lista):
    print('La lista es: ', lista)
    print('El numero de elementos es: ', len(lista))
    print('El mayor es: ', max(lista))
    print('El menor es: ', min(lista))
    print('La suma es: ', sum(lista))
    print('La media es: ', sum(lista)/len(lista))
    print('La mediana es: ', mediana(lista))
    print('La moda es: ', max(set(lista), key=lista.count))
    print('La varianza es: ', varianza(lista))
    print('La desviacion tipica es: ', desviacionTipica(lista))


def main():
    lista = pedirNumeros()
    estadisticas(lista)


if __name__ == '__main__':
    #main()
    print(max([6,7],key=[6,6,6,6,6,6].count))
