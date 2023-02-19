# Recebe 2 números inteiros e retorna o maior.
# Introdução à Ciência da Computação - Coursera - Semana 5
# Exercício 1 - Bruno Rodrigues - 12/02/23

def maximo(val1, val2):
    max = val1
    
    if val2 > max:
        max = val2
    
    return max

val1=int(input())
val2=int(input())

print(maximo(val1, val2))
