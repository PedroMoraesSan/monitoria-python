# Exercício 1: Contagem e Substituição
# Objetivo: Dada uma frase, usar o método .count() para determinar quantas vezes uma palavra específica aparece. 
# Em seguida, usar o método .replace() para substituir todas as ocorrências dessa palavra por outra.

# Programa Python (Solução 1):

frase = "Python é legal, e aprender Python é fundamental para Python" # Variável String [1]
palavra_antiga = "Python"
palavra_nova = "Linguagem"

# Contando o número de ocorrências da palavra [11]
contagem = frase.count(palavra_antiga)

# Substituindo todas as ocorrências de 'Python' por 'Linguagem' [13]
frase_modificada = frase.replace(palavra_antiga, palavra_nova)

# Imprimindo os resultados [2]
print(f"Frase original: {frase}")
print(f"A palavra '{palavra_antiga}' aparece {contagem} vezes na frase.")
print(f"Frase com substituição (usando .replace()): {frase_modificada}")

# Conceitos Utilizados: Método .count() para contar substrings, Método .replace() para substituir caracteres
