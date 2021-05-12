"""
Durante el curso ya has escrito un programa, similar al que hay en este
fichero, en el que el jugador tiene que adivinar el número en el que está
pensando el programa. Ahora vamos a hacerlo al revés, el programa tiene que
adivinar el número en el que estás pensando tú.

Para ello, completa estas tres tareas:
1. En la linea 37 hay una llamada a la función "adivinar", que no existe
   todavía. Crea esta función y haz que devuelva el siguiente intento.

2. Modifica la función "nueva_partida" para que, al final de la partida,
   muestre el total de intentos que ha usado el programa para acertar el
   número.

3. Modifica la función "nueva partida" para que, al final de la partida,
   muestre el número en el que el jugador estaba pensando.
"""

import math
from random import randint




def nueva_partida():
    print("Piensa un número entre 1 y 100, ¡lo adivinaré en 10 intentos o menos!\n")
    print("Pulsa ENTER para continuar, cuando lo hayas pensado")
    input()

    estado = ""
    intentos = []
    mayor_que = 0
    menor_que = 101
    
    def adivinar(intentos=[], estado=estado, mayor_que=mayor_que, menor_que=menor_que):
        if estado == "":
            numero = round((mayor_que+menor_que)/2)
        
        elif estado in ["1","2"]:
            numero = round((mayor_que+menor_que)/2)
    
        return (numero)

    while estado != "3":
        if len(intentos) > 10:
            print("No he conseguido adivinar tu número :(")
            exit()

        intento = adivinar(intentos, estado, mayor_que, menor_que)
        intentos.append(intento)

        print(f"¿Estás pensando en el número {intento}?")

        estado = ""
        while estado not in ["1", "2", "3"]:
            print("Escribe una opción y luego pulsa ENTER: 1 si tu número " +
                  "es menor, 2 si tu número es mayor, 3 si he acertado:")
            estado = input()

        if estado == "1":
            menor_que = intento
        elif estado == "2":
            mayor_que = intento

        print()

    total_intentos = len(intentos)
    numero_ganador = intento

    print(f"¡He acertado!, tu número era el {numero_ganador}.")
    print(f"Lo he conseguido en {total_intentos} intentos.")

while True:
    nueva_partida()
    print()
    print("Pulsa ENTER para jugar otra vez o CTRL+C para salir")
    input()

