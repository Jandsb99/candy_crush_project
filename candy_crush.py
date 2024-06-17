# Llibreries
import random
from screen_manager import ScreenManager

# Inici del codi

print("Introdueix el valor de la matriu (mínim 1, màxim 15): ")
valor_matriu = input()

# Comprovació de la varibale de la matriu

try:
    valor_matriu = int(valor_matriu)
except:
    print("Error")

if valor_matriu > 15:
    print("Error")

# Creació de la matriu

matriu = []
linia = []

for i in range(valor_matriu):
    for i in range(valor_matriu):
        linia.append(random.randint(1,valor_matriu))
    matriu.append(linia)
    linia = []

for l in matriu:
    print(l)


# Creació del bucle de joc

matriu_joc = ScreenManager(matriu)

while True:
    print("Introdueix les coordenades que vols intercanviar:  (introdueix valor i prem enter)")
    x0 = int(input())
    if x0 == -1:
        break
    y0 = int(input())
    x1 = int(input())
    y1 = int(input())

    matriu_joc.rearrange(x0, y0, x1, y1)
    matriu_joc.clear(x0, y0)
    matriu_joc.clear(x1, y1)

    print(matriu_joc.matriu)