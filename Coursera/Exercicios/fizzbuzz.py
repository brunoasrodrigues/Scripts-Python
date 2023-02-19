# Verifica se um número inteiro é divisível por 3 e por 5
# Introdução à Ciência da Computação - Coursera - Semana 3 - Lista 2
# Exercício 4 - Bruno Rodrigues - 27/12/22

numero_inicial = int(input("Digite um número inteiro: "))
numero_resto3 = numero_inicial % 3
numero_resto5 = numero_inicial % 5
if (numero_resto3 == 0 and numero_resto5 == 0):
    print("FizzBuzz")
else:
    print(numero_inicial)
