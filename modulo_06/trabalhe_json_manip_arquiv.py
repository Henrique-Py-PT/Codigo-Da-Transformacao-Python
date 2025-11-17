import json

## Arquivo JSON: Salvar e Carregar Dicionário

nome_arquivo_json = "clientes.json"

# Dados Python (Dicionário)
dados_clientes = {
    "cliente_001": {"nome": "Maria Silva", "email": "maria@exemplo.com", "ativo": True},
    "cliente_002": {"nome": "João Souza", "email": "joao@exemplo.com", "ativo": False},
    "cliente_003": {"nome": "Ana Oliveira", "email": "ana@exemplo.com", "ativo": True}
}

# --- SALVAR Dicionário em JSON ---
try:
    with open(nome_arquivo_json, 'w', encoding='utf-8') as arquivo:
        json.dump(dados_clientes, arquivo, indent=4) 
    print(f"✅ Dados salvos em '{nome_arquivo_json}' com sucesso.")
    
    with open(nome_arquivo_json, 'r', encoding='utf-8') as arquivo:
        # A função json.load() lê o JSON e o converte em um dicionário Python
        dados_carregados = json.load(arquivo)

    print("\nDados Carregados (Dicionário Python):")
    print(f"Total de clientes carregados: {len(dados_carregados)}")
    print("Detalhe do Cliente 002:", dados_carregados["cliente_002"])

except Exception as e:
    print(f"❌ Erro ao manipular o arquivo JSON: {e}")