# Exercício 3: Manipulação de Caixa (Case) e Substrings
# Objetivo: Receber uma frase do usuário e aplicar os métodos .upper() para exibir a frase em maiúsculas 
# e .lower() para exibir em minúsculas. Em seguida, exibir a primeira e a última letra da frase usando indexação.

# Programa Python (Solução 3):

# Variável armazena a sequência de caracteres [1]
frase_original = input("Digite uma frase: ")

# Convertendo todos os caracteres para maiúsculas [10]
frase_upper = frase_original.upper()

# Convertendo todos os caracteres para minúsculas [10, 11]
frase_lower = frase_original.lower()

# Retornando o primeiro caractere [8]
primeira_letra = frase_original[0]

# Retornando o último caractere usando indexação negativa [8]
ultima_letra = frase_original[-1]

# Imprimindo os resultados [2]
print(f"Frase em MAIÚSCULAS: {frase_upper}")
print(f"Frase em minúsculas: {frase_lower}")
print(f"A primeira letra da frase é: {primeira_letra}")
print(f"A última letra da frase é: {ultima_letra}")

# Conceitos Utilizados: Métodos .upper() e .lower(), Retornando caracteres da string usando indexação