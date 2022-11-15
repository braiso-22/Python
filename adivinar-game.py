import random

'''
Programa para adivinar un número
'''


def menuSeleccion():
    print('''
    1. Jugar
    2. Salir
    ''')


def menuAdivinar():
    print('''
    Se ha generado un número aleatorio entre 1 y 100
    Tecla un número y enter para adivinar
    ''')


def juego(numero):
    fallos = 0
    menuAdivinar()
    while fallos < 5:
        numero_usuario = int(input())
        if numero_usuario < numero:
            print('El número es mayor')
        elif numero_usuario > numero:
            print('El número es menor')
        else:
            print('Has acertado')
            break
        fallos += 1
    print('Era el número', numero)


def generar_numero():
    numero = random.randint(1, 100)
    return numero


def main():
    while True:
        numero = generar_numero()
        menuSeleccion()
        seleccion = input()
        if seleccion == '1':
            juego(numero)
        elif seleccion == '2':
            break
        else:
            print('Opción no válida')
            pass


if __name__ == '__main__':
    main()
pass
