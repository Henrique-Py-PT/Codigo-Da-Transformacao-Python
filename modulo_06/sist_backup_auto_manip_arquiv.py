import shutil
import os
from datetime import datetime

## Desafio Extra: Backup de Arquivos (usando shutil)

# 1. Definição de Caminhos
# O código assume que essas pastas existem. Crie-as antes de rodar!
PASTA_ORIGEM = "origem_dados"
PASTA_DESTINO = "backup_dados"

# 2. Configuração
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
NOME_BACKUP = f"backup_completo_{timestamp}"
CAMINHO_BACKUP_FINAL = os.path.join(PASTA_DESTINO, NOME_BACKUP)


def criar_pastas_e_arquivos_teste():
    """Função para garantir que as pastas e alguns arquivos de teste existam."""
    os.makedirs(PASTA_ORIGEM, exist_ok=True)
    os.makedirs(PASTA_DESTINO, exist_ok=True)
    
    # Cria alguns arquivos de teste na origem
    with open(os.path.join(PASTA_ORIGEM, "doc1.txt"), "w") as f:
        f.write("Conteúdo do documento 1.")
    with open(os.path.join(PASTA_ORIGEM, "config.json"), "w") as f:
        f.write('{"data": "teste"}')
    print(f"Preparação: Arquivos criados em '{PASTA_ORIGEM}' para backup.")


def fazer_backup():
    """Copia todo o conteúdo da pasta de origem para uma nova pasta de destino."""
    try:
        # Copia toda a árvore de diretórios.
        # copytree exige que a pasta de destino não exista.
        shutil.copytree(PASTA_ORIGEM, CAMINHO_BACKUP_FINAL)
        
        print("\n--- Resultado do Backup ---")
        print(f"✅ Backup concluído com sucesso!")
        print(f"Origem: {PASTA_ORIGEM}")
        print(f"Destino: {CAMINHO_BACKUP_FINAL}")

    except FileExistsError:
        print(f"❌ Erro: O diretório de backup '{CAMINHO_BACKUP_FINAL}' já existe.")
    except Exception as e:
        print(f"❌ Erro no backup: {e}")


# --- Execução do Desafio Extra ---
criar_pastas_e_arquivos_teste()
fazer_backup()