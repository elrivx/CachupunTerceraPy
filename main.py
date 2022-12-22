# Importaciones

import random

# Variables

enemyScore = 0
playerScore = 0
tieScore = 0
possibleHands = ["Piedra", "Papel", "Tijera"]

# Funciones

def checkWinner(playerHand, enemyHand):
    if (playerHand == "Piedra" and enemyHand == "Papel"):
        print("Perdiste :( ")
        return "Rival"
    elif (playerHand == "Piedra" and enemyHand == "Tijera"):
        print("Ganaste :)")
        return "Jugador"
    elif (playerHand == "Tijera" and enemyHand == "Papel"):
        print("Ganaste :)")
        return "Jugador"
    elif (playerHand == "Tijera" and enemyHand == "Piedra"):
        print("Perdiste :(")
        return "Rival"
    elif (playerHand == "Papel" and enemyHand == "Piedra"):
        print("Ganaste :)")
        return "Jugador"
    elif (playerHand == "Papel" and enemyHand == "Tijera"):
        print("Perdiste :(")
        return "Rival"
    else:
        print("Empataron. ¡Vamos otra vez!")
        return "Empate"

# Comenzamos

print("¡A jugar Cachipún Tercera!")
print("====================")

# Lógica del juego (Como diríamos en Chile, Cachipún Tercera)

while(playerScore != 3 and enemyScore != 3):
    # Pedimos al jugador que nos diga su opción
    while True:
        playerHand = input("\nEscoge tu opción entre Piedra, Papel o Tijera: ")
        # Validando opción Jugador
        if (playerHand == "Piedra" or playerHand == "Papel" or playerHand == "Tijera"):
            break
        else:
            print("Esa opción no existe aquí. Intenta otra vez.")
    # El rival ahora hará su jugada
    enemyHand = random.choice(possibleHands)
    # Mostramos los resultados
    print("Sacaste: ", playerHand)
    print("El rival sacó: ", enemyHand)
    result = checkWinner(playerHand, enemyHand)
    if (result == "Jugador"):
        playerScore += 1
    elif (result == "Rival"):
        enemyScore += 1
    else:
        tieScore += 1
    print("Ganadas: ", playerScore, " Perdidas: ", enemyScore, " Empates: ", tieScore)
print("Game Over!")

