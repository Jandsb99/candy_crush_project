# Llibreries
import random

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
        linia.append(random.randint(0,9))
    matriu.append(linia)
    linia = []

for l in matriu:
    print(l)


# Creació del bucle de joc

# Condició d'aturada del bucle --> si el jugador dona un -1 s'atura el bucle
# Estat de la matriu, s'ha de poder fer swap (el jugador ha de poder donar dues coordenades i canviar-les

# Primer crear matriu, després canviar posicions (SWAP), després comprovar posicions i si son iguals eliminar (CLEAR)
