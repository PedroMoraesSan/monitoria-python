def calcular_expressoes_e_gravar_resultados(arquivo_entrada, arquivo_saida):
    print("=" * 60)
    print("🚀 INICIANDO PROCESSAMENTO DE EXPRESSÕES")
    print("=" * 60)
    print(f"📂 Arquivo de entrada: '{arquivo_entrada}'")
    print(f"📄 Arquivo de saída: '{arquivo_saida}'")
    print("-" * 60)
    
    resultados = []
    erros = []
    total_linhas = 0
    linhas_vazias = 0
    
    try:
        print(f"\n📖 Abrindo arquivo de entrada '{arquivo_entrada}'...")
        with open(arquivo_entrada, 'r') as f_entrada:
            print("✅ Arquivo aberto com sucesso!\n")
            print("🔍 Iniciando leitura e processamento das expressões...")
            print("-" * 60)
            
            for numero_linha, linha in enumerate(f_entrada, 1):
                expressao = linha.strip()  # Remove espaços em branco e quebras de linha
                
                if not expressao:  # Ignora linhas vazias
                    linhas_vazias += 1
                    print(f"⏭️  Linha {numero_linha}: [VAZIA] - Ignorando...")
                    continue
                
                total_linhas += 1
                print(f"\n📝 Linha {numero_linha}: Processando '{expressao}'...")
                
                try:
                    print(f"   ⚙️  Calculando expressão...")
                    resultado = eval(expressao)
                    print(f"   ✅ SUCESSO! Resultado: {resultado}")
                    resultados.append(f"{expressao} = {resultado}")
                    print(f"   💾 Resultado armazenado na lista")
                    
                except ZeroDivisionError as e:
                    print(f"   ❌ ERRO: Divisão por zero detectada!")
                    print(f"   📋 Tipo: ZeroDivisionError")
                    erro_msg = f"Erro na linha {numero_linha} ('{expressao}'): {e}"
                    erros.append(erro_msg)
                    print(f"   💾 Erro armazenado na lista")
                    
                except NameError as e:
                    print(f"   ❌ ERRO: Variável ou função não definida!")
                    print(f"   📋 Tipo: NameError")
                    erro_msg = f"Erro na linha {numero_linha} ('{expressao}'): {e}"
                    erros.append(erro_msg)
                    print(f"   💾 Erro armazenado na lista")
                    
                except TypeError as e:
                    print(f"   ❌ ERRO: Operação inválida entre tipos!")
                    print(f"   📋 Tipo: TypeError")
                    erro_msg = f"Erro na linha {numero_linha} ('{expressao}'): {e}"
                    erros.append(erro_msg)
                    print(f"   💾 Erro armazenado na lista")
                    
                except SyntaxError as e:
                    print(f"   ❌ ERRO: Sintaxe inválida na expressão!")
                    print(f"   📋 Tipo: SyntaxError")
                    erro_msg = f"Erro na linha {numero_linha} ('{expressao}'): {e}"
                    erros.append(erro_msg)
                    print(f"   💾 Erro armazenado na lista")
                    
                except Exception as e:
                    print(f"   ❌ ERRO INESPERADO!")
                    print(f"   📋 Tipo: {type(e).__name__}")
                    erro_msg = f"Erro inesperado na linha {numero_linha} ('{expressao}'): {e}"
                    erros.append(erro_msg)
                    print(f"   💾 Erro armazenado na lista")
            
            print("\n" + "-" * 60)
            print("📊 RESUMO DO PROCESSAMENTO:")
            print("-" * 60)
            print(f"   📝 Total de linhas processadas: {total_linhas}")
            print(f"   ⏭️  Linhas vazias ignoradas: {linhas_vazias}")
            print(f"   ✅ Expressões calculadas com sucesso: {len(resultados)}")
            print(f"   ❌ Erros encontrados: {len(erros)}")
            print("-" * 60)
            
    except FileNotFoundError:
        print(f"\n❌ ERRO CRÍTICO: O arquivo de entrada '{arquivo_entrada}' não foi encontrado.")
        print("   Verifique se o caminho do arquivo está correto.")
        return
    except Exception as e:
        print(f"\n❌ ERRO CRÍTICO ao ler o arquivo de entrada: {e}")
        print(f"   Tipo do erro: {type(e).__name__}")
        return

    print(f"\n💾 Iniciando gravação do arquivo de saída '{arquivo_saida}'...")
    try:
        with open(arquivo_saida, 'w') as f_saida:
            print("   ✅ Arquivo de saída aberto com sucesso")
            print("   📝 Escrevendo cabeçalho...")
            f_saida.write("Resultados das Expressões:\n")
            f_saida.write("--------------------------\n")
            
            print(f"   📝 Escrevendo {len(resultados)} resultado(s)...")
            for res in resultados:
                f_saida.write(res + '\n')
            
            if erros:
                print(f"   📝 Escrevendo {len(erros)} erro(s)...")
                f_saida.write("\nErros encontrados:\n")
                f_saida.write("------------------\n")
                for err in erros:
                    f_saida.write(err + '\n')
            
            print("   ✅ Dados gravados com sucesso!")
        
        print(f"\n✅ Processamento concluído!")
        print(f"📄 Resultados gravados em '{arquivo_saida}'.")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ ERRO CRÍTICO ao escrever no arquivo de saída: {e}")
        print(f"   Tipo do erro: {type(e).__name__}")
        print("=" * 60)

