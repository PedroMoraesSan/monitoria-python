# Exercício 5: Código de César
# Programa simples para codificar e descodificar usando o Código de César (3 posições)

def codificar_cesar(texto):
    """Codifica um texto usando o Código de César com deslocamento de 3 posições"""
    texto_codificado = ""
    
    for caractere in texto:
        if caractere.isalpha():  # Se for uma letra
            if caractere.isupper():
                # Para maiúsculas
                novo_codigo = ord(caractere) + 3
                if novo_codigo > ord('Z'):
                    novo_codigo -= 26  # Volta ao início do alfabeto
                texto_codificado += chr(novo_codigo)
            else:
                # Para minúsculas
                novo_codigo = ord(caractere) + 3
                if novo_codigo > ord('z'):
                    novo_codigo -= 26  # Volta ao início do alfabeto
                texto_codificado += chr(novo_codigo)
        else:
            # Mantém caracteres que não são letras (espaços, pontuação)
            texto_codificado += caractere
    
    return texto_codificado

def descodificar_cesar(texto_codificado):
    """Descodifica um texto usando o Código de César com deslocamento de 3 posições"""
    texto_descodificado = ""
    
    for caractere in texto_codificado:
        if caractere.isalpha():  # Se for uma letra
            if caractere.isupper():
                # Para maiúsculas
                novo_codigo = ord(caractere) - 3
                if novo_codigo < ord('A'):
                    novo_codigo += 26  # Volta ao final do alfabeto
                texto_descodificado += chr(novo_codigo)
            else:
                # Para minúsculas
                novo_codigo = ord(caractere) - 3
                if novo_codigo < ord('a'):
                    novo_codigo += 26  # Volta ao final do alfabeto
                texto_descodificado += chr(novo_codigo)
        else:
            # Mantém caracteres que não são letras
            texto_descodificado += caractere
    
    return texto_descodificado

# Exemplo de uso
print("=== CÓDIGO DE CÉSAR ===")
print("Deslocamento: 3 posições")
print()

# Exemplo fornecido no exercício
texto_original = "a ligeira raposa marrom saltou sobre o cachorro cansado"
print(f"String original: {texto_original}")

# Codificar
texto_codificado = codificar_cesar(texto_original.upper())
print(f"String codificada: {texto_codificado}")

print()

# Teste com entrada do usuário
texto_usuario = input("Digite um texto para codificar: ")
texto_codificado_usuario = codificar_cesar(texto_usuario)
print(f"Texto codificado: {texto_codificado_usuario}")

# Descodificar
texto_descodificado = descodificar_cesar(texto_codificado_usuario)
print(f"Texto descodificado: {texto_descodificado}")