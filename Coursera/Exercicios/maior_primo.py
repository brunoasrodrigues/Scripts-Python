# Recebe um número inteiro e devolve o maior número primo.
# Introdução à Ciência da Computação - Coursera - Semana 5
# Exercício 2 - Bruno Rodrigues - 17/02/23

def maior_primo(n):
    k = n


    while k > 1 and éPrimo(k) == False:
        k = k - 1
    return k


def éPrimo(k):


    primo = True
    div = 2

    while k > div:

        if k % div == 0:
         primo = False
        div = div + 1

    return primo

n = int(input())
print(maior_primo(n))
