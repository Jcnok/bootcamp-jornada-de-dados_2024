# Aula 01

# Resumo da Aula

Nesta aula, abordamos técnicas de web scraping utilizando Python. Abaixo estão os principais tópicos discutidos:

## Tecnologias e Ferramentas Utilizadas

- **Requests**: Biblioteca para fazer requisições HTTP.
- **BeautifulSoup**: Biblioteca para parseamento de HTML e extração de dados.
- **Pandas**: Biblioteca para manipulação e análise de dados.

## Passos Realizados

1. **Introdução ao Web Scraping**:
    - Explicação sobre a importância de entender HTML e a estrutura das páginas web.
    - Discussão sobre a ética e as implicações legais do web scraping.
2. **Configuração do Ambiente**:
    - Criação de um projeto básico em Python.
    - Instalação das bibliotecas necessárias (`requests`, `beautifulsoup4`, `pandas`).
3. **Primeira Requisição**:
    - Realização de uma requisição simples para obter o IP da máquina.
    - Explicação sobre o status code e a resposta da requisição.
4. **Extração de Dados do Mercado Livre**:
    - Construção de uma URL de busca dinâmica.
    - Parseamento do HTML retornado utilizando BeautifulSoup.
    - Extração de informações específicas como título, preço, marca e link dos produtos.
    - Armazenamento dos dados extraídos em um DataFrame do Pandas.
5. **Discussão sobre Técnicas Avançadas**:
    - Introdução ao uso de ferramentas como Selenium e Puppeteer para automação de navegadores.
    - Planejamento para futuras aulas, incluindo a criação de um objeto dinâmico para requisições paralelas e técnicas de login automatizado.

## Exemplo de scraping:

* **Instalando as libs**:


```python
!poetry add bs4 pandas -q
```

* **Codigo exemplo:**


```python
# Código de Exemplo
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de busca no Mercado Livre

url = "https://lista.mercadolivre.com.br/shampoo"

# Realiza a requisição

response = requests.get(url)

# Verifica se a requisição foi bem-sucedida

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    data = []
    # Encontra todos os produtos na página
    for item in soup.find_all('div', class_='ui-search-result__content'):
        title = item.find('h2', class_='ui-search-item__title').text.strip()
        price = item.find('span', class_='andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript').text.strip()
        link = item.find('a', class_='ui-search-link')['href']
        data.append({'Título': title, 'Preço': price, 'Link': link})

    # Cria um DataFrame com os dados extraídos
    df = pd.DataFrame(data)
    display(df)

else:
    print("Erro na requisição")

```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Título</th>
      <th>Preço</th>
      <th>Link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kit Shampoo E Condicionador Antiqueda Aq-01</td>
      <td>R$79</td>
      <td>https://www.mercadolivre.com.br/kit-shampoo-e-...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Kit Shampoo + Máscara Matizadora Black Home Ca...</td>
      <td>R$75,90</td>
      <td>https://www.mercadolivre.com.br/kit-shampoo-ma...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Doctar Plus Shampoo Anticaspa 240ml - Darrow</td>
      <td>R$94,90</td>
      <td>https://www.mercadolivre.com.br/doctar-plus-sh...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Shampoo Redutor De Grisalhos Grecin Control Gx...</td>
      <td>R$63,82</td>
      <td>https://www.mercadolivre.com.br/shampoo-reduto...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Shampoo Anticaspa Men Ice Cool Menthol 400ml C...</td>
      <td>R$22,90</td>
      <td>https://www.mercadolivre.com.br/shampoo-antica...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Keune Man Shampoo Fortify 250ml</td>
      <td>R$71,99</td>
      <td>https://www.mercadolivre.com.br/keune-man-sham...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Vichy Dercos Thechnique  Shampoo Antiqueda 400 g</td>
      <td>R$118,73</td>
      <td>https://www.mercadolivre.com.br/vichy-dercos-t...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Kit Zap Me Leva Black + Shampoo Detox 500ml</td>
      <td>R$42,90</td>
      <td>https://www.mercadolivre.com.br/kit-zap-me-lev...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Shampoo Anticaspa Intensivo Dercos Cabelos Sec...</td>
      <td>R$66,90</td>
      <td>https://www.mercadolivre.com.br/shampoo-antica...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Shampoo Esfoliante Anticaspa Vichy Dercos Micr...</td>
      <td>R$77,42</td>
      <td>https://www.mercadolivre.com.br/shampoo-esfoli...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Shampoo E Condicionador Sos Hidratação Turbina...</td>
      <td>R$48,99</td>
      <td>https://www.mercadolivre.com.br/shampoo-e-cond...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shampoo Calmante Dercos Sensi Scalp 200ml Vichy</td>
      <td>R$81,97</td>
      <td>https://www.mercadolivre.com.br/shampoo-calman...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Shampoo Tonalizante Color Change Castanho Escu...</td>
      <td>R$29,52</td>
      <td>https://www.mercadolivre.com.br/shampoo-tonali...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Shampoo Lola Morte Súbita Hidratante 250g</td>
      <td>R$16,69</td>
      <td>https://www.mercadolivre.com.br/shampoo-lola-m...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Kit Shampoo + Condicionador Plástica Capilar I...</td>
      <td>R$48,59</td>
      <td>https://www.mercadolivre.com.br/kit-shampoo-co...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Shampoo Pantene Pro-v Brilho Extremo Frasco 400ml</td>
      <td>R$18,35</td>
      <td>https://www.mercadolivre.com.br/shampoo-panten...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Refil Shampoo Dercos Energy+ 200g Vichy</td>
      <td>R$71,17</td>
      <td>https://www.mercadolivre.com.br/refil-shampoo-...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Dove Shampoo Recontrução Completa 670ml</td>
      <td>R$25,67</td>
      <td>https://www.mercadolivre.com.br/dove-shampoo-r...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Progressiva Liso Master Original Azul - Shampo...</td>
      <td>R$309</td>
      <td>https://www.mercadolivre.com.br/progressiva-li...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Shampoo Bambu Nutre &amp; Cresce Pantene 400ml</td>
      <td>R$18,35</td>
      <td>https://www.mercadolivre.com.br/shampoo-bambu-...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Shampoo Reconstrução Completa Dove 400ml</td>
      <td>R$17,39</td>
      <td>https://www.mercadolivre.com.br/shampoo-recons...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Shampoo Anticaspa Clear Limpeza Diária 2 Em 1 ...</td>
      <td>R$23,12</td>
      <td>https://www.mercadolivre.com.br/shampoo-antica...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Shampoo Cetoconazol Prevenção Anticaspa Coceir...</td>
      <td>R$13,35</td>
      <td>https://www.mercadolivre.com.br/shampoo-cetoco...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Shampoo Limpeza Profunda Clear 400ml</td>
      <td>R$21,90</td>
      <td>https://www.mercadolivre.com.br/shampoo-limpez...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Kit Nioxin 2 Shampoo 300ml + Condicionador 300ml</td>
      <td>R$250,80</td>
      <td>https://www.mercadolivre.com.br/kit-nioxin-2-s...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Shampoo Caspiol 100ml</td>
      <td>R$15,93</td>
      <td>https://www.mercadolivre.com.br/shampoo-caspio...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Shampoo Anticaspa Intensivo La Roche-posay Ker...</td>
      <td>R$117</td>
      <td>https://www.mercadolivre.com.br/shampoo-antica...</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Shampoo Recarga Natural Pureza Detox 325ml Seda</td>
      <td>R$9,90</td>
      <td>https://www.mercadolivre.com.br/shampoo-recarg...</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Shampoo Suave Hipoalergênico Antialérgico Aler...</td>
      <td>R$64,20</td>
      <td>https://www.mercadolivre.com.br/shampoo-suave-...</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Shampoo Multibenefícios 1 Litro Pantene</td>
      <td>R$42,90</td>
      <td>https://www.mercadolivre.com.br/shampoo-multib...</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Kit Jubinha Infantil Shampoo Condicionador E C...</td>
      <td>R$123,90</td>
      <td>https://www.mercadolivre.com.br/kit-jubinha-in...</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Truss Shampoo Therapy Controle De Oleosidade 3...</td>
      <td>R$72</td>
      <td>https://www.mercadolivre.com.br/truss-shampoo-...</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Truss Professional Equilibrium Shampoo &amp; Condi...</td>
      <td>R$163,78</td>
      <td>https://www.mercadolivre.com.br/truss-professi...</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Shampoo L'oréal Paris Elseve Glycolic Gloss 400ml</td>
      <td>R$22,77</td>
      <td>https://www.mercadolivre.com.br/shampoo-loreal...</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Shampoo Cazi Caspacil Xampu De 100ml De 100g C...</td>
      <td>R$49,52</td>
      <td>https://www.mercadolivre.com.br/shampoo-cazi-c...</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Shampoo Loreal Professionnel Silver - 300ml</td>
      <td>R$70</td>
      <td>https://www.mercadolivre.com.br/shampoo-loreal...</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Kit Ultra Soft Shampoo 1l E Máscara Pós Químic...</td>
      <td>R$129,90</td>
      <td>https://www.mercadolivre.com.br/kit-ultra-soft...</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Shampoo Purificante Dercos Oil Correction 300g...</td>
      <td>R$79,32</td>
      <td>https://www.mercadolivre.com.br/shampoo-purifi...</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Kit Silver Touch - Shampoo + Condicionador Viz...</td>
      <td>R$138</td>
      <td>https://www.mercadolivre.com.br/kit-silver-tou...</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Farmaervas Shampoo Antiqueda Jaborandi E Vitam...</td>
      <td>R$29,17</td>
      <td>https://www.mercadolivre.com.br/farmaervas-sha...</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Vichy Dercos Shampoo Energy+ 200g</td>
      <td>R$83,25</td>
      <td>https://www.mercadolivre.com.br/vichy-dercos-s...</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Shampoo Anticoceira 650 Ml Head &amp; Shoulders</td>
      <td>R$30,74</td>
      <td>https://www.mercadolivre.com.br/shampoo-antico...</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Kit Linha A Aneethun Shampoo Creme Mascara + E...</td>
      <td>R$251,99</td>
      <td>https://www.mercadolivre.com.br/kit-linha-a-an...</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Redken All Soft  Shampoo - 1000ml New Look Vol...</td>
      <td>R$168,90</td>
      <td>https://www.mercadolivre.com.br/redken-all-sof...</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Kit x2 Shampoo Cetoconazol Prevenção Anticaspa...</td>
      <td>R$33,12</td>
      <td>https://www.mercadolivre.com.br/kit-x2-shampoo...</td>
    </tr>
    <tr>
      <th>45</th>
      <td>La Roche-posay Kerium Shampoo 200ml 200g com 1...</td>
      <td>R$106,48</td>
      <td>https://www.mercadolivre.com.br/la-roche-posay...</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Tio Nacho Kit Engrossador Shampoo 415ml +condi...</td>
      <td>R$45,96</td>
      <td>https://www.mercadolivre.com.br/tio-nacho-kit-...</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Kit Ultra Hydration Plus Shampoo + Condicionad...</td>
      <td>R$172</td>
      <td>https://www.mercadolivre.com.br/kit-ultra-hydr...</td>
    </tr>
  </tbody>
</table>
</div>



## Próximos Passos
- Transformar a classe de scraping em um objeto dinâmico.
- Implementar requisições paralelas.
- Explorar técnicas de automação de navegadores e login automatizado.

## Conclusão
A aula forneceu uma base sólida para iniciar com web scraping em Python, utilizando bibliotecas populares e abordando tanto aspectos técnicos quanto éticos da prática.



```python

```
