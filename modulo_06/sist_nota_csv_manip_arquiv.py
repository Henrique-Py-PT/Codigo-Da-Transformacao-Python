import csv
from typing import List, Dict

## Arquivo CSV: Adicionar e Carregar Notas

nome_arquivo_csv = "notas_alunos.csv"

def adicionar_notas(alunos: List[Dict]):
    """Adiciona as notas ao arquivo CSV."""
    cabecalho = ["Nome", "Materia", "Nota_1", "Nota_2", "Media"]
    
    # O modo 'w' sobrescreveria, o 'a' adiciona novas linhas (append)
    # Neste caso, usamos 'w' para garantir que o cabeçalho seja escrito corretamente
    try:
        with open(nome_arquivo_csv, 'w', newline='', encoding='utf-8') as arquivo:
            escritor_csv = csv.DictWriter(arquivo, fieldnames=cabecalho)
            
            # Escreve o cabeçalho
            escritor_csv.writeheader()
            
            # Escreve as linhas de dados
            escritor_csv.writerows(alunos)
        
        print(f"✅ Notas salvas em '{nome_arquivo_csv}' com sucesso.")
    except IOError as e:
        print(f"❌ Erro ao escrever no arquivo CSV: {e}")

def carregar_notas():
    """Lê e imprime todas as notas do arquivo CSV."""
    print(f"\nConteúdo Lido de '{nome_arquivo_csv}':")
    try:
        with open(nome_arquivo_csv, 'r', newline='', encoding='utf-8') as arquivo:
            leitor_csv = csv.DictReader(arquivo)
            
            for linha in leitor_csv:
                # O leitor_csv trata cada linha como um dicionário
                print(f"Nome: {linha['Nome']} | Matéria: {linha['Materia']} | Média: {linha['Media']}")
    except FileNotFoundError:
        print("Arquivo CSV não encontrado.")
    except Exception as e:
        print(f"❌ Erro ao ler o arquivo CSV: {e}")


# --- Execução ---
dados_novos = [
    {"Nome": "Pedro", "Materia": "Matemática", "Nota_1": 8.0, "Nota_2": 9.5, "Media": 8.75},
    {"Nome": "Luisa", "Materia": "Português", "Nota_1": 7.0, "Nota_2": 6.0, "Media": 6.50},
    {"Nome": "Felipe", "Materia": "História", "Nota_1": 9.0, "Nota_2": 8.5, "Media": 8.75}
]

adicionar_notas(dados_novos)
carregar_notas()