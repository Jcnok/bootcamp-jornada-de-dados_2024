# Aula 03 - SQL para Analytics: Join and Having in SQL

## Introdução aos Joins em SQL

Joins em SQL são fundamentais para combinar registros de duas ou mais tabelas em um banco de dados com base em uma condição comum, geralmente uma chave estrangeira. Essa técnica permite que dados relacionados, que são armazenados em tabelas separadas, sejam consultados juntos de forma eficiente e coerente.

Os joins são essenciais para consultar dados complexos e para aplicações em que a normalização do banco de dados resulta em distribuição de informações por diversas tabelas.

Existem vários tipos de joins, cada um com seu uso específico dependendo das necessidades da consulta:

1. **Inner Join**: Retorna registros que têm correspondência em ambas as tabelas.
2. **Left Join (ou Left Outer Join)**: Retorna todos os registros da tabela esquerda e os registros correspondentes da tabela direita. Se não houver correspondência, os resultados da tabela direita terão valores `NULL`.
3. **Right Join (ou Right Outer Join)**: Retorna todos os registros da tabela direita e os registros correspondentes da tabela esquerda. Se não houver correspondência, os resultados da tabela esquerda terão valores `NULL`.
4. **Full Join (ou Full Outer Join)**: Retorna registros quando há uma correspondência em uma das tabelas. Se não houver correspondência, ainda assim, o resultado aparecerá com `NULL` nos campos da tabela sem correspondência.

# Primeiro vamos criar uma conexão com o banco de dados:


```python
import psycopg
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Conectar ao banco de dados PostgreSQL
conn = psycopg.connect("dbname=postgres user=postgres password=password host=172.25.224.1 port=5432")
cursor = conn.cursor()
```

### 1. Criar um relatório para todos os pedidos de 1996 e seus clientes

**Inner Join**

**Uso**: Utilizado quando você precisa de registros que têm correspondência exata em ambas as tabelas.

**Exemplo Prático**: Se quisermos encontrar todos os pedidos de 1996 e os detalhes dos clientes que fizeram esses pedidos, usamos um Inner Join. Isso garante que só obteremos os pedidos que possuem um cliente correspondente e que foram feitos em 1996.


```python
query = '''
SELECT *
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
WHERE DATE_PART('YEAR', o.order_date) = 1996;
'''

pd.read_sql(query, conn)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>order_id</th>
      <th>customer_id</th>
      <th>employee_id</th>
      <th>order_date</th>
      <th>required_date</th>
      <th>shipped_date</th>
      <th>ship_via</th>
      <th>freight</th>
      <th>ship_name</th>
      <th>ship_address</th>
      <th>...</th>
      <th>company_name</th>
      <th>contact_name</th>
      <th>contact_title</th>
      <th>address</th>
      <th>city</th>
      <th>region</th>
      <th>postal_code</th>
      <th>country</th>
      <th>phone</th>
      <th>fax</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10308</td>
      <td>ANATR</td>
      <td>7</td>
      <td>1996-09-18</td>
      <td>1996-10-16</td>
      <td>1996-09-24</td>
      <td>3</td>
      <td>1.61</td>
      <td>Ana Trujillo Emparedados y helados</td>
      <td>Avda. de la Constitución 2222</td>
      <td>...</td>
      <td>Ana Trujillo Emparedados y helados</td>
      <td>Ana Trujillo</td>
      <td>Owner</td>
      <td>Avda. de la Constitución 2222</td>
      <td>México D.F.</td>
      <td>None</td>
      <td>05021</td>
      <td>Mexico</td>
      <td>(5) 555-4729</td>
      <td>(5) 555-3745</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10365</td>
      <td>ANTON</td>
      <td>3</td>
      <td>1996-11-27</td>
      <td>1996-12-25</td>
      <td>1996-12-02</td>
      <td>2</td>
      <td>22.00</td>
      <td>Antonio Moreno Taquería</td>
      <td>Mataderos  2312</td>
      <td>...</td>
      <td>Antonio Moreno Taquería</td>
      <td>Antonio Moreno</td>
      <td>Owner</td>
      <td>Mataderos  2312</td>
      <td>México D.F.</td>
      <td>None</td>
      <td>05023</td>
      <td>Mexico</td>
      <td>(5) 555-3932</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10383</td>
      <td>AROUT</td>
      <td>8</td>
      <td>1996-12-16</td>
      <td>1997-01-13</td>
      <td>1996-12-18</td>
      <td>3</td>
      <td>34.24</td>
      <td>Around the Horn</td>
      <td>Brook Farm Stratford St. Mary</td>
      <td>...</td>
      <td>Around the Horn</td>
      <td>Thomas Hardy</td>
      <td>Sales Representative</td>
      <td>120 Hanover Sq.</td>
      <td>London</td>
      <td>None</td>
      <td>WA1 1DP</td>
      <td>UK</td>
      <td>(171) 555-7788</td>
      <td>(171) 555-6750</td>
    </tr>
    <tr>
      <th>3</th>
      <td>10355</td>
      <td>AROUT</td>
      <td>6</td>
      <td>1996-11-15</td>
      <td>1996-12-13</td>
      <td>1996-11-20</td>
      <td>1</td>
      <td>41.95</td>
      <td>Around the Horn</td>
      <td>Brook Farm Stratford St. Mary</td>
      <td>...</td>
      <td>Around the Horn</td>
      <td>Thomas Hardy</td>
      <td>Sales Representative</td>
      <td>120 Hanover Sq.</td>
      <td>London</td>
      <td>None</td>
      <td>WA1 1DP</td>
      <td>UK</td>
      <td>(171) 555-7788</td>
      <td>(171) 555-6750</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10384</td>
      <td>BERGS</td>
      <td>3</td>
      <td>1996-12-16</td>
      <td>1997-01-13</td>
      <td>1996-12-20</td>
      <td>3</td>
      <td>168.64</td>
      <td>Berglunds snabbköp</td>
      <td>Berguvsvägen  8</td>
      <td>...</td>
      <td>Berglunds snabbköp</td>
      <td>Christina Berglund</td>
      <td>Order Administrator</td>
      <td>Berguvsvägen  8</td>
      <td>Luleå</td>
      <td>None</td>
      <td>S-958 22</td>
      <td>Sweden</td>
      <td>0921-12 34 65</td>
      <td>0921-12 34 67</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>147</th>
      <td>10266</td>
      <td>WARTH</td>
      <td>3</td>
      <td>1996-07-26</td>
      <td>1996-09-06</td>
      <td>1996-07-31</td>
      <td>3</td>
      <td>25.73</td>
      <td>Wartian Herkku</td>
      <td>Torikatu 38</td>
      <td>...</td>
      <td>Wartian Herkku</td>
      <td>Pirkko Koskitalo</td>
      <td>Accounting Manager</td>
      <td>Torikatu 38</td>
      <td>Oulu</td>
      <td>None</td>
      <td>90110</td>
      <td>Finland</td>
      <td>981-443655</td>
      <td>981-443655</td>
    </tr>
    <tr>
      <th>148</th>
      <td>10256</td>
      <td>WELLI</td>
      <td>3</td>
      <td>1996-07-15</td>
      <td>1996-08-12</td>
      <td>1996-07-17</td>
      <td>2</td>
      <td>13.97</td>
      <td>Wellington Importadora</td>
      <td>Rua do Mercado, 12</td>
      <td>...</td>
      <td>Wellington Importadora</td>
      <td>Paula Parente</td>
      <td>Sales Manager</td>
      <td>Rua do Mercado, 12</td>
      <td>Resende</td>
      <td>SP</td>
      <td>08737-363</td>
      <td>Brazil</td>
      <td>(14) 555-8122</td>
      <td>None</td>
    </tr>
    <tr>
      <th>149</th>
      <td>10344</td>
      <td>WHITC</td>
      <td>4</td>
      <td>1996-11-01</td>
      <td>1996-11-29</td>
      <td>1996-11-05</td>
      <td>2</td>
      <td>23.29</td>
      <td>White Clover Markets</td>
      <td>1029 - 12th Ave. S.</td>
      <td>...</td>
      <td>White Clover Markets</td>
      <td>Karl Jablonski</td>
      <td>Owner</td>
      <td>305 - 14th Ave. S. Suite 3B</td>
      <td>Seattle</td>
      <td>WA</td>
      <td>98128</td>
      <td>USA</td>
      <td>(206) 555-4112</td>
      <td>(206) 555-4115</td>
    </tr>
    <tr>
      <th>150</th>
      <td>10269</td>
      <td>WHITC</td>
      <td>5</td>
      <td>1996-07-31</td>
      <td>1996-08-14</td>
      <td>1996-08-09</td>
      <td>1</td>
      <td>4.56</td>
      <td>White Clover Markets</td>
      <td>1029 - 12th Ave. S.</td>
      <td>...</td>
      <td>White Clover Markets</td>
      <td>Karl Jablonski</td>
      <td>Owner</td>
      <td>305 - 14th Ave. S. Suite 3B</td>
      <td>Seattle</td>
      <td>WA</td>
      <td>98128</td>
      <td>USA</td>
      <td>(206) 555-4112</td>
      <td>(206) 555-4115</td>
    </tr>
    <tr>
      <th>151</th>
      <td>10374</td>
      <td>WOLZA</td>
      <td>1</td>
      <td>1996-12-05</td>
      <td>1997-01-02</td>
      <td>1996-12-09</td>
      <td>3</td>
      <td>3.94</td>
      <td>Wolski Zajazd</td>
      <td>ul. Filtrowa 68</td>
      <td>...</td>
      <td>Wolski  Zajazd</td>
      <td>Zbyszek Piestrzeniewicz</td>
      <td>Owner</td>
      <td>ul. Filtrowa 68</td>
      <td>Warszawa</td>
      <td>None</td>
      <td>01-012</td>
      <td>Poland</td>
      <td>(26) 642-7012</td>
      <td>(26) 642-7012</td>
    </tr>
  </tbody>
</table>
<p>152 rows × 25 columns</p>
</div>



**Vantagens:**

* **`DATE_PART` para extrair o ano:**  Em vez de usar `BETWEEN` para definir um intervalo de datas,  `DATE_PART('YEAR', o.order_date)` extrai apenas o ano da coluna `order_date`, tornando a consulta mais concisa.
* **Comparação direta:** O comando `WHERE DATE_PART('YEAR', o.order_date) = 1996` é mais simples e direto do que o `BETWEEN` usado no meu exemplo anterior.

**Observações:**

* `DATE_PART` é uma função específica do PostgreSQL. Se você estiver usando outro SGBD, como MySQL ou SQL Server, precisará usar uma função equivalente para extrair o ano da data.
* `SELECT *` irá retornar todas as colunas das duas tabelas. Se você quiser retornar apenas colunas específicas, liste-as na cláusula `SELECT` como no meu primeiro exemplo.

### 2. Criar um relatório que mostra o número de funcionários e clientes de cada cidade que tem funcionários

**Left Join**

**Uso**: Usado quando você quer todos os registros da primeira (esquerda) tabela, com os correspondentes da segunda (direita) tabela. Se não houver correspondência, a segunda tabela terá campos `NULL`.

**Exemplo Prático**: Se precisarmos listar todas as cidades onde temos funcionários, e também queremos saber quantos clientes temos nessas cidades, mesmo que não haja clientes, usamos um Left Join.



```python
query = '''
-- Cria um relatório que mostra o número de funcionários e clientes de cada cidade que tem funcionários (5 linhas)
SELECT e.city AS cidade,
       COUNT(DISTINCT e.employee_id) AS numero_de_funcionarios,
       COUNT(DISTINCT c.customer_id) AS numero_de_clientes
FROM employees e
LEFT JOIN customers c ON e.city = c.city
GROUP BY e.city
ORDER BY cidade;
'''
pd.read_sql(query, conn)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cidade</th>
      <th>numero_de_funcionarios</th>
      <th>numero_de_clientes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kirkland</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>London</td>
      <td>4</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Redmond</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Seattle</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Tacoma</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



### Descrição da Tabela

* **cidade**: O nome da cidade onde os funcionários e clientes estão localizados.
* **numero_de_funcionarios**: Contagem dos funcionários distintos nessa cidade. Este número vem diretamente da tabela `employees`.
* **numero_de_clientes**: Contagem dos clientes distintos que têm a mesma cidade que os funcionários. Se não houver clientes em uma cidade onde há funcionários, o número será 0.

### Explicação Detalhada

* **Kirkland**: Tem um equilíbrio entre o número de funcionários e clientes, com ambos os valores sendo 1. Isso indica uma correspondência direta entre locais de funcionários e clientes.
* **London**: Apresenta uma maior concentração tanto de funcionários quanto de clientes, com mais clientes (6) do que funcionários (4), indicando uma forte presença de ambos na cidade.
* **Redmond**: Tem 1 funcionário, mas nenhum cliente registrado nesta cidade, sugerindo que, embora a empresa tenha presença laboral aqui, não há clientes registrados.
* **Seattle**: Tem 2 funcionários e apenas 1 cliente, mostrando uma presença menor de clientes em relação aos funcionários.
* **Tacoma**: Similar a Redmond, tem funcionários (1) mas nenhum cliente, o que pode indicar uma área onde a empresa opera, mas ainda não estabeleceu uma base de clientes.

Essa análise é particularmente útil para entender como os recursos humanos da empresa (funcionários) estão distribuídos em relação à sua base de clientes em diferentes locais. Isso pode ajudar a identificar cidades onde a empresa pode precisar intensificar esforços de aquisição de clientes ou avaliar a eficácia de suas operações e estratégias de mercado locais.

### 3. Criar um relatório que mostra o número de funcionários e clientes de cada cidade que tem clientes

**Right Join**

**Uso**: É o inverso do Left Join e é menos comum. Usado quando queremos todos os registros da segunda (direita) tabela e os correspondentes da primeira (esquerda) tabela.

**Exemplo Prático**: Para listar todas as cidades onde temos clientes, e também contar quantos funcionários temos nessas cidades, usamos um Right Join.


```python
query = '''
-- Cria um relatório que mostra o número de funcionários e clientes de cada cidade que tem clientes (69 linhas)
SELECT c.city AS cidade,
       COUNT(DISTINCT c.customer_id) AS numero_de_clientes,
       COUNT(DISTINCT e.employee_id) AS numero_de_funcionarios
FROM employees e
RIGHT JOIN customers c ON e.city = c.city
GROUP BY c.city
ORDER BY cidade;
'''
pd.read_sql(query, conn)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cidade</th>
      <th>numero_de_clientes</th>
      <th>numero_de_funcionarios</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Aachen</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albuquerque</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Anchorage</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Århus</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Barcelona</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>64</th>
      <td>Tsawassen</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Vancouver</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>66</th>
      <td>Versailles</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>67</th>
      <td>Walla Walla</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>68</th>
      <td>Warszawa</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>69 rows × 3 columns</p>
</div>



### Diferenças Principais do `RIGHT JOIN`

1. **Foco na Tabela à Direita**: Ao contrário do `LEFT JOIN` que foca na tabela à esquerda, o `RIGHT JOIN` garante que todos os registros da tabela à direita (neste caso, `customers`) estejam presentes no resultado. Se não houver correspondência na tabela à esquerda (`employees`), as colunas relacionadas desta tabela aparecerão como `NULL`.

2. **Exibição de Dados Não Correspondentes**: Como mostrado, o `RIGHT JOIN` pode exibir linhas onde não há correspondência na tabela à esquerda, o que é útil para identificar dados que estão apenas na tabela à direita. No contexto de um negócio, isso pode destacar áreas (ou dados) que requerem atenção, como clientes em locais onde a empresa não tem funcionários representados.

3. **Utilização Estratégica para Análise de Dados**: O `RIGHT JOIN` é menos comum que o `LEFT JOIN` porque muitas vezes as tabelas são organizadas de modo que a tabela mais importante (ou abrangente) seja colocada à esquerda da consulta. No entanto, o `RIGHT JOIN` é útil quando a tabela à direita é prioritária e queremos garantir que todos os seus registros sejam analisados.

### 4. Criar um relatório que mostra o número de funcionários e clientes de cada cidade

* **Análise Completa de Dados**: O `FULL JOIN` é útil quando você precisa de uma visão completa dos dados em duas tabelas relacionadas, especialmente para identificar onde os dados estão faltando em uma ou ambas as tabelas.
* **Relatórios Abrangentes**: Permite criar relatórios que mostram todas as possíveis relações entre duas tabelas, incluindo onde as relações não existem.
* **Análise de Lacunas de Dados**: Ajuda a identificar lacunas nos dados de ambas as tabelas simultaneamente, facilitando análises de cobertura e consistência entre conjuntos de dados.

**Full Join**

**Uso**: Utilizado quando queremos a união de Left Join e Right Join, mostrando todos os registros de ambas as tabelas, e preenchendo com `NULL` onde não há correspondência.

**Exemplo Prático**: Para listar todas as cidades onde temos clientes ou funcionários, e contar ambos em cada cidade, usamos um Full Join.


```python
query = '''
-- Cria um relatório que mostra o número de funcionários e clientes de cada cidade (71 linhas)
SELECT
	COALESCE(e.city, c.city) AS cidade,
	COUNT(DISTINCT e.employee_id) AS numero_de_funcionarios,
	COUNT(DISTINCT c.customer_id) AS numero_de_clientes
FROM employees e
FULL JOIN customers c ON e.city = c.city
GROUP BY e.city, c.city
ORDER BY cidade;
'''
pd.read_sql(query, conn)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cidade</th>
      <th>numero_de_funcionarios</th>
      <th>numero_de_clientes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Aachen</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albuquerque</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Anchorage</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Århus</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Barcelona</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>66</th>
      <td>Tsawassen</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>67</th>
      <td>Vancouver</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>68</th>
      <td>Versailles</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Walla Walla</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>70</th>
      <td>Warszawa</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>71 rows × 3 columns</p>
</div>



Esta consulta retorna uma lista de todas as cidades conhecidas por ambas as tabelas, junto com a contagem de funcionários e clientes em cada cidade. Aqui estão alguns cenários possíveis no resultado:

### Análise do Resultado

O resultado do `FULL JOIN` mostra:

* A maioria das cidades listadas tem clientes, mas não funcionários (indicado por "0" no número de funcionários).
* Em algumas cidades, como "Kirkland", "Redmond", "Seattle", e "Tacoma", há funcionários e/ou clientes, mostrando correspondência direta entre as tabelas.
* Notavelmente, em cidades como "London" e "Madrid", o número de clientes é significativamente maior do que o de funcionários, o que pode indicar centros de alta atividade de clientes sem uma proporção correspondente de suporte de funcionários.

### Observações Importantes

1. **Cidades com apenas Clientes**: A maioria das cidades no resultado possui clientes, mas não funcionários. Isso pode sugerir que a empresa tem uma ampla base de clientes geograficamente, mas uma distribuição mais limitada de sua força de trabalho.

2. **Cidades com Funcionários e sem Clientes**: Cidades como "Redmond" e "Tacoma" têm funcionários, mas nenhuma contagem de clientes listada, indicando que há operações da empresa sem correspondente atividade de clientes registrada nesses locais.

3. **Concentrações de Clientes e Funcionários**: Em cidades como "London", "Seattle", e "Sao Paulo", há uma concentração significativa de clientes e alguma presença de funcionários, sugerindo centros operacionais ou mercados importantes para a empresa.

4. **Ausência de Dados em Algumas Cidades**: Algumas cidades têm zero funcionários e clientes, indicando que pode haver um erro de dados, cidades listadas incorretamente, ou simplesmente que não há atividade de funcionários ou clientes registrados nesses locais.


### Implicações Estratégicas

A partir desses dados, a empresa poderia considerar várias ações estratégicas:

* **Expansão de Funcionários**: Investir em recursos humanos nas cidades com altos números de clientes, mas baixa presença de funcionários, para melhorar o suporte e a satisfação do cliente.

* **Análise de Mercado**: Realizar uma análise mais aprofundada sobre por que certas cidades têm alta atividade de clientes e ajustar as estratégias de marketing e vendas conforme necessário.

* **Revisão de Dados**: Verificar a precisão dos dados para entender melhor as discrepâncias ou ausências nas contagens de funcionários e clientes.

Este exemplo realça o valor de usar `FULL JOIN` para obter uma visão completa da relação entre duas variáveis críticas (funcionários e clientes) e como essa informação pode ser usada para insights estratégicos.

## Having

### 1. Criar um relatório que mostra a quantidade total de produtos (da tabela order_details)


```python
query = '''
-- Cria um relatório que mostra a quantidade total de produtos encomendados.
-- Mostra apenas registros para produtos para os quais a quantidade encomendada é menor que 200 (5 linhas)
SELECT o.product_id, p.product_name, SUM(o.quantity) AS quantidade_total
FROM order_details o
JOIN products p ON p.product_id = o.product_id
GROUP BY o.product_id, p.product_name
HAVING SUM(o.quantity) < 200
ORDER BY quantidade_total DESC;
'''
pd.read_sql(query, conn)

```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>product_id</th>
      <th>product_name</th>
      <th>quantidade_total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>67</td>
      <td>Laughing Lumberjack Lager</td>
      <td>184</td>
    </tr>
    <tr>
      <th>1</th>
      <td>48</td>
      <td>Chocolade</td>
      <td>138</td>
    </tr>
    <tr>
      <th>2</th>
      <td>37</td>
      <td>Gravad lax</td>
      <td>125</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>Genen Shouyu</td>
      <td>122</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9</td>
      <td>Mishi Kobe Niku</td>
      <td>95</td>
    </tr>
  </tbody>
</table>
</div>



### 2. Criar um relatório que mostra o total de pedidos por cliente desde 31 de dezembro de 1996


```python
query = '''
-- Cria um relatório que mostra o total de pedidos por cliente desde 31 de dezembro de 1996.
SELECT customer_id, COUNT(order_id) AS total_de_pedidos
FROM orders
WHERE order_date > '1996-12-31'
GROUP BY customer_id
HAVING COUNT(order_id) > 15
ORDER BY total_de_pedidos;
'''
pd.read_sql(query, conn)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>customer_id</th>
      <th>total_de_pedidos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>FOLKO</td>
      <td>16</td>
    </tr>
    <tr>
      <th>1</th>
      <td>HILAA</td>
      <td>16</td>
    </tr>
    <tr>
      <th>2</th>
      <td>QUICK</td>
      <td>22</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ERNSH</td>
      <td>24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>SAVEA</td>
      <td>28</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

### Explicação das Consultas Convertidas

**Consulta 1:**

* **Seleção e Junção**: A consulta seleciona o `product_id` e `product_name` da tabela `products` e junta com a tabela `order_details` pelo `product_id`.
* **Agrupamento e Filtragem**: Os dados são agrupados por `product_id` e `product_name`, e a função agregada `SUM(o.quantity)` calcula a quantidade total de cada produto encomendado. A cláusula `HAVING` é usada para filtrar produtos cuja quantidade total encomendada é menor que 200.

**Consulta 2:**

* **Filtragem de Data**: A consulta filtra os pedidos realizados após 31 de dezembro de 1996.
* **Agrupamento e Contagem**: Agrupa os pedidos pelo `customer_id` e conta o número de pedidos feitos por cada cliente usando `COUNT(order_id)`.
* **Filtragem de Resultados**: Utiliza a cláusula `HAVING` para incluir apenas os clientes que fizeram mais de 15 pedidos desde a data especificada.


```python

```
