colors = ["R", "B", "Y", "G", "O"]
colores_adivinado = []

for i in range(4):
    color = input("Pon tu color: ")
    colores_adivinado.append(color)


for color in colores_adivinado:
    if color in colors:
        print(f"Este color {color} si esta en la lista")
