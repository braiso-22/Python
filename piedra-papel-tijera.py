import random
from os.path import exists
import time


def menuSeleccion():
    print('''
    1. Jugar
    2. Salir
    ''')


def menu_juego():
    return int(input('''
    1. Piedra
    2. Papel
    3. Tijera
    '''))


def mostrar_resultados(opciones, seleccion_maquina, seleccion_jugador):

    # un array bidimensional para comparar las opciones
    # 0 = piedra
    # 1 = gana jugador
    # 2 = gana maquina
    finales = [
        [0, 2, 1],
        [1, 0, 2],
        [2, 1, 0]
    ]
    finales_text = ['Empate', 'Has ganado', 'Has perdido']

    print('\nHas elegido ', opciones[seleccion_jugador])
    print('\nLa máquina ha elegido ', opciones[seleccion_maquina])

    resultado = finales[seleccion_jugador][seleccion_maquina]
    print(f'\n{finales_text[resultado]}')
    
    pass

def save_data(seleccion_jugador, seleccion_maquina):
    if not exists("./files/save-piedra-papel-tijera.csv"):
        with open("./files/save-piedra-papel-tijera.csv", "w") as f:
            f.write("jugador;maquina;fecha\n")

    with open('./files/save-piedra-papel-tijera.csv', 'a') as f:
        f.write(f'{seleccion_jugador};{seleccion_maquina};{time.time()}\n')
        

def juego():
    opciones = ['piedra', 'papel', 'tijera']
    seleccion_maquina = random.randint(0, 2)
    print('Piedra, papel o tijera...')
    seleccion_jugador = menu_juego()-1

    mostrar_resultados(opciones, seleccion_maquina, seleccion_jugador)
    save_data(seleccion_jugador, seleccion_maquina)


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
