# Código de Exemplo
import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL de busca no Mercado Livre

url = "https://lista.mercadolivre.com.br/shampoo"

# Realiza a requisição

response = requests.get(url)

# Verifica se a requisição foi bem-sucedida

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    data = []
    # Encontra todos os produtos na página
    for item in soup.find_all("div", class_="ui-search-result__content"):
        title = item.find("h2", class_="ui-search-item__title").text.strip()
        price = item.find(
            "span",
            class_="andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript",
        ).text.strip()
        link = item.find("a", class_="ui-search-link")["href"]
        data.append({"Título": title, "Preço": price, "Link": link})

    # Cria um DataFrame com os dados extraídos
    df = pd.DataFrame(data)
    print(df)

else:
    print("Erro na requisição")
