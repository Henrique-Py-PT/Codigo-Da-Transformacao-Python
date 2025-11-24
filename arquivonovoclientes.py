import json
from faker import Faker
import random


fake = Faker('pt_BR') 

def gerar_cliente():

    endereco_completo = f"{fake.street_name()}, {random.randint(100, 1000)}"
    
    cliente = {
        "nome": fake.name(),
        "idade": random.randint(18, 65),  
        "cidade": fake.city(),
        "telefone": fake.cellphone_number(),
        "email": fake.email(),
        "cpf": fake.cpf(),
        "endereco": endereco_completo
    }
    return cliente

# 1. Configuração e Geração de Dados
NUMERO_CLIENTES = 4
clientes = []

print(f"Gerando dados para {NUMERO_CLIENTES} clientes...")

# Gera a lista de clientes
for _ in range(NUMERO_CLIENTES):
    clientes.append(gerar_cliente())

# 2. Salvar no Arquivo JSON
NOME_ARQUIVO = "clientes.json" 
try:
    with open(NOME_ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(clientes, f, ensure_ascii=False, indent=4)
    
    print(f"✅ Sucesso! O arquivo '{NOME_ARQUIVO}' foi criado com {len(clientes)} clientes.")

except Exception as e:
    print(f"❌ Ocorreu um erro ao salvar o arquivo: {e}")