#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de uso da função calcular_expressoes_e_gravar_resultados

Este script demonstra como usar a função para processar expressões matemáticas
de um arquivo de entrada e gravar os resultados em um arquivo de saída.

A função agora possui logs detalhados que mostram cada etapa do processamento,
tornando mais fácil entender o que está acontecendo durante a execução.
"""

from python import calcular_expressoes_e_gravar_resultados

# Definindo os nomes dos arquivos
arquivo_entrada = "expressoes_entrada.txt"
arquivo_saida = "resultados_saida_python.txt"

# Executando a função
# A função já possui logs detalhados internos, então não precisamos
# adicionar mais prints aqui
calcular_expressoes_e_gravar_resultados(arquivo_entrada, arquivo_saida)

