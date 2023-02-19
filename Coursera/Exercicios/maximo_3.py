# Recebe 3 números inteiros e retorna o maior.
# Introdução à Ciência da Computação - Coursera - Semana 5 - Adicional
# Exercício 2 - Bruno Rodrigues - 17/02/23

def maximo(val1, val2, val3):
    max = val1
    
    if val2 > max and val2 > val3:
        max = val2
    elif val3 > max:
        max = val3
    
    return max


val1=int(input())
val2=int(input())
val3=int(input())

print(maximo(val1, val2, val3))
