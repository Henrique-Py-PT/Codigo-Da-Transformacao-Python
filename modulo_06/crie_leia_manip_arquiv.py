nome_arquivo_txt = "informacoes.txt"
conteudo = [
    "Linha 1: Guardando dados fora do código.",
    "Linha 2: A manipulação de arquivos é essencial.",
    "Linha 3: Este é um teste de leitura e escrita."
]

try:
    with open(nome_arquivo_txt, 'w', encoding='utf-8') as arquivo:
        for linha in conteudo:
            arquivo.write(linha + "\n")
    print(f"✅ Arquivo '{nome_arquivo_txt}' criado e escrito com sucesso.")

    # --- LEITURA ---
    with open(nome_arquivo_txt, 'r', encoding='utf-8') as arquivo:
        conteudo_lido = arquivo.read()
    
    print("\nConteúdo Lido do Arquivo:")
    print("-" * 30)
    print(conteudo_lido)
    print("-" * 30)

except IOError as e:
    print(f"❌ Erro ao manipular o arquivo TXT: {e}")