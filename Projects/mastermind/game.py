import random

COLORS = ["R", "W", "B", "Y", "G", "O"]
TRIES_LENGTH = 10
CODE_LENGTH = 4
tries = 0


def generade_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    print(code)
    return code


def guess_code():
    while True:
        guess = input("Pon 4 colores R W B Y G O: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"Deben se solo {CODE_LENGTH} colores")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"No es un color valido {color}")
                break
        else:
            break

    return guess


def check_code(guess, code):
    condicion = True
    correctas = 0
    while condicion:
        if code == guess:
            print("Son correctos adivinaste")
            break
        for cod in code:
            if cod == guess[0]:
                correctas = correctas + 1
                continue
            if cod == guess[1]:
                correctas = correctas + 1
                continue
            if cod == guess[2]:
                correctas = correctas + 1
                continue
            if cod == guess[3]:
                correctas = correctas + 1
                continue
        print(f"Tienes {correctas} acertadas")

        condicion = False


def game():
    print("Bienvenido al juego de MASTERMIND!!!")
    print("Se ha generado tu codigo de colores secreto trata de averiguarlo muajajaja ")
    print("Para lograrlo deberas escoger cuatro colores de estas opciones: ")
    print("\nR W B Y G O")
    print("Escogelos y comienza tu tortura ==>")

    code = generade_code()

    for jugadas in range(1, TRIES_LENGTH + 1):
        jugada = guess_code()
        if jugada != code:
            check_code(jugada, code)
        else:
            print("Ganaste cabron!!!")
            break


game()
