# Calcula as raízes de uma equação do segundo grau - Bhaskara
# Introdução à Ciência da Computação - Coursera - Semana 3 - Adicional
# Exercício 2 - Bruno Rodrigues - 27/12/22

valor_de_a = int(input("Digite o valor de a: "))
valor_de_b = int(input("Digite o valor de b: "))
valor_de_c = int(input("Digite o valor de c: "))

delta = (valor_de_b ** 2) - (4 * valor_de_a * valor_de_c)

import math

raiz1 = (-valor_de_b + math.sqrt(abs(delta))) / 2 * valor_de_a
raiz2 = (-valor_de_b - math.sqrt(abs(delta))) / 2 * valor_de_a

if delta < 0:
    print("esta equação não possui raízes reais")
    
elif delta == 0:
    print(f"a raiz dupla desta equação é {raiz1}")
    
else:
    if raiz1 < raiz2:
        print(f"as raízes da equação são {raiz1} e {raiz2}")
    else:
        print(f"as raízes da equação são {raiz2} e {raiz1}")
