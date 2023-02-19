

decrescente = True
anterior = int(input("Digite o primeiro valor: "))
valor = 1

while valor != 0 and decrescente:
    valor = int(input("Digite o próximo valor: "))
    if valor > anterior:
        decrescente = False
    anterior = valor
    
if decrescente:
    print("A sequência está em oredem decrescente")
else:
    print("A sequência não está em ordem decrescente")
