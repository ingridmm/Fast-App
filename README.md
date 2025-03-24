# 📌 FastAPI Integrado com Leitura para CSV

## 1️⃣ Introdução
Este projeto consiste em uma API desenvolvida com **FastAPI**, que permite o cadastro de usuários com autenticação JWT. Além disso, há um script Python que lê dados de um arquivo CSV e os envia para a API.

---
## 2️⃣ Requisitos
Antes de iniciar, certifique-se de ter instalado:
- **Python 3.8+**
- **Pip**
- Bibliotecas necessárias:
  ```bash
  pip install fastapi uvicorn pydantic[email] python-jose[cryptography] passlib[bcrypt] sqlalchemy requests
  ```

---
## 3️⃣ Configuração do ambiente
1. **Clone o repositório** (se aplicável):
   ```bash
   git clone https://github.com/seu-repositorio.git
   cd nome-do-projeto
   ```
2. **Criação do banco de dados**: O banco SQLite será criado automaticamente ao iniciar a API.
3. **Arquivos do projeto**:
   - `main.py` → API principal
   - `database.py` → Configuração do banco de dados
   - `schemas.py` → Validação de dados
   - `auth.py` → Autenticação JWT
   - `script.py` → Script para envio de dados via CSV
   - `usuarios.csv` → Arquivo de entrada de dados

---
## 4️⃣ Execução da API
Para iniciar a API, execute:
```bash
uvicorn main:app --reload
```
Após iniciar, acesse a documentação interativa em:
🔗 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---
## 5️⃣ Uso dos Endpoints
### 🔹 **1. Login (`POST /login`)**
**Descrição:** Gera um token JWT para autenticação.
**Exemplo de requisição:**
```json
{
  "username": "admin@example.com",
  "password": "senha123"
}
```
**Resposta esperada:**
```json
{
  "access_token": "TOKEN_JWT",
  "token_type": "bearer"
}
```

### 🔹 **2. Cadastro de usuário (`POST /users`)**
**Descrição:** Cadastra um novo usuário na API.
**Requer autenticação JWT.**
**Exemplo de requisição:**
```json
{
  "nome": "Ana Silva",
  "email": "ana.silva@example.com",
  "cpf": "123.456.789-00",
  "data_nascimento": "1990-05-14"
}
```
**Resposta esperada:**
```json
{
  "message": "Usuário cadastrado com sucesso!",
  "user": {
    "nome": "Ana Silva",
    "email": "ana.silva@example.com",
    "cpf": "123.456.789-00",
    "data_nascimento": "1990-05-14"
  }
}
```

### 🔹 **3. Listagem de usuários (`GET /users`)**
**Descrição:** Retorna todos os usuários cadastrados.
**Requer autenticação JWT.**

---
## 6️⃣ Execução do script de integração
O script `script.py` lê os dados do arquivo `usuarios.csv` e os envia para a API. Para executá-lo:
```bash
python script.py
```

**Exemplo de saída esperada:**
```
✅ Usuário Ana Silva cadastrado com sucesso!
✅ Usuário Bruno Souza cadastrado com sucesso!
✅ Usuário Carla Pereira cadastrado com sucesso!
❌ Erro ao cadastrar Daniel Oliveira: {'detail': 'CPF inválido'}
```

---

