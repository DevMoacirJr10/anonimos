from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import hashlib
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite que qualquer site (Vercel ou Local) acesse
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Definir o Contrato de Dados (Sua tarefa da semana)
class CadastroUsuario(BaseModel):
    nome: str
    email: str
    senha: str

# 2. Lógica de Inicialização do Banco (Lógica do Neto)
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

# 3. Sua Rota de Teste
@app.post("/testar_cadastro")
async def testar_cadastro(usuario: CadastroUsuario):
    conexao = sqlite3.connect('banco_teste.db')
    cursor = conexao.cursor()
    
    # Gerando o hash da senha (Segurança)
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