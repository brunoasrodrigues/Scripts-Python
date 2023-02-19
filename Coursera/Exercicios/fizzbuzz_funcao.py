# Lê um inteiro e devolve Fizz' se o número for divisível por 3 e não for divisível por 5;
# 'Buzz' se o número for divisível por 5 e não for divisível por 3;
# 'FizzBuzz' se o número for divisível por 3 e por 5;
# Introdução à Ciência da Computação - Coursera - Semana 5 - Adicional
# Exercício 1 - Bruno Rodrigues - 17/02/23

def fizzbuzz(valor):
    if valor % 3 == 0 and valor % 5 == 0:
        resposta = "FizzBuzz"
    else:
        if valor % 3 == 0:
            resposta = "Fizz"
        elif valor % 5 == 0:
            resposta = "Buzz"
        else:
            resposta = valor
    return (resposta)


valor = int(input())
print(fizzbuzz(valor))
