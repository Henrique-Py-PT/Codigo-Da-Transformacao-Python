def validar_login(usuario, senha, usuarios_db):

    if usuario in usuarios_db:
        # 2. Se existe, verifica se a senha fornecida corresponde à senha armazenada
        if usuarios_db[usuario] == senha:
            return True  # Login Válido
        else:
            return False # Senha Incorreta
    else:
        return False # Usuário Não Encontrado

# Banco de dados de usuários (Dicionário)
DB_USUARIOS = {
    "admin": "senha123",
    "joao": "joao456",
    "maria": "maria_dev"
}

# --- Teste do Sistema de Login ---

# 1. Login Válido
user_input_a = "admin"
pass_input_a = "senha123"

if validar_login(user_input_a, pass_input_a, DB_USUARIOS):
    print(f"Login bem-sucedido para o usuário: {user_input_a}")
else:
    print(f"Falha no login. Usuário ou senha inválidos para: {user_input_a}")

# 2. Login Inválido (Senha Errada)
user_input_b = "joao"
pass_input_b = "senhaerrada"

if validar_login(user_input_b, pass_input_b, DB_USUARIOS):
    print(f"Login bem-sucedido para o usuário: {user_input_b}")
else:
    print(f"Falha no login. Usuário ou senha inválidos para: {user_input_b}")