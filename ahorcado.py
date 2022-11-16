# hacer el juego del ahorcado
import random


def obtener_palabras():
    '''
    palabras = ["hola", "adios", "perro", "gato", "ordenador", "python", "java", "c++", "c#", "javascript",
                "php", "html", "css", "mysql", "postgresql", "mongodb", "oracle", "microsoft", "apple", "linux"]
    '''
    
    with open("./files/palabras.csv", "r",encoding="utf-8") as f:
        palabras = f.read().splitlines()[0].split(";")
    
    return palabras


def quitar_tildes(frase):
    frase = frase.replace('á', 'a')
    frase = frase.replace('é', 'e')
    frase = frase.replace('í', 'i')
    frase = frase.replace('ó', 'o')
    frase = frase.replace('ú', 'u')
    return frase


def limpiar_palabra(palabra):
    palabra = palabra.lower()
    palabra = quitar_tildes(palabra)
    return palabra


def obtener_palabra_aleatoria():
    palabras = obtener_palabras()
    palabra = random.choice(palabras)
    palabra = limpiar_palabra(palabra)
    return palabra


def juego():
    intentos = 6

    intentos_ascii = [
        """
        +---+
        |   |
            |
            |
            |
            |
        =========""",
        """
        +---+
        |   |
        O   |
            |
            |
            |
        =========""",

        """
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========""",
        """
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========""",
        """
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========""",
        """
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========""",
        """
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        ========="""
    ]

    palabra = [i for i in obtener_palabra_aleatoria()]
    palabra_set = set(palabra)
    palabra_mostrar = ["_"] * len(palabra)
    print(intentos_ascii[::-1][intentos])
    while True:
        if intentos <= 0:
            print("Has perdido")
            print(f"La palabra era: {''.join(palabra)}")
            break

        if "_" not in palabra_mostrar:
            print("Has ganado")
            break

        print(f"Palabra: {' '.join(palabra_mostrar)}")
        letra = input("Introduce una letra: ")

        if letra in palabra_set:
            lista_indices = [i for i, letraI in enumerate(
                palabra) if letraI == letra]
            print("Correcto")
            for i in lista_indices:
                palabra_mostrar[i] = letra
        else:
            print("Incorrecto")
            intentos -= 1
            
        print(intentos_ascii[::-1][intentos])


def menu():
    return input("1. Jugar\n2. Salir\n")


def main():
    while True:
        opcion = menu()

        if opcion == '1':
            juego()
        elif opcion == '2':
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
