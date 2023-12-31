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
    return code


def guess_code():
    guess = []
    for i in range(CODE_LENGTH):
        colores = input("Pon cuatro colores pueden ser R W B Y G O:  ")
        guess.append(colores)
    return guess


code1 = ["R", "B", "Y", "G"]
guess1 = ["R", "B", "Y", "5"]


def check_code(guess, code):
    condicion = True
    while condicion:
        if code == guess:
            print("Son correctos adivinaste")
            break

        for color in guess:
            if color in code:
                print(f"Este color {color} si esta en la lista")
            guess_code()

        condicion = False


def game():
    print("Bienvenido al juego de MASTERMIND!!!")
    print(" Se ha generado tu codigo de colores secreto trata de averiguarlo ")
    codigo = generade_code()
    adivina = guess_code()
    check_code(codigo, adivina)


game()
