# Calcula o fatorial de um número dado.
# Introdução à Ciência da Computação - Coursera - Semana 4
# Exercício 1 - Bruno Rodrigues - 02/01/23


num_inicial = int(input("Digite o valor de n: "))
antecessor = num_inicial - 1

if(num_inicial == 0 or num_inicial == 1):
    print("1")

else:

    fator = num_inicial * (num_inicial - 1)

    while antecessor > 1:
    
        antecessor = antecessor - 1
        fator = fator * antecessor

    print(fator)
