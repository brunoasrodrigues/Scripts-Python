# Verifica se um número inteiro é par ou ímpar
# Introdução à Ciência da Computação - Coursera - Semana 3 - Lista 2
# Exercício 1 - Bruno Rodrigues - 27/12/22

numero_inicial = int(input("Digite um número inteiro: "))
numero_resto = numero_inicial % 2
if (numero_resto == 0):
    print("par")
else:
    print("ímpar")
