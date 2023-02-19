# Recebe um caractere e verifica se é vogal(True) ou consoante(False).
# Introdução à Ciência da Computação - Coursera - Semana 5
# Exercício 1 - Bruno Rodrigues - 17/02/23

def vogal(caractere):
    caractere = caractere.lower()
    if caractere in "aeiou":
        return True
    else:
        return False


letra = str(input())
print(vogal(letra))
