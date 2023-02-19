# Calcula a distância entre dois pontos no plano cartesiano
# Introdução à Ciência da Computação - Coursera - Semana 3 - Adicional
# Exercício 1 - Bruno Rodrigues - 27/12/22

import math
coord_x_inicial = int(input("Digite a coordenada x inicial: "))
coord_y_inicial = int(input("Digite a coordenada y inicial: "))
coord_x_final = int(input("Digite a coordenada x final: "))
coord_y_final = int(input("Digite a coordenada y final: "))

distancia = math.sqrt(((coord_x_inicial - coord_x_final) ** 2) + ((coord_y_inicial - coord_y_final) ** 2))

if distancia >= 10:
    print("longe")

else:
    print("perto")
