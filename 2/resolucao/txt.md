# Resoluções dos Exercícios de Manipulação de Strings

## Exercício 1: Contagem e Substituição
**Objetivo:** Demonstrar o uso dos métodos `.count()` e `.replace()` para manipulação de strings.

**Conceitos Utilizados:**
- **Método `.count()`**: Conta o número de ocorrências de uma substring em uma string
- **Método `.replace()`**: Substitui todas as ocorrências de uma substring por outra
- **Variáveis String**: Armazenamento e manipulação de sequências de caracteres
- **F-strings**: Formatação moderna de strings para exibição de resultados

**Exemplo de Saída:**
```
Frase original: Python é legal, e aprender Python é fundamental para Python
A palavra 'Python' aparece 3 vezes na frase.
Frase com substituição (usando .replace()): Linguagem é legal, e aprender Linguagem é fundamental para Linguagem
```

## Exercício 2: Busca de Substring e Inversão
**Objetivo:** Demonstrar o uso do operador `in` para busca e fatiamento para inversão de strings.

**Conceitos Utilizados:**
- **Operador `in`**: Verifica se uma substring está presente em uma string
- **Fatiamento `[::-1]`**: Inverte uma string usando slicing com passo negativo
- **Comparação de strings**: Verificação de presença de substrings
- **F-strings**: Formatação de saída com interpolação de variáveis

**Exemplo de Saída:**
```
Frase original: Estou aprendendo Python na INBEC
A palavra 'Python' está presente na frase? True
Frase invertida: CEBIN an nohtyP odnepma uotsE
```

## Exercício 3: Manipulação de Caixa (Case) e Substrings
**Objetivo:** Demonstrar métodos de conversão de caixa e indexação de strings.

**Conceitos Utilizados:**
- **Método `.upper()`**: Converte todos os caracteres para maiúsculas
- **Método `.lower()`**: Converte todos os caracteres para minúsculas
- **Indexação `[0]`**: Acesso ao primeiro caractere da string
- **Indexação `[-1]`**: Acesso ao último caractere usando índice negativo
- **Função `input()`**: Entrada de dados do usuário

**Exemplo de Saída:**
```
Digite uma frase: Olá Mundo
Frase em MAIÚSCULAS: OLÁ MUNDO
Frase em minúsculas: olá mundo
A primeira letra da frase é: O
A última letra da frase é: o
```

## Exercício 4: Menu de Manipulação de Strings
**Objetivo:** Criar um programa interativo com menu para diversas operações de manipulação de strings.

**Funcionalidades Implementadas:**
- **(a) Ler string S1**: Validação de tamanho máximo (20 caracteres)
- **(b) Imprimir tamanho**: Uso da função `len()`
- **(c) Comparar strings**: Comparação lexicográfica com operadores relacionais
- **(d) Concatenar strings**: Operador `+` para concatenação
- **(e) Inverter string**: Fatiamento `[::-1]`
- **(f) Contar caractere**: Método `.count()` para caracteres específicos
- **(g) Substituir caractere**: Método `.replace()` com limite de ocorrências
- **(h) Verificar substring**: Operador `in` para verificação
- **(i) Extrair substring**: Fatiamento com posição e tamanho específicos

**Conceitos Avançados:**
- **Funções**: Modularização do código em funções específicas
- **Tratamento de erros**: Validação de entrada e tratamento de exceções
- **Programação interativa**: Loop principal com menu de opções
- **Documentação**: Docstrings para documentar as funções

## Exercício 5: Código de César
**Objetivo:** Implementar um algoritmo de criptografia clássica com codificação e descodificação.

**Algoritmo do Código de César:**
- Cada letra é substituída por outra que está 3 posições à frente no alfabeto
- Caracteres não-alfabéticos (espaços, pontuação) são mantidos inalterados
- O alfabeto "volta ao início" após a letra Z (A, B, C, ..., Z, A, B, C...)

**Conceitos Implementados:**
- **Função `ord()`**: Converte caractere para código ASCII
- **Função `chr()`**: Converte código ASCII para caractere
- **Operação módulo `%`**: Para fazer o alfabeto "circular"
- **Método `.isalpha()`**: Verifica se o caractere é uma letra
- **Métodos `.isupper()` e `.islower()`**: Verificam se é maiúscula ou minúscula

**Exemplo de Funcionamento:**
```
String original: a ligeira raposa marrom saltou sobre o cachorro cansado
String codificada: D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR FDQVDGR
```

**Funcionalidades do Programa:**
- Menu interativo para codificar/descodificar
- Demonstração automática do exemplo fornecido
- Teste de verificação automática
- Tratamento de maiúsculas e minúsculas
- Preservação de caracteres especiais

## Conceitos Gerais de Strings em Python

### Métodos Principais Utilizados:
- `.count(substring)`: Conta ocorrências
- `.replace(old, new, count)`: Substitui substrings
- `.upper()`: Converte para maiúsculas
- `.lower()`: Converte para minúsculas
- `.strip()`: Remove espaços em branco das extremidades

### Operações de Indexação:
- `string[0]`: Primeiro caractere
- `string[-1]`: Último caractere
- `string[start:end]`: Fatiamento
- `string[::-1]`: Inversão

### Operadores Especiais:
- `in`: Verifica presença de substring
- `+`: Concatenação de strings
- `==`, `>`, `<`: Comparação lexicográfica

### Funções Built-in:
- `len(string)`: Retorna o tamanho
- `input()`: Entrada do usuário
- `print()`: Saída formatada
- `ord(char)`: Código ASCII
- `chr(code)`: Caractere do código ASCII