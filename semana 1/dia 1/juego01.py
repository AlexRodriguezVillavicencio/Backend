from random import choice
#JUEGO DE YANQUEPO
#DEFINIR VARIABLES DE ENTRADA Y SALIDA
opciones= ["piedra", "papel", "tijera"]
jugador = input("ingresa tu jugada:")
computadora = choice(opciones + opciones)
print("la computadora jugo:" + computadora)
ganador = ""
#LOGICA DE LA SOLUCIÓN
if jugador == "piedra":
    if computadora == "piedra":
        ganador = "empate"
    elif computadora == "papel":
        ganador = "computador"
    elif computadora == "tijera":
        ganador = "jugador"
if jugador == "tijera":
    if computadora == "piedra":
        ganador = "computadora"
    elif computadora == "papel":
        ganador = "jugador"
    elif computadora == "tijera":
        ganador = "empate"
if jugador == "papel":
    if computadora == "piedra":
        ganador = "jugador"
    elif computadora == "papel":
        ganador = "empate"
    elif computadora == "tijera":
        ganador = "computadora"

#MUESTRO RESULTADOS
print("El ganador es: " + ganador)

        