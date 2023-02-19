# Imprime os n primeiros números ímpares de um número dado.
# Introdução à Ciência da Computação - Coursera - Semana 4
# Exercício 2 - Bruno Rodrigues - 02/01/23


num_Inicial = int(input("Digite o valor de n: "))
valor_Inicial = 0
contador = 0

while contador < num_Inicial:
    valor_Inicial = valor_Inicial + 1
    if valor_Inicial % 2 != 0:
        print(valor_Inicial)
        contador = contador + 1
