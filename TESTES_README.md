## 🧪 Testes Automatizados para API Flask com pytest

Este desafio implementa uma suite completa de testes para uma API Flask usando **pytest** - um dos frameworks de teste mais populares do Python.

### 📋 Conteúdo Implementado

#### 1. **API Flask Completa** (`modulo_13/crie_api_para_blog.py`)
Uma API RESTful de blog com as seguintes features:
- ✅ Endpoints CRUD (Create, Read, Update, Delete)
- ✅ Validação de dados
- ✅ Tratamento de erros
- ✅ Busca de posts
- ✅ Timestamps automáticos

**Endpoints disponíveis:**
```
GET    /api/health           - Verificar saúde da API
GET    /api/posts            - Listar todos os posts
GET    /api/posts/<id>       - Obter post específico
GET    /api/posts/search     - Buscar posts por título
POST   /api/posts            - Criar novo post
PUT    /api/posts/<id>       - Atualizar post
DELETE /api/posts/<id>       - Deletar post
```

#### 2. **Suite de Testes Completa** (`modulo_12/implemente_testes_teste_automatizados.py`)

**Cobertura de Testes:**
- 🟢 **50+ testes automatizados** organizados em 9 classes
- 🟢 **Fixtures reutilizáveis** para dados de teste
- 🟢 **Testes unitários** (teste comportamento individual)
- 🟢 **Testes de integração** (teste fluxo completo)
- 🟢 **Testes de validação** (teste tipos e estrutura)
- 🟢 **Testes de erro** (teste tratamento de exceções)

**Classes de Teste:**
```
✓ TestHealthCheck          - 3 testes
✓ TestListPosts            - 4 testes
✓ TestCreatePost           - 9 testes
✓ TestGetPost              - 4 testes
✓ TestUpdatePost           - 6 testes
✓ TestDeletePost           - 4 testes
✓ TestSearchPosts          - 5 testes
✓ TestIntegration          - 2 testes (fluxo completo)
✓ TestDataValidation       - 3 testes
✓ TestErrorHandling        - 4 testes
```

#### 3. **Testes Avançados** (`modulo_12/teste_avancado_teste_automatizados.py`)

Exemplos de técnicas avançadas:
- 📊 **Parametrização** - rodar teste com múltiplos valores
- 🏷️ **Marcadores customizados** - @pytest.mark.unit, @pytest.mark.integration
- 🔍 **Fixtures complexas** - setup/teardown automático
- ⚡ **Testes de performance** - verificar tempo de resposta
- 🛡️ **Captura de exceções** - verificar erro handling

#### 4. **Configurações** (`modulo_13/config_servidor_dev_api_com_flask.py`)
- Configurações por ambiente (development, testing, production)
- Modo debug e testing configurável
- Banco de dados em memória para testes

#### 5. **Documentação** 
- 📖 `GUIA_TESTES_PYTEST.md` - Guia completo com exemplos
- 📋 `requirements.txt` - Dependências do projeto
- ⚙️ `pytest.ini` - Configuração do pytest

---

### 🚀 Como Usar

#### 1. **Instalar Dependências**
```bash
pip install -r requirements.txt
```

Ou instale manualmente:
```bash
pip install Flask pytest pytest-cov pytest-flask
```

#### 2. **Executar Testes**

**Teste básico:**
```bash
pytest modulo_12/implemente_testes_teste_automatizados.py
```

**Com detalhes verbose:**
```bash
pytest modulo_12/implemente_testes_teste_automatizados.py -v
```

**Com outputs (prints) visíveis:**
```bash
pytest modulo_12/implemente_testes_teste_automatizados.py -v -s
```

**Com cobertura de código:**
```bash
pytest modulo_12/implemente_testes_teste_automatizados.py --cov=modulo_13
```

**Testes avançados:**
```bash
pytest modulo_12/teste_avancado_teste_automatizados.py -v
```

**Apenas testes unitários:**
```bash
pytest modulo_12/ -m unit -v
```

**Apenas testes de integração:**
```bash
pytest modulo_12/ -m integration -v
```

**Teste específico:**
```bash
pytest modulo_12/implemente_testes_teste_automatizados.py::TestCreatePost::test_create_post_returns_201 -v
```

**Com parada no primeiro erro:**
```bash
pytest modulo_12/ -x
```

#### 3. **Rodar a API Manualmente (Opcional)**
```bash
python modulo_13/crie_api_para_blog.py
# API estará disponível em http://localhost:5000
```

---

### 📊 Exemplo de Saída

```
modulo_12/implemente_testes_teste_automatizados.py::TestHealthCheck::test_health_endpoint_returns_200 PASSED [ 1%]
modulo_12/implemente_testes_teste_automatizados.py::TestHealthCheck::test_health_endpoint_returns_healthy_status PASSED [ 2%]
...
modulo_12/implemente_testes_teste_automatizados.py::TestErrorHandling::test_missing_content_type_with_json_data PASSED [100%]

==================== 50 passed in 0.45s ====================
```

---

### 🎯 Conceitos Principais

#### **Fixtures**
Funções que fornecem dados para os testes:
```python
@pytest.fixture
def client(app):
    return app.test_client()

def test_something(client):  # client é injetado automaticamente
    response = client.get('/api/health')
```

#### **Padrão AAA (Arrange-Act-Assert)**
Estrutura padrão para testes:
```python
def test_create_post(client, sample_post):
    # ARRANGE: Preparar dados
    # ASSERT: Executar ação
    response = client.post('/api/posts', data=json.dumps(sample_post), ...)
    # ASSERT: Verificar resultado
    assert response.status_code == 201
```

#### **Asserções**
Verificações no teste:
```python
assert response.status_code == 200           # Status code
assert len(data) == 5                        # Tamanho
assert 'title' in data                       # Pertencimento
assert data['id'] != expected_id             # Desigualdade
```

#### **Parametrização**
Executar teste com múltiplos valores:
```python
@pytest.mark.parametrize("status_code", [200, 201, 404])
def test_status_codes(client, status_code):
    ...
```

---

### 📈 Cobertura de Código

A suite cobre:
- ✅ Todos os endpoints HTTP
- ✅ Casos de sucesso (status 200-201)
- ✅ Casos de erro (status 400, 404)
- ✅ Validação de dados
- ✅ Tipos e estrutura de respostas
- ✅ Fluxos de negócio (criar → atualizar → deletar)
- ✅ Busca e filtros
- ✅ Tratamento de exceções

---

### 🔧 Extensões Possíveis

1. **Testes com Mock:**
   ```python
   from unittest.mock import patch
   
   @patch('datetime.datetime')
   def test_with_mock(mock_datetime, client):
       mock_datetime.now.return_value = '2024-01-01'
       ...
   ```

2. **Testes com Database:**
   ```python
   @pytest.fixture
   def db():
       db = Database()
       db.create_tables()
       yield db
       db.drop_tables()
   ```

3. **Testes de Load:**
   ```python
   @pytest.mark.slow
   def test_bulk_operations(client):
       for i in range(1000):
           client.post('/api/posts', ...)
   ```

---

### 📚 Recursos Adicionais

- **Documentação oficial pytest:** https://docs.pytest.org/
- **Documentação Flask Testing:** https://flask.palletsprojects.com/testing/
- **Guia Completo:** Veja `GUIA_TESTES_PYTEST.md`

---

### ✨ Padrões Seguidos

Este projeto segue as práticas educacionais do "Código da Transformação":
- ✅ Português em código e documentação
- ✅ Exemplos práticos e autocontidos
- ✅ Seções comentadas e organizadas
- ✅ Nomes descritivos e claros
- ✅ Demonstrações de cada conceito

---

### 💡 Próximos Passos

1. ✅ Execute os testes: `pytest modulo_12/ -v`
2. ✅ Explore a cobertura: `pytest modulo_12/ --cov`
3. ✅ Estude os padrões em `teste_avancado_teste_automatizados.py`
4. ✅ Integre com seu CI/CD (GitHub Actions, GitLab CI, etc.)
5. ✅ Configure pre-commit hooks para rodar testes automaticamente

---

**Desafio completado! 🎉**

Você agora tem uma suite profissional de testes para uma API Flask, pronta para uso em projetos educacionais e reais.
