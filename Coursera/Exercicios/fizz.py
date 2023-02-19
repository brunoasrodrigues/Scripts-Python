# Verifica se um número inteiro é divisível por 3
# Introdução à Ciência da Computação - Coursera - Semana 3 - Lista 2
# Exercício 2 - Bruno Rodrigues - 27/12/22

numero_inicial = int(input("Digite um número inteiro: "))
numero_resto = numero_inicial % 3
if (numero_resto == 0):
    print("Fizz")
else:
    print(numero_inicial)
