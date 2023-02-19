# Verifica se um número inteiro é divisível por 5
# Introdução à Ciência da Computação - Coursera - Semana 3 - Lista 2
# Exercício 3 - Bruno Rodrigues - 27/12/22

numero_inicial = int(input("Digite um número inteiro: "))
numero_resto = numero_inicial % 5
if (numero_resto == 0):
    print("Buzz")
else:
    print(numero_inicial)
