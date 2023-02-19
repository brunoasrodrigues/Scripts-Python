# Verifica se 3 números inteiros foram digitados em ordem crescente
# Introdução à Ciência da Computação - Coursera - Semana 3 - Lista 2
# Exercício 5 - Bruno Rodrigues - 27/12/22

numero_1 = int(input("Digite o primeiro número inteiro: "))
numero_2 = int(input("Digite o segundo número inteiro: "))
numero_3 = int(input("Digite o terceiro número inteiro: "))
if (numero_1 < numero_2 < numero_3):
    print("crescente")
else:
    print("não está em ordem crescente")
