from fastapi import FastAPI

app = FastAPI()

#Importante
'''
Bem vindos
Antes de fazer qualquer coisa no código(serve até mesmo se for só testar),
verificar se tem o python instalado na máquina, seguir o comando abaixo:
python --version

Depois instale os fastAPI:
pip install fastapi

Instale o uvicorn, que vai ser o servidor ultrarrápido que vai rodar a API:
pip install uvicorn

Crie o ambiente virtual em backend:
cd backend
python -m venv .venv

Ative o ambiente virtual:
.\.venv\Scripts\activate

Após isso basta rodar e clicar na porta que vai aparecer no terminal segurando a tecla "CTRL":
uvicorn app:app --reload
'''
#Agora vamos produzir, e entender os exemplos de "GET" abaixo:

vendas = {
    1: {"item": "luminho", "preco_unitario": 20, "quantidade": 5},
    2: {"item": "sput", "preco_unitario": 15, "quatidade": 5},
    3: {"item": "laika", "preco_unitario": 10, "quantidade": 5},
    4: {"item": "aria", "preco_unitario": 5, "quantidade": 5}
}

@app.get("/")
def home():
    return { "Status" : "API Online",
            "Projeto":"Anônimos",
        "Vendas": len(vendas)}

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {"Erro": "ID Venda inexistente"}