from random import choice
#JUEGO DE YANQUEPO
print('***************************************************************')
print('***************************************************************')
print('*************!BIENVENIDO AL JUEGO DE YANQUENPO!****************')
print('***************************************************************')
print('************elige entre piedra, papel o tijera*****************')
print('***************************************************************')
#DEFINE ENTRADAS Y SALIDAS DE VARIABLES
options= ["piedra", "papel", "tijera"]
player = input("Ingresa tu jugada:")
computer = choice(options + options + options)
winner = ""
play= "si"
#LOGICA DE LA SOLUCIÓN
def jugada ():
    for i in range(len(options)):
        a = options[i]
        if (player == a):
            if (computer == player):
                print("han quedado empate")
            elif (computer != player):
                if(player == "piedra" and computer == "tijera"):
                    print("ganaste!")
                if(player == "piedra" and computer == "papel"):
                    print("perdiste...suerte para la proxima")
                if(player == "papel" and computer == "tijera"):
                    print("perdiste...suerte para la proxima")
                if(player == "papel" and computer == "piedra"):
                    print("ganaste!")
                if(player == "tijera" and computer == "papel"):
                    print("ganaste!")
                if(player == "tijera" and computer == "piedra"):
                    print("perdiste...suerte para la proxima")

# #MUESTRO RESULTADOS
if(player == "papel" or player =="tijera" or player == "piedra"):
    print("la maquina jugó: " + computer)
    jugada()
else:
    print("ingresa un movimiento valido")
