# Exercício 2: Busca de Substring e Inversão
# Objetivo: Dada uma frase predefinida, usar o operador in para verificar se uma determinada palavra está presente. 
# Em seguida, inverter a string usando fatiamento (slicing).

# Programa Python (Solução 2):

frase = "Estou aprendendo Python na INBEC" # Variável String [1]
palavra_busca = "Python"

# Verificando se a substring está presente usando o operador 'in' [7, 8]
resultado_busca = palavra_busca in frase 

# Invertendo a string usando o fatiamento [::-1] [12]
frase_invertida = frase[::-1] 

# Imprimindo resultados usando f-string [5, 6]
print(f"Frase original: {frase}")
print(f"A palavra '{palavra_busca}' está presente na frase? {resultado_busca}")
print(f"Frase invertida: {frase_invertida}")

# Conceitos Utilizados: Operador in para verificar a presença de uma substring, Invertendo uma string usando [::-1]
