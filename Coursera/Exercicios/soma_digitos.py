# Recebe 2 números inteiros e retorna o maior.
# Introdução à Ciência da Computação - Coursera - Semana 5
# Exercício 1 - Bruno Rodrigues - 02/01/23


num_Inicial = int(input("Digite um número inteiro: "))
casas_Decimais = len(str(num_Inicial))
divisor = 10 ** (casas_Decimais - 1)
soma1 = 0
contador = 0

divisao1 = num_Inicial // divisor

while contador < casas_Decimais:
    resto = num_Inicial % divisor
    divisor = divisor / 10
    divisao2 = resto // divisor
    soma1 = soma1 + divisao2
    contador = contador + 1
    
print(int(divisao1) + int(soma1))
