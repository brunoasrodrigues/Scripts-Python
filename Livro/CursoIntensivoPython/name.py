# name = "bruno rodrigues"
# print(name.title()) # imprime o texto com as primeiras letras em caixa alta
# print(name.upper()) # imprime todo o texto em caixa alta
#  print(name.lower()) # imprime todo o texto em caixa baixa

first_name = "marta"
last_name = "rodrigues"
full_name = first_name + " " + last_name
print(full_name)
print("Hi, " + full_name.title() + "!")
print("\tPython")  # \t acrescenta tabulação no texto
print("Languages:\nPython\n\tC\n\t\tJava")  # \n quebra de linha

favorite_language = "  Python  "
print(favorite_language.rstrip()+"!")
print(favorite_language.lstrip()+"!")
print(favorite_language.strip()+"!")
favorite_language = favorite_language.strip()
print(favorite_language)

teste = "   Bruno   "
print(teste+"!")
print(teste.strip()+"!")  # remove espaços em branco a direita e a esquerda do texto
print(f"Seja bem vindo {teste.strip()}!")
