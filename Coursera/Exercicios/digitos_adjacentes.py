# Verifica se um número dado possui números adjacentes iguais.
# Introdução à Ciência da Computação - Coursera - Semana 4 - Opcional
# Exercício 2 - Bruno Rodrigues - 06/01/23

num_Ini = str(input("Digite um número inteiro: "))
comp_Digito = len(num_Ini)
contador = 0

while contador < comp_Digito:
    comp1 = contador
    comp2 = contador + 1
    valor1 = num_Ini[comp1:comp2]
    valor2 = num_Ini[(comp1+1):(comp2+1)]
    if valor1 == valor2:
        print("sim")
        contador = comp_Digito + 1
    else:
        contador = contador + 1

    if contador == comp_Digito:
        print("não")
