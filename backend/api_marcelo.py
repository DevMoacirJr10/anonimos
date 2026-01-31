from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import hashlib
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuração de CORS para permitir a conexão com o Frontend na Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Modelos de Dados (Contratos da API)
class CadastroUsuario(BaseModel):
    nome: str
    email: str
    senha: str

class LoginUsuario(BaseModel):
    email: str
    senha: str

# 2. Inicialização do Banco de Dados
def iniciar_banco():
    conexao = sqlite3.connect('banco_teste.db')
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE,
            senha_hash TEXT
        )
    """)
    conexao.commit()
    conexao.close()

iniciar_banco()

# 3. Rota de Cadastro
@app.post("/testar_cadastro")
async def testar_cadastro(usuario: CadastroUsuario):
    conexao = sqlite3.connect('banco_teste.db')
    cursor = conexao.cursor()
    
    # Segurança: Transformando a senha em Hash antes de salvar
    senha_hash = hashlib.sha256(usuario.senha.encode()).hexdigest()
    
    try:
        cursor.execute("INSERT INTO usuarios (nome, email, senha_hash) VALUES (?, ?, ?)", 
                       (usuario.nome, usuario.email, senha_hash))
        conexao.commit()
        return {"status": "sucesso", "mensagem": f"Usuário {usuario.nome} cadastrado!"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Este e-mail já existe no banco!")
    finally:
        conexao.close()

# 4. Rota de Login (Nova Rota para sua tela de Teste)
@app.post("/testar_login")
async def testar_login(dados: LoginUsuario):
    conexao = sqlite3.connect('banco_teste.db')
    cursor = conexao.cursor()
    
    # Busca o usuário pelo e-mail
    cursor.execute("SELECT senha_hash, nome FROM usuarios WHERE email = ?", (dados.email,))
    resultado = cursor.fetchone()
    conexao.close()
    
    if not resultado:
        raise HTTPException(status_code=400, detail="Usuário não encontrado!")
    
    senha_banco = resultado[0]
    nome_usuario = resultado[1]
    
    # Verifica se a senha digitada bate com o Hash do banco
    senha_digitada_hash = hashlib.sha256(dados.senha.encode()).hexdigest()
    
    if senha_digitada_hash == senha_banco:
        return {"status": "sucesso", "mensagem": f"Bem-vindo, {nome_usuario}!"}
    else:
        raise HTTPException(status_code=401, detail="Senha incorreta!")