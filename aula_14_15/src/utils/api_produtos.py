import random

import pandas as pd
from faker import Faker
from fastapi import FastAPI

app = FastAPI(debug=True)
fake = Faker()

# Carregar o arquivo CSV de produtos
file_name = "data/products.csv"
df = pd.read_csv(file_name)
df["indice"] = range(1, len(df) + 1)
df.set_index("indice", inplace=True)

loja_padrao_online = 11


@app.get("/")
async def hello_world():
    """Rota para retornar uma mensagem de saudação."""
    return "Coca-Cola me patrocina!"


@app.get("/gerar_compra")
async def gerar_compra():
    """Rota para gerar uma compra aleatória."""
    index = random.randint(1, len(df) - 1)
    row = df.iloc[index]
    return [
        {
            "client": fake.name(),
            "creditcard": fake.credit_card_provider(),
            "product": row["Product Name"],
            "ean": int(row["EAN"]),
            "price": round(float(row["Price"]) * 1.2, 2),
            "clientPosition": fake.location_on_land(),
            "store": loja_padrao_online,
            "dateTime": fake.iso8601(),
        }
    ]


@app.get("/gerar_compras/{numero_registro}")
async def gerar_compras(numero_registro: int):
    """Rota para gerar várias compras."""
    if numero_registro < 1:
        return {"error": "O número deve ser maior que 1"}

    respostas = []
    for _ in range(numero_registro):
        try:
            index = random.randint(1, len(df) - 1)
            row = df.iloc[index]
            compra = {
                "client": fake.name(),
                "creditcard": fake.credit_card_provider(),
                "product": row["Product Name"],
                "ean": int(row["EAN"]),
                "price": round(float(row["Price"]) * 1.2, 2),
                "clientPosition": fake.location_on_land(),
                "store": loja_padrao_online,
                "dateTime": fake.iso8601(),
            }
            respostas.append(compra)
        except Exception as e:
            print(f"Erro inesperado: {e}")
            # Se ocorrer um erro, adiciona uma compra com dados de erro
            compra = {
                "client": fake.name(),
                "creditcard": fake.credit_card_provider(),
                "product": "error",
                "ean": 0,
                "price": 0.0,
                "clientPosition": fake.location_on_land(),
                "store": loja_padrao_online,
                "dateTime": fake.iso8601(),
            }
            respostas.append(compra)
    return respostas
