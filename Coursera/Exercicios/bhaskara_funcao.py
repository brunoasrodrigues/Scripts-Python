"""
Calcula as raízes de uma equação do segundo grau - Bhaskara
Introdução à Ciência da Computação - Coursera - Semana 3 - Adicional
Exercício 2 - Bruno Rodrigues - 27/12/22
"""

import math


def main():
    val_a = int(input("Digite o valor de a: "))
    val_b = int(input("Digite o valor de b: "))
    val_c = int(input("Digite o valor de c: "))
    raizes(val_a, val_b, val_c)


def delta(val_a, val_b, val_c):
    return val_b ** 2 - 4 * val_a * val_c


def raizes(val_a, val_b, val_c):
    delta2 = delta(val_a, val_b, val_c)
    raiz1 = (-val_b + math.sqrt(abs(delta2))) / 2 * val_a
    raiz2 = (-val_b - math.sqrt(abs(delta2))) / 2 * val_a

    if delta2 < 0:
        print("esta equação não possui raízes reais")

    elif delta2 == 0:
        print(f"a raiz dupla desta equação é {raiz1}")

    else:
        if raiz1 < raiz2:
            print(f"as raízes da equação são {raiz1} e {raiz2}")
        else:
            print(f"as raízes da equação são {raiz2} e {raiz1}")

# teste de Git.
