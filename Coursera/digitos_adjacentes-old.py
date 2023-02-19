# Verifica se um número dado possui números adjacentes iguais.
# Introdução à Ciência da Computação - Coursera - Semana 4 - Opcional
# Exercício 2 - Bruno Rodrigues - 03/01/23


num_Inicial = int(input("Digite um número inteiro: "))
divisor = int(10 ** (len(str(num_Inicial)) - 1)) 
soma1 = 0
contador = 0

while contador <= len(str(num_Inicial)):
    divisao1 = num_Inicial // divisor
    resto = num_Inicial % divisor
    divisor = divisor / 10
    divisao2 = resto // divisor
    if divisao1 == divisao2:
        print("sim")        
    else:
        num_Inicial = resto
        contador = contador + 1

    if contador == len(str(num_Inicial)):
        print("não")
