import random


def menuSeleccion():
    print('''
    1. Jugar
    2. Salir
    ''')


def generar_numero(rango):
    numero = random.randint(rango[1], rango[-1])
    return numero


def juego():
    numero = int(input('Introduce un número del 1 al 100: '))
    print('El número que tiene que adivinar la máquina es: ', numero)
    fallos = 0
    ultimo_intento = 0
    rango = range(1, 101)

    while fallos < 5:
        ultimo_intento = generar_numero(rango)
        
        input(f'Es el número {ultimo_intento}?')
        if (ultimo_intento < numero):
            print('El número es mayor')
            rango = range(ultimo_intento, rango[-1]+1)
        elif (ultimo_intento > numero):
            print('El número es menor')
            rango = range(rango[0], ultimo_intento)
        else:
            print('Has acertado')
            break
        fallos += 1
        pass


def main():
    while True:
        menuSeleccion()
        seleccion = input()
        if seleccion == '1':
            juego()
        elif seleccion == '2':
            break
        else:
            print('Opción no válida')
            pass


if __name__ == '__main__':
    main()
pass
