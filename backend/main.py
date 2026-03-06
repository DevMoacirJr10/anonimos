import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib
from fastapi.middleware.cors import CORSMiddleware

# 1. MUDANÇA: Tiramos o 'import sqlite3' e colocamos o Supabase
from supabase import create_client, Client

app = FastAPI()

# Configuração BLINDADA de CORS (Mantida igual!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. MUDANÇA: Substituímos o 'iniciar_banco()' do SQLite por isso aqui:
SUPABASE_URL = "https://oqfnduzdddnoqxdxxobu.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9xZm5kdXpkZGRub3F4ZHh4b2J1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njk4NDM0NzcsImV4cCI6MjA4NTQxOTQ3N30.rZlLW17xMDeys8eobwnO7vhSYigxK88MrvhxTwgKIzc" 
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- SEUS MODELOS (Mantidos iguais!) ---
class CadastroUsuario(BaseModel):
    nome: str
    email: str
    senha: str

class LoginUsuario(BaseModel):
    email: str
    senha: str


# --- ROTAS ---

@app.post("/testar_cadastro")
async def testar_cadastro(usuario: CadastroUsuario):
    # A segurança do Hash continua igual (Isso é ótimo para falar na reunião!)
    senha_hash = hashlib.sha256(usuario.senha.encode()).hexdigest()
    
    try:
        # 3. MUDANÇA: Trocamos o INSERT do SQL pelo comando do Supabase
        response = supabase.table("usuarios").insert({
            "nome": usuario.nome,
            "email": usuario.email,
            "senha_hash": senha_hash
        }).execute()
        
        return {"status": "sucesso", "mensagem": f"Usuário {usuario.nome} cadastrado com sucesso no Supabase!"}
        
    except Exception as e:
        # Se o e-mail já existir, o erro cai aqui
        print(f"Erro no banco: {e}")
        raise HTTPException(status_code=400, detail="Este e-mail já existe no banco de dados!")


@app.post("/testar_login")
async def testar_login(dados: LoginUsuario):
    try:
        # 4. MUDANÇA: Trocamos o SELECT do SQL pela busca do Supabase
        response = supabase.table("usuarios").select("*").eq("email", dados.email).execute()
        
        # Se a lista vier vazia, o usuário não existe
        if not response.data:
            raise HTTPException(status_code=400, detail="Usuário não encontrado!")
        
        # Pegamos o primeiro usuário que ele achou na lista
        usuario_banco = response.data[0]
        
        # Verificamos a senha
        if hashlib.sha256(dados.senha.encode()).hexdigest() == usuario_banco["senha_hash"]:
            return {"status": "sucesso", "mensagem": f"Bem-vindo, {usuario_banco['nome']}!"}
        else:
            raise HTTPException(status_code=401, detail="Senha incorreta!")
            
    except HTTPException:
        # Repassa os erros de senha ou usuário não encontrado
        raise
    except Exception as e:
        print(f"Erro no banco: {e}")
        raise HTTPException(status_code=500, detail="Erro interno ao conectar com o banco de dados.")