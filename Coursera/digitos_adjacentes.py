# Verifica se um número dado possui números adjacentes iguais.
# Introdução à Ciência da Computação - Coursera - Semana 4 - Opcional
# Exercício 2 - Bruno Rodrigues - 04/01/23


num_Inicial = int(input("Digite um número inteiro: "))
comp_Digito = len(str(num_Inicial))
divisor = 10 ** (comp_Digito - 1)
contador = 0

while contador < comp_Digito:
    divisao1 = num_Inicial // divisor
    resto = num_Inicial % divisor
    divisor = divisor / 10
    divisao2 = resto // divisor
    if divisao1 == divisao2:
        print("sim")
        contador = comp_Digito + 1
    else:
        num_Inicial = resto
        contador = contador + 1

    if contador == comp_Digito:
        print("não")
