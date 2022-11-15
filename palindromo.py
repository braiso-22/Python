"""
    Programa que dice si una frase es palindromo o no
"""

def quitar_tildes(frase):
    frase = frase.replace('á', 'a')
    frase = frase.replace('é', 'e')
    frase = frase.replace('í', 'i')
    frase = frase.replace('ó', 'o')
    frase = frase.replace('ú', 'u')
    return frase

def es_palindromo(frase):
    frase = frase.replace(' ', '')
    frase = frase.lower()
    frase = quitar_tildes(frase)
    frase_invertida = frase[::-1]
    if frase == frase_invertida:
        return True
    else:
        return False

def funcion():
    frase = input("Introduce una frase y te digo si es palíndromo: ")
    if es_palindromo(frase):
        print("Es palíndromo")
    else:
        print("No es palíndromo")

def menuSeleccion():
    print('''
    1. Trabajar
    2. Salir
    ''')

def main():
    while True:
        menuSeleccion()
        seleccion = input()
        if seleccion == '1':
            funcion()
        elif seleccion == '2':
            break
        else:
            print('Opción no válida')
            pass

if __name__ == '__main__':
    main()