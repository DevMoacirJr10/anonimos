from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import hashlib
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuração BLINDADA de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens (Vercel, Localhost, etc)
    allow_credentials=True,
    allow_methods=["*"],  # Permite POST, GET, OPTIONS, etc.
    allow_headers=["*"],  # Permite todos os headers
)

# --- SEUS MODELOS ---
class CadastroUsuario(BaseModel):
    nome: str
    email: str
    senha: str

class LoginUsuario(BaseModel):
    email: str
    senha: str

# --- BANCO DE DADOS ---
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

try:
    iniciar_banco()
except Exception as e:
    print(f"Erro ao iniciar banco: {e}")

# --- ROTAS ---
@app.post("/testar_cadastro")
async def testar_cadastro(usuario: CadastroUsuario):
    conexao = sqlite3.connect('banco_teste.db')
    cursor = conexao.cursor()
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

@app.post("/testar_login")
async def testar_login(dados: LoginUsuario):
    conexao = sqlite3.connect('banco_teste.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT senha_hash, nome FROM usuarios WHERE email = ?", (dados.email,))
    resultado = cursor.fetchone()
    conexao.close()
    
    if not resultado:
        raise HTTPException(status_code=400, detail="Usuário não encontrado!")
    
    if hashlib.sha256(dados.senha.encode()).hexdigest() == resultado[0]:
        return {"status": "sucesso", "mensagem": f"Bem-vindo, {resultado[1]}!"}
    else:
        raise HTTPException(status_code=401, detail="Senha incorreta!")