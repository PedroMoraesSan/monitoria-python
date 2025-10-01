# Exercício 4: Menu de Manipulação de Strings
# Programa simples para demonstrar operações básicas com strings

# Ler uma string S1 (tamanho máximo 20 caracteres)
s1 = input("Digite uma string (máximo 20 caracteres): ")

# Imprimir o tamanho da string S1
print(f"Tamanho da string S1: {len(s1)}")

# Comparar a string S1 com uma nova string S2
s2 = input("Digite uma string S2 para comparação: ")
if s1 == s2:
    print("As strings são iguais")
elif s1 > s2:
    print("S1 é maior que S2")
else:
    print("S1 é menor que S2")

# Concatenar a string S1 com uma nova string S2
s2_concat = input("Digite uma string S2 para concatenação: ")
resultado = s1 + s2_concat
print(f"Resultado da concatenação: {resultado}")

# Imprimir a string S1 de forma reversa
print(f"String S1 invertida: {s1[::-1]}")

# Contar quantas vezes um dado caractere aparece na string S1
caractere = input("Digite um caractere para contar: ")
contagem = s1.count(caractere)
print(f"O caractere '{caractere}' aparece {contagem} vez(es) na string S1")

# Substituir a primeira ocorrência do caractere C1 da string S1 pelo caractere C2
c1 = input("Digite o caractere C1 a ser substituído: ")
c2 = input("Digite o caractere C2 substituto: ")
nova_string = s1.replace(c1, c2, 1)  # Substitui apenas a primeira ocorrência
print(f"String original: {s1}")
print(f"String modificada: {nova_string}")

# Verificar se uma string S2 é substring de S1
s2_substring = input("Digite uma string S2 para verificar se é substring: ")
if s2_substring in s1:
    print(f"'{s2_substring}' é substring de '{s1}'")
else:
    print(f"'{s2_substring}' NÃO é substring de '{s1}'")

# Retornar uma substring da string S1
posicao = int(input("Digite a posição inicial (índice): "))
tamanho = int(input("Digite o tamanho da substring: "))
substring = s1[posicao:posicao + tamanho]
print(f"Substring extraída: '{substring}'")