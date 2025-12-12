"""
Exemplos de Uso da API Flask com curl e requests

Este arquivo contém exemplos práticos de como interagir com a API
usando ferramentas como curl, Python requests e Postman.
"""

# ============================================================================
# EXEMPLOS COM CURL (Terminal/PowerShell)
# ============================================================================

# Assumindo que a API está rodando em http://localhost:5000

# 1. HEALTH CHECK
# ==============
# curl http://localhost:5000/api/health
# Resposta: {"status": "healthy", "timestamp": "2024-01-15T10:30:00.123456"}


# 2. LISTAR POSTS (vazio inicialmente)
# =====================================
# curl http://localhost:5000/api/posts
# Resposta: []


# 3. CRIAR UM POST
# ================
# curl -X POST http://localhost:5000/api/posts \
#   -H "Content-Type: application/json" \
#   -d '{"title": "Meu Primeiro Post", "content": "Este é o conteúdo", "author": "João"}'
# 
# Resposta: 
# {
#   "id": 1,
#   "title": "Meu Primeiro Post",
#   "content": "Este é o conteúdo",
#   "author": "João",
#   "created_at": "2024-01-15T10:30:00.123456",
#   "updated_at": "2024-01-15T10:30:00.123456"
# }


# 4. OBTER POST ESPECÍFICO
# =========================
# curl http://localhost:5000/api/posts/1
# Resposta: {post completo}


# 5. ATUALIZAR POST
# =================
# curl -X PUT http://localhost:5000/api/posts/1 \
#   -H "Content-Type: application/json" \
#   -d '{"title": "Título Atualizado"}'
# 
# Resposta: {post com título atualizado}


# 6. DELETAR POST
# ===============
# curl -X DELETE http://localhost:5000/api/posts/1
# Resposta: {"message": "Post deleted successfully"}


# 7. BUSCAR POSTS
# ===============
# curl "http://localhost:5000/api/posts/search?q=Python"
# Resposta: [posts que contenham "Python" no título]


# ============================================================================
# EXEMPLOS COM PYTHON (requests)
# ============================================================================

import requests
import json

BASE_URL = "http://localhost:5000/api"

class ExemplosAPI:
    """Exemplos de uso da API com requests"""
    
    @staticmethod
    def exemplo_1_health_check():
        """Exemplo 1: Verificar saúde da API"""
        print("📋 Exemplo 1: Health Check")
        print("-" * 50)
        
        response = requests.get(f"{BASE_URL}/health")
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        print()
    
    @staticmethod
    def exemplo_2_criar_post():
        """Exemplo 2: Criar um novo post"""
        print("📋 Exemplo 2: Criar Post")
        print("-" * 50)
        
        novo_post = {
            "title": "Python Basics",
            "content": "Introdução ao Python",
            "author": "Maria Silva"
        }
        
        response = requests.post(
            f"{BASE_URL}/posts",
            json=novo_post
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        return response.json()['id']
    
    @staticmethod
    def exemplo_3_listar_posts():
        """Exemplo 3: Listar todos os posts"""
        print("📋 Exemplo 3: Listar Posts")
        print("-" * 50)
        
        response = requests.get(f"{BASE_URL}/posts")
        
        print(f"Status Code: {response.status_code}")
        print(f"Total Posts: {len(response.json())}")
        for post in response.json():
            print(f"  - {post['title']} (ID: {post['id']})")
        print()
    
    @staticmethod
    def exemplo_4_obter_post_especifico(post_id):
        """Exemplo 4: Obter um post específico"""
        print(f"📋 Exemplo 4: Obter Post {post_id}")
        print("-" * 50)
        
        response = requests.get(f"{BASE_URL}/posts/{post_id}")
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        print()
    
    @staticmethod
    def exemplo_5_atualizar_post(post_id):
        """Exemplo 5: Atualizar um post"""
        print(f"📋 Exemplo 5: Atualizar Post {post_id}")
        print("-" * 50)
        
        atualizacao = {
            "title": "Python Avançado",
            "content": "Conceitos avançados de Python"
        }
        
        response = requests.put(
            f"{BASE_URL}/posts/{post_id}",
            json=atualizacao
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        print()
    
    @staticmethod
    def exemplo_6_buscar_posts(termo):
        """Exemplo 6: Buscar posts"""
        print(f"📋 Exemplo 6: Buscar Posts com '{termo}'")
        print("-" * 50)
        
        response = requests.get(
            f"{BASE_URL}/posts/search",
            params={'q': termo}
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Resultados: {len(response.json())}")
        for post in response.json():
            print(f"  - {post['title']}")
        print()
    
    @staticmethod
    def exemplo_7_deletar_post(post_id):
        """Exemplo 7: Deletar um post"""
        print(f"📋 Exemplo 7: Deletar Post {post_id}")
        print("-" * 50)
        
        response = requests.delete(f"{BASE_URL}/posts/{post_id}")
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        print()
    
    @staticmethod
    def exemplo_8_fluxo_completo():
        """Exemplo 8: Fluxo completo (criar, ler, atualizar, deletar)"""
        print("📋 Exemplo 8: Fluxo Completo (CRUD)")
        print("=" * 50)
        print()
        
        # CREATE
        print("1️⃣  CRIAR POST")
        novo_post = {
            "title": "Flask Tutorial",
            "content": "Aprenda Flask do zero",
            "author": "João"
        }
        response = requests.post(f"{BASE_URL}/posts", json=novo_post)
        post_id = response.json()['id']
        print(f"   ✅ Post criado com ID: {post_id}")
        print()
        
        # READ
        print("2️⃣  LER POST")
        response = requests.get(f"{BASE_URL}/posts/{post_id}")
        post = response.json()
        print(f"   ✅ Post obtido: {post['title']}")
        print()
        
        # UPDATE
        print("3️⃣  ATUALIZAR POST")
        atualizacao = {"title": "Flask Intermediário"}
        response = requests.put(f"{BASE_URL}/posts/{post_id}", json=atualizacao)
        post = response.json()
        print(f"   ✅ Post atualizado: {post['title']}")
        print()
        
        # DELETE
        print("4️⃣  DELETAR POST")
        response = requests.delete(f"{BASE_URL}/posts/{post_id}")
        print(f"   ✅ Post deletado")
        print()
        
        # VERIFY
        print("5️⃣  VERIFICAR DELEÇÃO")
        response = requests.get(f"{BASE_URL}/posts/{post_id}")
        if response.status_code == 404:
            print(f"   ✅ Confirmado: Post não existe mais")
        print()
    
    @staticmethod
    def exemplo_9_tratamento_erros():
        """Exemplo 9: Tratamento de erros"""
        print("📋 Exemplo 9: Tratamento de Erros")
        print("-" * 50)
        
        # Tentar criar post sem título
        print("Tentando criar post sem título...")
        response = requests.post(
            f"{BASE_URL}/posts",
            json={"content": "Sem título"}
        )
        
        print(f"Status Code: {response.status_code}")
        if response.status_code == 400:
            print(f"❌ Erro esperado: {response.json()['error']}")
        print()
        
        # Tentar obter post inexistente
        print("Tentando obter post inexistente...")
        response = requests.get(f"{BASE_URL}/posts/9999")
        
        print(f"Status Code: {response.status_code}")
        if response.status_code == 404:
            print(f"❌ Erro esperado: {response.json()['error']}")
        print()


# ============================================================================
# EXEMPLO DE USO
# ============================================================================

if __name__ == "__main__":
    # ⚠️  Certifique-se de que a API está rodando:
    # python modulo_13/crie_api_para_blog.py
    
    print("=" * 60)
    print("EXEMPLOS DE USO DA API FLASK")
    print("=" * 60)
    print()
    
    try:
        # Exemplo 1: Health Check
        ExemplosAPI.exemplo_1_health_check()
        
        # Exemplo 2: Criar Post
        post_id = ExemplosAPI.exemplo_2_criar_post()
        
        # Exemplo 3: Listar Posts
        ExemplosAPI.exemplo_3_listar_posts()
        
        # Exemplo 4: Obter Post Específico
        ExemplosAPI.exemplo_4_obter_post_especifico(post_id)
        
        # Exemplo 5: Atualizar Post
        ExemplosAPI.exemplo_5_atualizar_post(post_id)
        
        # Exemplo 6: Buscar Posts
        ExemplosAPI.exemplo_6_buscar_posts("Python")
        
        # Exemplo 7: Deletar Post
        ExemplosAPI.exemplo_7_deletar_post(post_id)
        
        # Exemplo 8: Fluxo Completo
        ExemplosAPI.exemplo_8_fluxo_completo()
        
        # Exemplo 9: Tratamento de Erros
        ExemplosAPI.exemplo_9_tratamento_erros()
        
    except requests.exceptions.ConnectionError:
        print("❌ Erro: Não foi possível conectar à API!")
        print("💡 Dica: Certifique-se de que a API está rodando:")
        print("   python modulo_13/crie_api_para_blog.py")
    except Exception as e:
        print(f"❌ Erro: {e}")
