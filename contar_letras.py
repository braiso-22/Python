# Contar cuantas veces aparece una letra en una cadena


def contar_letras(cadena):
    diccionario = {}
    for letra in cadena:
        '''
        if letra not in diccionario:
            diccionario[letra] = 1
        else:
            diccionario[letra] += 1
        '''
        diccionario[letra] = diccionario.get(letra, 0) + 1
    return diccionario


def main():
    cadena = input("Introduce una cadena: ")
    diccionario = contar_letras(cadena)
    '''
    {print(clave, valor) for clave, valor in diccionario.items()}
    '''
    for clave, valor in diccionario.items():
        print(clave, valor)
    pass


if __name__ == "__main__":
    main()
