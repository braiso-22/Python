def calcular_cambio(importe_pagado, importe_a_pagar):
    cambio = importe_pagado - importe_a_pagar
    return cambio


def calcular_billetes(cambio):
    billetes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    for billete in billetes:
        numero_billetes = cambio // billete
        if numero_billetes > 0:
            print(numero_billetes, "billetes de", billete)
            cambio = cambio % billete
        pass
    return cambio


def mostrar_respuesta(importe_a_pagar, importe_pagado):
    if importe_a_pagar > importe_pagado:
        print("El importe pagado es menor que el importe a pagar")
        return

    cambio = calcular_cambio(importe_pagado, importe_a_pagar)
    print("El cambio es: ", cambio)
    print("Billetes devueltos: ")
    calcular_billetes(cambio)

    pass


def main():
    importe_a_pagar = float(input("Introduce el importe a pagar: "))
    importe_pagado = float(input("Introduce el importe pagado: "))

    mostrar_respuesta(importe_a_pagar, importe_pagado)
    pass


if __name__ == '__main__':
    main()
pass
