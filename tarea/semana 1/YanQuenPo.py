from random import choice
#JUEGO DE YANQUEPO
print('***************************************************************')
print('***************************************************************')
print('***************!WELCOME TO THE YANQUENPO GAME!*****************')
print('***************************************************************')
print('************choose between stone, paper or scissor*************')
print('***************************************************************')
#DEFINE INPUT AND OUTPUT VARIABLES
options= ["stone", "paper", "scissor"]
player = input("input you game:")
computer = choice(options + options + options)
print("the computer played:" + computer)
winner = ""
#LOGICA DE LA SOLUCIÓN
if player == "stone":
    if computer == "stone":
        winner = "empate"
    elif computer == "paper":
        winner = "computer"
    elif computer == "scissor":
        winner = "player"
if player == "scissor":
    if computer == "stone":
        winner = "computer"
    elif computer == "paper":
        winner = "player"
    elif computer == "scissor":
        winner = "empate"
if player == "paper":
    if computer == "stone":
        winner = "player"
    elif computer == "paper":
        winner = "empate"
    elif computer == "scissor":
        winner = "computer"

#MUESTRO RESULTADOS
print("El winner es: " + winner)

        