#



Aula 02 - SQL para Analytics: Nossas primeiras consultas

## Objetivo

Realizar nossas primeiras consultas no banco Northwind

## Uma tangente antes de realizarmos nossas primeiras consultas

SQL, ou Structured Query Language, é uma linguagem de programação projetada para gerenciar dados armazenados em um sistema de gerenciamento de banco de dados relacional (RDBMS). SQL possui vários componentes, cada um responsável por diferentes tipos de tarefas e operações que podem ser executadas em um banco de dados. Esses componentes incluem DDL, DML, DCL, e DQL, entre outros. Aqui está um resumo de cada um deles:

Cada componente da linguagem SQL tem um papel fundamental na gestão e no uso de bancos de dados, e diferentes tipos de profissionais de tecnologia podem utilizar esses comandos para desempenhar suas funções específicas. Vamos detalhar quem geralmente é responsável por cada tipo de comando e qual o objetivo de cada um dos componentes mencionados (DDL, DML, DQL, DCL, TCL):

### 1. DDL (Data Definition Language)

O DDL ou Linguagem de Definição de Dados é usado para definir e modificar a estrutura do banco de dados e seus objetos, como tabelas, índices, restrições, esquemas, entre outros. Comandos DDL incluem:

* **CREATE**: Usado para criar novos objetos no banco de dados, como tabelas, índices, funções, vistas, triggers, etc.
* **ALTER**: Modifica a estrutura de um objeto existente no banco de dados, por exemplo, adicionando uma coluna a uma tabela ou alterando características de uma coluna existente.
* **DROP**: Remove objetos do banco de dados.
* **TRUNCATE**: Remove todos os registros de uma tabela, liberando o espaço ocupado por esses registros.

* **Responsável**: Administradores de banco de dados (DBAs) e desenvolvedores de banco de dados.
* **Objetivo**: O DDL é usado para criar e modificar a estrutura do banco de dados e de seus objetos. Esses comandos ajudam a definir como os dados são organizados, armazenados, e como as relações entre eles são estabelecidas. Eles são essenciais durante a fase de design do banco de dados e quando são necessárias mudanças na estrutura.

### 2. DML (Data Manipulation Language)

O DML ou Linguagem de Manipulação de Dados é usado para gerenciar dados dentro dos objetos (como tabelas). Inclui comandos para inserir, modificar e deletar dados:

* **INSERT**: Insere dados em uma tabela.
* **UPDATE**: Altera dados existentes em uma tabela.
* **DELETE**: Remove dados de uma tabela.
* **MERGE**: Uma operação que permite inserir, atualizar ou deletar registros em uma tabela com base em um conjunto de condições determinadas.

* **Responsável**: Desenvolvedores de software, analistas de dados e, ocasionalmente, usuários finais através de interfaces que executam comandos DML por trás dos panos.
* **Objetivo**: O DML é crucial para o gerenciamento dos dados dentro das tabelas. Ele é utilizado para inserir, atualizar, deletar e manipular dados armazenados. Analistas de dados podem usar DML para preparar conjuntos de dados para análise, enquanto os desenvolvedores o utilizam para implementar a lógica de negócios.

### 3. DQL (Data Query Language)

O DQL ou Linguagem de Consulta de Dados é fundamentalmente usado para realizar consultas nos dados. O comando mais conhecido na DQL é o **SELECT**, que é utilizado para recuperar dados de uma ou mais tabelas.

* **Responsável**: Analistas de dados, cientistas de dados, e qualquer usuário que necessite extrair informações do banco de dados.
* **Objetivo**: O DQL é usado para consultar e recuperar dados. É fundamental para gerar relatórios, realizar análises, e fornecer dados que ajudem na tomada de decisões. O comando `SELECT`, parte do DQL, é um dos mais usados e é essencial para qualquer tarefa que requer visualização ou análise de dados.

### 4. DCL (Data Control Language)

O DCL ou Linguagem de Controle de Dados inclui comandos relacionados à segurança na acessibilidade dos dados no banco de dados. Isso envolve comandos para conceder e revogar permissões de acesso:

* **GRANT**: Concede permissões de acesso aos usuários.
* **REVOKE**: Remove permissões de acesso.

* **Responsável**: Administradores de banco de dados.
* **Objetivo**: O DCL é usado para configurar permissões em um banco de dados, garantindo que apenas usuários autorizados possam acessar, modificar, ou administrar os dados. Isso é crucial para a segurança e a governança de dados, protegendo informações sensíveis e mantendo a integridade do sistema.

### 5. TCL (Transaction Control Language)

O TCL ou Linguagem de Controle de Transação é usado para gerenciar transações no banco de dados. Transações são importantes para manter a integridade dos dados e garantir que operações múltiplas sejam concluídas com sucesso ou não sejam realizadas de todo:

* **COMMIT**: Confirma uma transação, tornando todas as mudanças permanentes no banco de dados.
* **ROLLBACK**: Desfaz todas as mudanças feitas durante a transação atual.
* **SAVEPOINT**: Define um ponto na transação que pode ser usado para um rollback parcial.

* **Responsável**: Desenvolvedores de software e administradores de banco de dados.
* **Objetivo**: O TCL é usado para gerenciar transações no banco de dados, garantindo que as operações sejam completadas com sucesso ou revertidas em caso de erro. Isso é essencial para manter a consistência e integridade dos dados, especialmente em ambientes onde múltiplas transações ocorrem simultaneamente.

Essa separação de responsabilidades ajuda a manter a organização e eficiência das operações do banco de dados, além de garantir que as ações executadas em um ambiente de banco de dados sejam seguras e alinhadas com as necessidades da organização.

## Se olharmos os comandos que fizemos ontem...

1) Esse comando é de qual subconjunto?
   * R: **DQL**

```sql
SELECT * FROM customers WHERE country='Mexico';
```

2) Esse comando é de qual subconjunto?
   * R: **DML**

```sql
INSERT INTO customers VALUES ('ALFKI', 'Alfreds Futterkiste', 'Maria Anders', 'Sales Representative', 'Obere Str. 57', 'Berlin', NULL, '12209', 'Germany', '030-0074321', '030-0076545');
INSERT INTO customers VALUES ('ANATR', 'Ana Trujillo Emparedados y helados', 'Ana Trujillo', 'Owner', 'Avda. de la Constitución 2222', 'México D.F.', NULL, '05021', 'Mexico', '(5) 555-4729', '(5) 555-3745');
INSERT INTO customers VALUES ('ANTON', 'Antonio Moreno Taquería', 'Antonio Moreno', 'Owner', 'Mataderos  2312', 'México D.F.', NULL, '05023', 'Mexico', '(5) 555-3932', NULL);
INSERT INTO customers VALUES ('AROUT', 'Around the Horn', 'Thomas Hardy', 'Sales Representative', '120 Hanover Sq.', 'London', NULL, 'WA1 1DP', 'UK', '(171) 555-7788', '(171) 555-6750');
INSERT INTO customers VALUES ('BERGS', 'Berglunds snabbköp', 'Christina Berglund', 'Order Administrator', 'Berguvsvägen  8', 'Luleå', NULL, 'S-958 22', 'Sweden', '0921-12 34 65', '0921-12 34 67');
```

3) Esse comando é de qual subconjunto?
   * R: **DDL**

```sql
CREATE TABLE suppliers (
    supplier_id smallint NOT NULL,
    company_name character varying(40) NOT NULL,
    contact_name character varying(30),
    contact_title character varying(30),
    address character varying(60),
    city character varying(15),
    region character varying(15),
    postal_code character varying(10),
    country character varying(15),
    phone character varying(24),
    fax character varying(24),
    homepage text
);
```

4) Esse comando é de qual subconjunto?
   * R: **TCL**

```sql
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
```

## Agora vamos para nossas primeiras QUERY? (Data Query Language)

## Primeiro vamos criar uma conexão com o banco de dados:


```python
import psycopg
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Conectar ao banco de dados PostgreSQL
conn = psycopg.connect("dbname=postgres user=postgres password=password host=172.25.224.1 port=5432")
cursor = conn.cursor()
```

### Pronto agora vamos praticar um pouco.

Data Query Language (DQL) é um subconjunto da linguagem SQL (Structured Query Language) utilizado especificamente para consultar dados em bancos de dados. DQL é fundamental para extrair informações, realizar análises e gerar relatórios a partir dos dados armazenados em um sistema de gerenciamento de banco de dados relacional (RDBMS). O principal comando em DQL é o `SELECT`, que é amplamente utilizado para selecionar dados de uma ou mais tabelas.

**Objetivos da DQL**

O principal objetivo da DQL é permitir que usuários e aplicações recuperem dados de forma eficiente e precisa de um banco de dados. DQL proporciona a flexibilidade para especificar exatamente quais dados são necessários, como devem ser filtrados, agrupados, ordenados e transformados. Isso torna a DQL uma ferramenta essencial para:

* **Análise de dados**: Extrair conjuntos de dados para análise e tomada de decisão baseada em evidências.
* **Geração de relatórios**: Criar relatórios detalhados que ajudam as organizações a entender o desempenho operacional e estratégico.
* **Visualização de dados**: Alimentar ferramentas de visualização com dados que ajudam a representar informações complexas de maneira compreensível.
* **Auditoria e monitoramento**: Acompanhar e revisar operações e transações para conformidade e segurança.

**Como começar com DQL**

Para começar a usar DQL, é essencial ter um conhecimento básico de SQL e entender a estrutura dos dados dentro do banco de dados com o qual você está trabalhando. Aqui estão alguns passos para começar:

1. **Entenda o esquema do banco de dados**: Conheça as tabelas, colunas, tipos de dados e relações entre as tabelas.
2. **Aprenda os fundamentos do comando `SELECT`**: Comece com consultas simples para selecionar colunas específicas de uma tabela.
3. **Use cláusulas para refinar suas consultas**:
    * **WHERE**: Para filtrar registros.
    * **GROUP BY**: Para agrupar registros.
    * **HAVING**: Para filtrar grupos.
    * **ORDER BY**: Para ordenar os resultados.
4. **Pratique com dados de exemplo**: Use um banco de dados de exemplo para praticar suas consultas e testar diferentes cenários.

**Principais comandos da DQL**

* **SELECT**: O comando mais fundamental em DQL, usado para selecionar dados de uma ou mais tabelas.

    ```sql
    SELECT * FROM customers;
    select contact_name, city from customers;
    ```


```python
# executando a query
query = '''SELECT * FROM customers limit 5;'''
pd.read_sql(query, con=conn)
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
      <th>customer_id</th>
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
      <td>ALFKI</td>
      <td>Alfreds Futterkiste</td>
      <td>Maria Anders</td>
      <td>Sales Representative</td>
      <td>Obere Str. 57</td>
      <td>Berlin</td>
      <td>None</td>
      <td>12209</td>
      <td>Germany</td>
      <td>030-0074321</td>
      <td>030-0076545</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ANATR</td>
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
      <th>2</th>
      <td>ANTON</td>
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
      <th>3</th>
      <td>AROUT</td>
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
      <td>BERGS</td>
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
  </tbody>
</table>
</div>



* **DISTINCT**: Usado com `SELECT` para retornar apenas valores distintos.

    ```sql
    select country from customers;
    select distinct country from customers;
    select count(distinct country) from customers;
    ```


```python
# Executando uma query com distinct
query = '''SELECT COUNT(DISTINCT country) as "Total de Países distintintos" FROM customers;'''
pd.read_sql(query, conn,index_col="Total de Países distintintos")
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
    </tr>
    <tr>
      <th>Total de Países distintintos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>21</th>
    </tr>
  </tbody>
</table>
</div>



* **WHERE**: Usado para filtrar.

```sql
-- Seleciona todos os clientes do México
SELECT * FROM customers WHERE country='Mexico';
-- Seleciona clientes com ID específico
SELECT * FROM customers WHERE customer_id='ANATR';
-- Utiliza AND para múltiplos critérios
SELECT * FROM customers WHERE country='Germany' AND city='Berlin';
-- Utiliza OR para mais de uma cidade
SELECT * FROM customers WHERE city='Berlin' OR city='Aachen';
-- Utiliza NOT para excluir a Alemanha
SELECT * FROM customers WHERE country<>'Germany';
-- Combina AND, OR e NOT
SELECT * FROM customers WHERE country='Germany' AND (city='Berlin' OR city='Aachen');
-- Exclui clientes da Alemanha e EUA
SELECT * FROM customers WHERE country<>'Germany' AND country<>'USA';
```


```python
#Seleciona todos os clientes do México
q1 = "SELECT * FROM customers WHERE country='Mexico';"
#Seleciona clientes com ID específico
q2 = "SELECT * FROM customers WHERE customer_id='ANATR';"
# Utiliza AND para múltiplos critérios
q3 = "SELECT * FROM customers WHERE country='Germany' AND city='Berlin';"
# Utiliza OR para mais de uma cidade
q4 = "SELECT * FROM customers WHERE city='Berlin' OR city='Aachen';"
# Utiliza NOT para excluir a Alemanha
q5 = "SELECT * FROM customers WHERE country<>'Germany' LIMIT 5;"
# Combina AND, OR e NOT
q6 = "SELECT * FROM customers WHERE country='Germany' AND (city='Berlin' OR city='Aachen');"
# Exclui clientes da Alemanha e EUA
q7 = "SELECT * FROM customers WHERE country<>'Germany' AND country<>'USA' LIMIT 5"
queries = [q1,q2,q3,q4,q5,q6,q7]
# Executando todas as queries.
for query in queries:
    print(100 * "=")
    print(f"Resultado da query:{query}")
    print(100 * "=")
    display(pd.read_sql(query,conn))
```

    ====================================================================================================
    Resultado da query:SELECT * FROM customers WHERE country='Mexico';
    ====================================================================================================



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
      <th>customer_id</th>
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
      <td>ANATR</td>
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
      <td>ANTON</td>
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
      <td>CENTC</td>
      <td>Centro comercial Moctezuma</td>
      <td>Francisco Chang</td>
      <td>Marketing Manager</td>
      <td>Sierras de Granada 9993</td>
      <td>México D.F.</td>
      <td>None</td>
      <td>05022</td>
      <td>Mexico</td>
      <td>(5) 555-3392</td>
      <td>(5) 555-7293</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PERIC</td>
      <td>Pericles Comidas clásicas</td>
      <td>Guillermo Fernández</td>
      <td>Sales Representative</td>
      <td>Calle Dr. Jorge Cash 321</td>
      <td>México D.F.</td>
      <td>None</td>
      <td>05033</td>
      <td>Mexico</td>
      <td>(5) 552-3745</td>
      <td>(5) 545-3745</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TORTU</td>
      <td>Tortuga Restaurante</td>
      <td>Miguel Angel Paolino</td>
      <td>Owner</td>
      <td>Avda. Azteca 123</td>
      <td>México D.F.</td>
      <td>None</td>
      <td>05033</td>
      <td>Mexico</td>
      <td>(5) 555-2933</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:SELECT * FROM customers WHERE customer_id='ANATR';
    ====================================================================================================



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
      <th>customer_id</th>
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
      <td>ANATR</td>
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
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:SELECT * FROM customers WHERE country='Germany' AND city='Berlin';
    ====================================================================================================



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
      <th>customer_id</th>
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
      <td>ALFKI</td>
      <td>Alfreds Futterkiste</td>
      <td>Maria Anders</td>
      <td>Sales Representative</td>
      <td>Obere Str. 57</td>
      <td>Berlin</td>
      <td>None</td>
      <td>12209</td>
      <td>Germany</td>
      <td>030-0074321</td>
      <td>030-0076545</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:SELECT * FROM customers WHERE city='Berlin' OR city='Aachen';
    ====================================================================================================



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
      <th>customer_id</th>
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
      <td>ALFKI</td>
      <td>Alfreds Futterkiste</td>
      <td>Maria Anders</td>
      <td>Sales Representative</td>
      <td>Obere Str. 57</td>
      <td>Berlin</td>
      <td>None</td>
      <td>12209</td>
      <td>Germany</td>
      <td>030-0074321</td>
      <td>030-0076545</td>
    </tr>
    <tr>
      <th>1</th>
      <td>DRACD</td>
      <td>Drachenblut Delikatessen</td>
      <td>Sven Ottlieb</td>
      <td>Order Administrator</td>
      <td>Walserweg 21</td>
      <td>Aachen</td>
      <td>None</td>
      <td>52066</td>
      <td>Germany</td>
      <td>0241-039123</td>
      <td>0241-059428</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:SELECT * FROM customers WHERE country<>'Germany' LIMIT 5;
    ====================================================================================================



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
      <th>customer_id</th>
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
      <td>ANATR</td>
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
      <td>ANTON</td>
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
      <td>AROUT</td>
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
      <td>BERGS</td>
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
      <th>4</th>
      <td>BLONP</td>
      <td>Blondesddsl père et fils</td>
      <td>Frédérique Citeaux</td>
      <td>Marketing Manager</td>
      <td>24, place Kléber</td>
      <td>Strasbourg</td>
      <td>None</td>
      <td>67000</td>
      <td>France</td>
      <td>88.60.15.31</td>
      <td>88.60.15.32</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:SELECT * FROM customers WHERE country='Germany' AND (city='Berlin' OR city='Aachen');
    ====================================================================================================



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
      <th>customer_id</th>
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
      <td>ALFKI</td>
      <td>Alfreds Futterkiste</td>
      <td>Maria Anders</td>
      <td>Sales Representative</td>
      <td>Obere Str. 57</td>
      <td>Berlin</td>
      <td>None</td>
      <td>12209</td>
      <td>Germany</td>
      <td>030-0074321</td>
      <td>030-0076545</td>
    </tr>
    <tr>
      <th>1</th>
      <td>DRACD</td>
      <td>Drachenblut Delikatessen</td>
      <td>Sven Ottlieb</td>
      <td>Order Administrator</td>
      <td>Walserweg 21</td>
      <td>Aachen</td>
      <td>None</td>
      <td>52066</td>
      <td>Germany</td>
      <td>0241-039123</td>
      <td>0241-059428</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:SELECT * FROM customers WHERE country<>'Germany' AND country<>'USA' LIMIT 5
    ====================================================================================================



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
      <th>customer_id</th>
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
      <td>ANATR</td>
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
      <td>ANTON</td>
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
      <td>AROUT</td>
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
      <td>BERGS</td>
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
      <th>4</th>
      <td>BLONP</td>
      <td>Blondesddsl père et fils</td>
      <td>Frédérique Citeaux</td>
      <td>Marketing Manager</td>
      <td>24, place Kléber</td>
      <td>Strasbourg</td>
      <td>None</td>
      <td>67000</td>
      <td>France</td>
      <td>88.60.15.31</td>
      <td>88.60.15.32</td>
    </tr>
  </tbody>
</table>
</div>


### Mais operadores

Os operadores de comparação no SQL são essenciais para filtrar registros em consultas com base em condições específicas. Vamos examinar cada um dos operadores que você mencionou (`<`, `>`, `<=`, `>=`, `<>`) com exemplos práticos. Suponhamos que temos uma tabela chamada `products` com uma coluna `unit_price` para o preço dos produtos e uma coluna `units_in_stock` para o número de itens em estoque.

### Operador `<` (Menor que)

```sql
-- Seleciona todos os produtos com preço menor que 20
SELECT * FROM products
WHERE unit_price < 20;
```


```python
query = '''
SELECT * FROM products
WHERE unit_price < 20 LIMIT 10 '''
pd.read_sql(query,conn)
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
      <th>product_id</th>
      <th>product_name</th>
      <th>supplier_id</th>
      <th>category_id</th>
      <th>quantity_per_unit</th>
      <th>unit_price</th>
      <th>units_in_stock</th>
      <th>units_on_order</th>
      <th>reorder_level</th>
      <th>discontinued</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Chai</td>
      <td>8</td>
      <td>1</td>
      <td>10 boxes x 30 bags</td>
      <td>18.00</td>
      <td>39</td>
      <td>0</td>
      <td>10</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Chang</td>
      <td>1</td>
      <td>1</td>
      <td>24 - 12 oz bottles</td>
      <td>19.00</td>
      <td>17</td>
      <td>40</td>
      <td>25</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Aniseed Syrup</td>
      <td>1</td>
      <td>2</td>
      <td>12 - 550 ml bottles</td>
      <td>10.00</td>
      <td>13</td>
      <td>70</td>
      <td>25</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13</td>
      <td>Konbu</td>
      <td>6</td>
      <td>8</td>
      <td>2 kg box</td>
      <td>6.00</td>
      <td>24</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>15</td>
      <td>Genen Shouyu</td>
      <td>6</td>
      <td>2</td>
      <td>24 - 250 ml bottles</td>
      <td>13.00</td>
      <td>39</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>16</td>
      <td>Pavlova</td>
      <td>7</td>
      <td>3</td>
      <td>32 - 500 g boxes</td>
      <td>17.45</td>
      <td>29</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>19</td>
      <td>Teatime Chocolate Biscuits</td>
      <td>8</td>
      <td>3</td>
      <td>10 boxes x 12 pieces</td>
      <td>9.20</td>
      <td>25</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>21</td>
      <td>Sir Rodney's Scones</td>
      <td>8</td>
      <td>3</td>
      <td>24 pkgs. x 4 pieces</td>
      <td>10.00</td>
      <td>3</td>
      <td>40</td>
      <td>5</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>23</td>
      <td>Tunnbröd</td>
      <td>9</td>
      <td>5</td>
      <td>12 - 250 g pkgs.</td>
      <td>9.00</td>
      <td>61</td>
      <td>0</td>
      <td>25</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>24</td>
      <td>Guaraná Fantástica</td>
      <td>10</td>
      <td>1</td>
      <td>12 - 355 ml cans</td>
      <td>4.50</td>
      <td>20</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### Operador `>` (Maior que)

```sql
-- Seleciona todos os produtos com preço maior que 100
SELECT * FROM products
WHERE unit_price > 100;
```


```python
query = '''
SELECT * FROM products
WHERE unit_price > 100 '''
pd.read_sql(query, conn)
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
      <th>product_id</th>
      <th>product_name</th>
      <th>supplier_id</th>
      <th>category_id</th>
      <th>quantity_per_unit</th>
      <th>unit_price</th>
      <th>units_in_stock</th>
      <th>units_on_order</th>
      <th>reorder_level</th>
      <th>discontinued</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>29</td>
      <td>Thüringer Rostbratwurst</td>
      <td>12</td>
      <td>6</td>
      <td>50 bags x 30 sausgs.</td>
      <td>123.79</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>38</td>
      <td>Côte de Blaye</td>
      <td>18</td>
      <td>1</td>
      <td>12 - 75 cl bottles</td>
      <td>263.50</td>
      <td>17</td>
      <td>0</td>
      <td>15</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



### Operador `<=` (Menor ou igual a)

```sql
-- Seleciona todos os produtos com preço menor ou igual a 50
SELECT * FROM products
WHERE unit_price <= 50;
```


```python
query = '''
SELECT * FROM products
WHERE unit_price <= 50 LIMIT 5'''
pd.read_sql(query, conn)
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
      <th>product_id</th>
      <th>product_name</th>
      <th>supplier_id</th>
      <th>category_id</th>
      <th>quantity_per_unit</th>
      <th>unit_price</th>
      <th>units_in_stock</th>
      <th>units_on_order</th>
      <th>reorder_level</th>
      <th>discontinued</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Chai</td>
      <td>8</td>
      <td>1</td>
      <td>10 boxes x 30 bags</td>
      <td>18.00</td>
      <td>39</td>
      <td>0</td>
      <td>10</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Chang</td>
      <td>1</td>
      <td>1</td>
      <td>24 - 12 oz bottles</td>
      <td>19.00</td>
      <td>17</td>
      <td>40</td>
      <td>25</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Aniseed Syrup</td>
      <td>1</td>
      <td>2</td>
      <td>12 - 550 ml bottles</td>
      <td>10.00</td>
      <td>13</td>
      <td>70</td>
      <td>25</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Chef Anton's Cajun Seasoning</td>
      <td>2</td>
      <td>2</td>
      <td>48 - 6 oz jars</td>
      <td>22.00</td>
      <td>53</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Chef Anton's Gumbo Mix</td>
      <td>2</td>
      <td>2</td>
      <td>36 boxes</td>
      <td>21.35</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### Operador `>=` (Maior ou igual a)

```sql
-- Seleciona todos os produtos com quantidade em estoque maior ou igual a 10
SELECT * FROM products
WHERE units_in_stock >= 10;
```


```python
query = '''
SELECT * FROM products
WHERE units_in_stock >= 10 LIMIT 5 '''
pd.read_sql(query, conn)
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
      <th>product_id</th>
      <th>product_name</th>
      <th>supplier_id</th>
      <th>category_id</th>
      <th>quantity_per_unit</th>
      <th>unit_price</th>
      <th>units_in_stock</th>
      <th>units_on_order</th>
      <th>reorder_level</th>
      <th>discontinued</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Chai</td>
      <td>8</td>
      <td>1</td>
      <td>10 boxes x 30 bags</td>
      <td>18.0</td>
      <td>39</td>
      <td>0</td>
      <td>10</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Chang</td>
      <td>1</td>
      <td>1</td>
      <td>24 - 12 oz bottles</td>
      <td>19.0</td>
      <td>17</td>
      <td>40</td>
      <td>25</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Aniseed Syrup</td>
      <td>1</td>
      <td>2</td>
      <td>12 - 550 ml bottles</td>
      <td>10.0</td>
      <td>13</td>
      <td>70</td>
      <td>25</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Chef Anton's Cajun Seasoning</td>
      <td>2</td>
      <td>2</td>
      <td>48 - 6 oz jars</td>
      <td>22.0</td>
      <td>53</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6</td>
      <td>Grandma's Boysenberry Spread</td>
      <td>3</td>
      <td>2</td>
      <td>12 - 8 oz jars</td>
      <td>25.0</td>
      <td>120</td>
      <td>0</td>
      <td>25</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



### Operador `<>` (Diferente de)

```sql
-- Seleciona todos os produtos cujo preço não é 30
SELECT * FROM products
WHERE unit_price <> 30;
```


```python
query = '''
SELECT * FROM products
WHERE unit_price <> 30 LIMIT 5 '''
pd.read_sql(query, conn)
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
      <th>product_id</th>
      <th>product_name</th>
      <th>supplier_id</th>
      <th>category_id</th>
      <th>quantity_per_unit</th>
      <th>unit_price</th>
      <th>units_in_stock</th>
      <th>units_on_order</th>
      <th>reorder_level</th>
      <th>discontinued</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Chai</td>
      <td>8</td>
      <td>1</td>
      <td>10 boxes x 30 bags</td>
      <td>18.00</td>
      <td>39</td>
      <td>0</td>
      <td>10</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Chang</td>
      <td>1</td>
      <td>1</td>
      <td>24 - 12 oz bottles</td>
      <td>19.00</td>
      <td>17</td>
      <td>40</td>
      <td>25</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Aniseed Syrup</td>
      <td>1</td>
      <td>2</td>
      <td>12 - 550 ml bottles</td>
      <td>10.00</td>
      <td>13</td>
      <td>70</td>
      <td>25</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Chef Anton's Cajun Seasoning</td>
      <td>2</td>
      <td>2</td>
      <td>48 - 6 oz jars</td>
      <td>22.00</td>
      <td>53</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Chef Anton's Gumbo Mix</td>
      <td>2</td>
      <td>2</td>
      <td>36 boxes</td>
      <td>21.35</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### Combinação de Operadores

Você também pode combinar vários operadores em uma única consulta para criar condições mais específicas:

```sql
-- Seleciona todos os produtos com preço entre 50 e 100 (exclusive)
SELECT * FROM products
WHERE unit_price >= 50 AND unit_price < 100;
```

```sql
-- Seleciona todos os produtos com preço fora do intervalo 20 a 40
SELECT * FROM products
WHERE unit_price < 20 OR unit_price > 40;
```


```python
query = '''
SELECT * FROM products
WHERE unit_price >= 50 AND unit_price < 100'''
pd.read_sql(query, conn)

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
      <th>product_id</th>
      <th>product_name</th>
      <th>supplier_id</th>
      <th>category_id</th>
      <th>quantity_per_unit</th>
      <th>unit_price</th>
      <th>units_in_stock</th>
      <th>units_on_order</th>
      <th>reorder_level</th>
      <th>discontinued</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9</td>
      <td>Mishi Kobe Niku</td>
      <td>4</td>
      <td>6</td>
      <td>18 - 500 g pkgs.</td>
      <td>97.0</td>
      <td>29</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>18</td>
      <td>Carnarvon Tigers</td>
      <td>7</td>
      <td>8</td>
      <td>16 kg pkg.</td>
      <td>62.5</td>
      <td>42</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20</td>
      <td>Sir Rodney's Marmalade</td>
      <td>8</td>
      <td>3</td>
      <td>30 gift boxes</td>
      <td>81.0</td>
      <td>40</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>51</td>
      <td>Manjimup Dried Apples</td>
      <td>24</td>
      <td>7</td>
      <td>50 - 300 g pkgs.</td>
      <td>53.0</td>
      <td>20</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>59</td>
      <td>Raclette Courdavault</td>
      <td>28</td>
      <td>4</td>
      <td>5 kg pkg.</td>
      <td>55.0</td>
      <td>79</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



#### **Is null and is not null**: Usado em conjunto com o `where` para criar regras mais complexas de filtro nos registros.

```sql
SELECT * FROM customers
WHERE contact_name is Null;

SELECT * FROM customers
WHERE contact_name is not null;
```


```python
query = '''
SELECT * FROM customers
WHERE contact_name is not null LIMIT 5'''
pd.read_sql(query, conn)
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
      <th>customer_id</th>
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
      <td>ALFKI</td>
      <td>Alfreds Futterkiste</td>
      <td>Maria Anders</td>
      <td>Sales Representative</td>
      <td>Obere Str. 57</td>
      <td>Berlin</td>
      <td>None</td>
      <td>12209</td>
      <td>Germany</td>
      <td>030-0074321</td>
      <td>030-0076545</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ANATR</td>
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
      <th>2</th>
      <td>ANTON</td>
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
      <th>3</th>
      <td>AROUT</td>
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
      <td>BERGS</td>
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
  </tbody>
</table>
</div>



#### **LIKE**

```SQL
-- Nome do cliente começando com "a":
SELECT * FROM customers
WHERE contact_name LIKE 'a%';
```


```python
query = '''
SELECT * FROM customers
WHERE contact_name LIKE 'a%'
'''
pd.read_sql(query, conn)
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
      <th>customer_id</th>
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
  </tbody>
</table>
</div>



* **Não localizou nenhum dado onde o atributo contact_name começa com `a` em mínusculo.**

Para tratar as strings como maiúsculas ou minúsculas em uma consulta SQL, você pode usar as funções `UPPER()` ou `LOWER()`, respectivamente. Essas funções convertem todas as letras em uma string para maiúsculas ou minúsculas, permitindo que você faça comparações de forma mais flexível, ignorando a diferença entre maiúsculas e minúsculas.

Aqui está como você pode modificar a consulta para encontrar todos os clientes cujo nome começa com a letra "a", independentemente de ser maiúscula ou minúscula:

```sql
SELECT * FROM customers
WHERE LOWER(contact_name) LIKE 'a%';
```


```python
query = '''
SELECT * FROM customers WHERE LOWER(contact_name) LIKE 'a%' LIMIT 5
'''
pd.read_sql(query, conn)
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
      <th>customer_id</th>
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
      <td>ANATR</td>
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
      <td>ANTON</td>
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
      <td>EASTC</td>
      <td>Eastern Connection</td>
      <td>Ann Devon</td>
      <td>Sales Agent</td>
      <td>35 King George</td>
      <td>London</td>
      <td>None</td>
      <td>WX3 6FW</td>
      <td>UK</td>
      <td>(171) 555-0297</td>
      <td>(171) 555-3373</td>
    </tr>
    <tr>
      <th>3</th>
      <td>FAMIA</td>
      <td>Familia Arquibaldo</td>
      <td>Aria Cruz</td>
      <td>Marketing Assistant</td>
      <td>Rua Orós, 92</td>
      <td>Sao Paulo</td>
      <td>SP</td>
      <td>05442-030</td>
      <td>Brazil</td>
      <td>(11) 555-9857</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>GOURL</td>
      <td>Gourmet Lanchonetes</td>
      <td>André Fonseca</td>
      <td>Sales Associate</td>
      <td>Av. Brasil, 442</td>
      <td>Campinas</td>
      <td>SP</td>
      <td>04876-786</td>
      <td>Brazil</td>
      <td>(11) 555-9482</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>



#### **Usar `ILIKE()` é uma prática comum para garantir que as condições não sejam afetadas por diferenças de capitalização nas entradas de dados.**

```sql
-- Nome do cliente terminando com "a":
SELECT * FROM customers
WHERE contact_name ILIKE '%a';

-- Nome do cliente que possui "or" em qualquer posição:
SELECT * FROM customers
WHERE contact_name ILIKE '%or%';

-- Nome do cliente com "r" na segunda posição:
SELECT * FROM customers
WHERE contact_name ILIKE '_r%';

-- Nome do cliente que começa com "A" e tem pelo menos 3 caracteres de comprimento:
SELECT * FROM customers
WHERE contact_name ILIKE 'A_%_%';

-- Nome do contato que começa com "A" e termina com "o":
SELECT * FROM customers
WHERE contact_name ILIKE 'A%o';

-- Nome do cliente que NÃO começa com "a":
SELECT * FROM customers
WHERE contact_name NOT ILIKE 'A%';

-- Usando o curinga [charlist] (SQL server)
SELECT * FROM customers
WHERE city ILIKE '[BSP]%';

-- Usando o curinga Similar To (Postgres)
SELECT * FROM customers
WHERE city SIMILAR TO '(B|S|P)%';

-- Usando o MySQL (coitado, tem nada)
SELECT * FROM customers
WHERE (city LIKE 'B%' OR city LIKE 'S%' OR city LIKE 'P%');
```


```python
q1 = '''
SELECT * FROM customers
WHERE contact_name ILIKE '%a' LIMIT 5;
'''
q2 = '''
SELECT * FROM customers
WHERE contact_name ILIKE '%or%' LIMIT 5;
'''
q3 = '''
SELECT * FROM customers
WHERE contact_name ILIKE '_r%' LIMIT 5;
'''
q4 = '''
SELECT * FROM customers
WHERE contact_name ILIKE 'A_%_%' LIMIT 5;
'''
q5 = '''
SELECT * FROM customers
WHERE contact_name ILIKE 'A%o' LIMIT 5;
'''
q6 = '''
SELECT * FROM customers
WHERE contact_name NOT ILIKE 'A%' LIMIT 5;
'''
q7 = '''
SELECT * FROM customers
WHERE city ILIKE '[BSP]%' LIMIT 5;
'''
q8 = '''
SELECT * FROM customers
WHERE city SIMILAR TO '(B|S|P)%' LIMIT 5;
'''
q9 = '''
SELECT * FROM customers
WHERE (city LIKE 'B%' OR city LIKE 'S%' OR city LIKE 'P%') LIMIT 5;
'''
queries = [q1,q2,q3,q4,q5,q6,q7,q8,q9]

# Executando todas a queries:
for query in queries:
    print(100 * "=")
    print(f"Resultado da query:{query}")
    print(100 * "=")
    display(pd.read_sql(query,conn))
```

    ====================================================================================================
    Resultado da query:
    SELECT * FROM customers
    WHERE contact_name ILIKE '%a' LIMIT 5;

    ====================================================================================================



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
      <th>customer_id</th>
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
      <td>GALED</td>
      <td>Galería del gastrónomo</td>
      <td>Eduardo Saavedra</td>
      <td>Marketing Manager</td>
      <td>Rambla de Cataluña, 23</td>
      <td>Barcelona</td>
      <td>None</td>
      <td>08022</td>
      <td>Spain</td>
      <td>(93) 203 4560</td>
      <td>(93) 203 4561</td>
    </tr>
    <tr>
      <th>1</th>
      <td>GOURL</td>
      <td>Gourmet Lanchonetes</td>
      <td>André Fonseca</td>
      <td>Sales Associate</td>
      <td>Av. Brasil, 442</td>
      <td>Campinas</td>
      <td>SP</td>
      <td>04876-786</td>
      <td>Brazil</td>
      <td>(11) 555-9482</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>GROSR</td>
      <td>GROSELLA-Restaurante</td>
      <td>Manuel Pereira</td>
      <td>Owner</td>
      <td>5ª Ave. Los Palos Grandes</td>
      <td>Caracas</td>
      <td>DF</td>
      <td>1081</td>
      <td>Venezuela</td>
      <td>(2) 283-2951</td>
      <td>(2) 283-3397</td>
    </tr>
    <tr>
      <th>3</th>
      <td>HUNGO</td>
      <td>Hungry Owl All-Night Grocers</td>
      <td>Patricia McKenna</td>
      <td>Sales Associate</td>
      <td>8 Johnstown Road</td>
      <td>Cork</td>
      <td>Co. Cork</td>
      <td>None</td>
      <td>Ireland</td>
      <td>2967 542</td>
      <td>2967 3333</td>
    </tr>
    <tr>
      <th>4</th>
      <td>OCEAN</td>
      <td>Océano Atlántico Ltda.</td>
      <td>Yvonne Moncada</td>
      <td>Sales Agent</td>
      <td>Ing. Gustavo Moncada 8585 Piso 20-A</td>
      <td>Buenos Aires</td>
      <td>None</td>
      <td>1010</td>
      <td>Argentina</td>
      <td>(1) 135-5333</td>
      <td>(1) 135-5535</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    SELECT * FROM customers
    WHERE contact_name ILIKE '%or%' LIMIT 5;

    ====================================================================================================



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
      <th>customer_id</th>
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
      <td>ANTON</td>
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
      <th>1</th>
      <td>BSBEV</td>
      <td>B's Beverages</td>
      <td>Victoria Ashworth</td>
      <td>Sales Representative</td>
      <td>Fauntleroy Circus</td>
      <td>London</td>
      <td>None</td>
      <td>EC2 5NT</td>
      <td>UK</td>
      <td>(171) 555-1212</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>FRANS</td>
      <td>Franchi S.p.A.</td>
      <td>Paolo Accorti</td>
      <td>Sales Representative</td>
      <td>Via Monte Bianco 34</td>
      <td>Torino</td>
      <td>None</td>
      <td>10100</td>
      <td>Italy</td>
      <td>011-4988260</td>
      <td>011-4988261</td>
    </tr>
    <tr>
      <th>3</th>
      <td>LETSS</td>
      <td>Let's Stop N Shop</td>
      <td>Jaime Yorres</td>
      <td>Owner</td>
      <td>87 Polk St. Suite 5</td>
      <td>San Francisco</td>
      <td>CA</td>
      <td>94117</td>
      <td>USA</td>
      <td>(415) 555-5938</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PICCO</td>
      <td>Piccolo und mehr</td>
      <td>Georg Pipps</td>
      <td>Sales Manager</td>
      <td>Geislweg 14</td>
      <td>Salzburg</td>
      <td>None</td>
      <td>5020</td>
      <td>Austria</td>
      <td>6562-9722</td>
      <td>6562-9723</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    SELECT * FROM customers
    WHERE contact_name ILIKE '_r%' LIMIT 5;

    ====================================================================================================



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
      <th>customer_id</th>
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
      <td>BLONP</td>
      <td>Blondesddsl père et fils</td>
      <td>Frédérique Citeaux</td>
      <td>Marketing Manager</td>
      <td>24, place Kléber</td>
      <td>Strasbourg</td>
      <td>None</td>
      <td>67000</td>
      <td>France</td>
      <td>88.60.15.31</td>
      <td>88.60.15.32</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CENTC</td>
      <td>Centro comercial Moctezuma</td>
      <td>Francisco Chang</td>
      <td>Marketing Manager</td>
      <td>Sierras de Granada 9993</td>
      <td>México D.F.</td>
      <td>None</td>
      <td>05022</td>
      <td>Mexico</td>
      <td>(5) 555-3392</td>
      <td>(5) 555-7293</td>
    </tr>
    <tr>
      <th>2</th>
      <td>FAMIA</td>
      <td>Familia Arquibaldo</td>
      <td>Aria Cruz</td>
      <td>Marketing Assistant</td>
      <td>Rua Orós, 92</td>
      <td>Sao Paulo</td>
      <td>SP</td>
      <td>05442-030</td>
      <td>Brazil</td>
      <td>(11) 555-9857</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>LONEP</td>
      <td>Lonesome Pine Restaurant</td>
      <td>Fran Wilson</td>
      <td>Sales Manager</td>
      <td>89 Chiaroscuro Rd.</td>
      <td>Portland</td>
      <td>OR</td>
      <td>97219</td>
      <td>USA</td>
      <td>(503) 555-9573</td>
      <td>(503) 555-9646</td>
    </tr>
    <tr>
      <th>4</th>
      <td>SPLIR</td>
      <td>Split Rail Beer &amp; Ale</td>
      <td>Art Braunschweiger</td>
      <td>Sales Manager</td>
      <td>P.O. Box 555</td>
      <td>Lander</td>
      <td>WY</td>
      <td>82520</td>
      <td>USA</td>
      <td>(307) 555-4680</td>
      <td>(307) 555-6525</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    SELECT * FROM customers
    WHERE contact_name ILIKE 'A_%_%' LIMIT 5;

    ====================================================================================================



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
      <th>customer_id</th>
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
      <td>ANATR</td>
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
      <td>ANTON</td>
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
      <td>EASTC</td>
      <td>Eastern Connection</td>
      <td>Ann Devon</td>
      <td>Sales Agent</td>
      <td>35 King George</td>
      <td>London</td>
      <td>None</td>
      <td>WX3 6FW</td>
      <td>UK</td>
      <td>(171) 555-0297</td>
      <td>(171) 555-3373</td>
    </tr>
    <tr>
      <th>3</th>
      <td>FAMIA</td>
      <td>Familia Arquibaldo</td>
      <td>Aria Cruz</td>
      <td>Marketing Assistant</td>
      <td>Rua Orós, 92</td>
      <td>Sao Paulo</td>
      <td>SP</td>
      <td>05442-030</td>
      <td>Brazil</td>
      <td>(11) 555-9857</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>GOURL</td>
      <td>Gourmet Lanchonetes</td>
      <td>André Fonseca</td>
      <td>Sales Associate</td>
      <td>Av. Brasil, 442</td>
      <td>Campinas</td>
      <td>SP</td>
      <td>04876-786</td>
      <td>Brazil</td>
      <td>(11) 555-9482</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    SELECT * FROM customers
    WHERE contact_name ILIKE 'A%o' LIMIT 5;

    ====================================================================================================



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
      <th>customer_id</th>
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
      <td>ANATR</td>
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
      <td>ANTON</td>
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
      <td>ROMEY</td>
      <td>Romero y tomillo</td>
      <td>Alejandra Camino</td>
      <td>Accounting Manager</td>
      <td>Gran Vía, 1</td>
      <td>Madrid</td>
      <td>None</td>
      <td>28001</td>
      <td>Spain</td>
      <td>(91) 745 6200</td>
      <td>(91) 745 6210</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    SELECT * FROM customers
    WHERE contact_name NOT ILIKE 'A%' LIMIT 5;

    ====================================================================================================



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
      <th>customer_id</th>
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
      <td>ALFKI</td>
      <td>Alfreds Futterkiste</td>
      <td>Maria Anders</td>
      <td>Sales Representative</td>
      <td>Obere Str. 57</td>
      <td>Berlin</td>
      <td>None</td>
      <td>12209</td>
      <td>Germany</td>
      <td>030-0074321</td>
      <td>030-0076545</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AROUT</td>
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
      <th>2</th>
      <td>BERGS</td>
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
      <th>3</th>
      <td>BLAUS</td>
      <td>Blauer See Delikatessen</td>
      <td>Hanna Moos</td>
      <td>Sales Representative</td>
      <td>Forsterstr. 57</td>
      <td>Mannheim</td>
      <td>None</td>
      <td>68306</td>
      <td>Germany</td>
      <td>0621-08460</td>
      <td>0621-08924</td>
    </tr>
    <tr>
      <th>4</th>
      <td>BLONP</td>
      <td>Blondesddsl père et fils</td>
      <td>Frédérique Citeaux</td>
      <td>Marketing Manager</td>
      <td>24, place Kléber</td>
      <td>Strasbourg</td>
      <td>None</td>
      <td>67000</td>
      <td>France</td>
      <td>88.60.15.31</td>
      <td>88.60.15.32</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    SELECT * FROM customers
    WHERE city ILIKE '[BSP]%' LIMIT 5;

    ====================================================================================================



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
      <th>customer_id</th>
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
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    SELECT * FROM customers
    WHERE city SIMILAR TO '(B|S|P)%' LIMIT 5;

    ====================================================================================================



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
      <th>customer_id</th>
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
      <td>ALFKI</td>
      <td>Alfreds Futterkiste</td>
      <td>Maria Anders</td>
      <td>Sales Representative</td>
      <td>Obere Str. 57</td>
      <td>Berlin</td>
      <td>None</td>
      <td>12209</td>
      <td>Germany</td>
      <td>030-0074321</td>
      <td>030-0076545</td>
    </tr>
    <tr>
      <th>1</th>
      <td>BLONP</td>
      <td>Blondesddsl père et fils</td>
      <td>Frédérique Citeaux</td>
      <td>Marketing Manager</td>
      <td>24, place Kléber</td>
      <td>Strasbourg</td>
      <td>None</td>
      <td>67000</td>
      <td>France</td>
      <td>88.60.15.31</td>
      <td>88.60.15.32</td>
    </tr>
    <tr>
      <th>2</th>
      <td>CACTU</td>
      <td>Cactus Comidas para llevar</td>
      <td>Patricio Simpson</td>
      <td>Sales Agent</td>
      <td>Cerrito 333</td>
      <td>Buenos Aires</td>
      <td>None</td>
      <td>1010</td>
      <td>Argentina</td>
      <td>(1) 135-5555</td>
      <td>(1) 135-4892</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CHOPS</td>
      <td>Chop-suey Chinese</td>
      <td>Yang Wang</td>
      <td>Owner</td>
      <td>Hauptstr. 29</td>
      <td>Bern</td>
      <td>None</td>
      <td>3012</td>
      <td>Switzerland</td>
      <td>0452-076545</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>COMMI</td>
      <td>Comércio Mineiro</td>
      <td>Pedro Afonso</td>
      <td>Sales Associate</td>
      <td>Av. dos Lusíadas, 23</td>
      <td>Sao Paulo</td>
      <td>SP</td>
      <td>05432-043</td>
      <td>Brazil</td>
      <td>(11) 555-7647</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    SELECT * FROM customers
    WHERE (city LIKE 'B%' OR city LIKE 'S%' OR city LIKE 'P%') LIMIT 5;

    ====================================================================================================



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
      <th>customer_id</th>
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
      <td>ALFKI</td>
      <td>Alfreds Futterkiste</td>
      <td>Maria Anders</td>
      <td>Sales Representative</td>
      <td>Obere Str. 57</td>
      <td>Berlin</td>
      <td>None</td>
      <td>12209</td>
      <td>Germany</td>
      <td>030-0074321</td>
      <td>030-0076545</td>
    </tr>
    <tr>
      <th>1</th>
      <td>BLONP</td>
      <td>Blondesddsl père et fils</td>
      <td>Frédérique Citeaux</td>
      <td>Marketing Manager</td>
      <td>24, place Kléber</td>
      <td>Strasbourg</td>
      <td>None</td>
      <td>67000</td>
      <td>France</td>
      <td>88.60.15.31</td>
      <td>88.60.15.32</td>
    </tr>
    <tr>
      <th>2</th>
      <td>CACTU</td>
      <td>Cactus Comidas para llevar</td>
      <td>Patricio Simpson</td>
      <td>Sales Agent</td>
      <td>Cerrito 333</td>
      <td>Buenos Aires</td>
      <td>None</td>
      <td>1010</td>
      <td>Argentina</td>
      <td>(1) 135-5555</td>
      <td>(1) 135-4892</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CHOPS</td>
      <td>Chop-suey Chinese</td>
      <td>Yang Wang</td>
      <td>Owner</td>
      <td>Hauptstr. 29</td>
      <td>Bern</td>
      <td>None</td>
      <td>3012</td>
      <td>Switzerland</td>
      <td>0452-076545</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>COMMI</td>
      <td>Comércio Mineiro</td>
      <td>Pedro Afonso</td>
      <td>Sales Associate</td>
      <td>Av. dos Lusíadas, 23</td>
      <td>Sao Paulo</td>
      <td>SP</td>
      <td>05432-043</td>
      <td>Brazil</td>
      <td>(11) 555-7647</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>


### **Operador IN**

```sql
-- localizado na "Alemanha", "França" ou "Reino Unido":
SELECT * FROM customers
WHERE country IN ('Germany', 'France', 'UK');

-- NÃO localizado na "Alemanha", "França" ou "Reino Unido":
SELECT * FROM customers
WHERE country NOT IN ('Germany', 'France', 'UK');

-- Só para dar um gostinho de uma subqueyr... Seleciona todos os clientes que são dos mesmos países que os fornecedores:

SELECT * FROM customers
WHERE country IN (SELECT country FROM suppliers);

-- Exemplo com BETWEEN
SELECT * FROM products
WHERE unit_price BETWEEN 10 AND 20;

-- Exemplo com NOT BETWEEN
SELECT * FROM products
WHERE unit_price NOT BETWEEN 10 AND 20;

-- Seleciona todos os produtos com preço ENTRE 10 e 20. Adicionalmente, não mostra produtos com CategoryID de 1, 2 ou 3:
SELECT * FROM products
WHERE (unit_price BETWEEN 10 AND 20) AND category_id NOT IN (1, 2, 3);
```

```sql
--selects todos os produtos entre 'Carnarvon Tigers' e 'Mozzarella di Giovanni':
select * from products
where product_name between 'Carnarvon Tigers' and 'Mozzarella di Giovanni'
order by product_name;

--Selecione todas as ordens BETWEEN '04-July-1996' e '09-July-1996':
select * from orders
where order_date between '07/04/1996' and '07/09/1996';
```


```python
q1 = '''
SELECT * FROM customers
WHERE country IN ('Germany', 'France', 'UK') LIMIT 5;
'''
q2 = '''
SELECT * FROM customers
WHERE country NOT IN ('Germany', 'France', 'UK') LIMIT 5;
'''
q3 = '''
SELECT * FROM customers
WHERE country IN (SELECT country FROM suppliers) LIMIT 5;
'''
q4 = '''
SELECT * FROM products
WHERE unit_price BETWEEN 10 AND 20 LIMIT 5;
'''
q5 = '''
SELECT * FROM products
WHERE unit_price NOT BETWEEN 10 AND 20 LIMIT 5;
'''
q6 = '''
SELECT * FROM products
WHERE (unit_price BETWEEN 10 AND 20) AND category_id NOT IN (1, 2, 3) LIMIT 5;
'''
q7 = '''
select * from products
where product_name between 'Carnarvon Tigers' and 'Mozzarella di Giovanni'
order by product_name LIMIT 5;
'''
q8 = '''
select * from orders
where order_date between '07/04/1996' and '07/09/1996' LIMIT 5;
'''

queries = [q1,q2,q3,q4,q5,q6,q7,q8]

# Executando todas a queries:
for query in queries:
    print(100 * "=")
    print(f"Resultado da query:{query}")
    print(100 * "=")
    display(pd.read_sql(query,conn))
```

    ====================================================================================================
    Resultado da query:
    SELECT * FROM customers
    WHERE country IN ('Germany', 'France', 'UK') LIMIT 5;

    ====================================================================================================



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
      <th>customer_id</th>
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
      <td>ALFKI</td>
      <td>Alfreds Futterkiste</td>
      <td>Maria Anders</td>
      <td>Sales Representative</td>
      <td>Obere Str. 57</td>
      <td>Berlin</td>
      <td>None</td>
      <td>12209</td>
      <td>Germany</td>
      <td>030-0074321</td>
      <td>030-0076545</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AROUT</td>
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
      <th>2</th>
      <td>BLAUS</td>
      <td>Blauer See Delikatessen</td>
      <td>Hanna Moos</td>
      <td>Sales Representative</td>
      <td>Forsterstr. 57</td>
      <td>Mannheim</td>
      <td>None</td>
      <td>68306</td>
      <td>Germany</td>
      <td>0621-08460</td>
      <td>0621-08924</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BLONP</td>
      <td>Blondesddsl père et fils</td>
      <td>Frédérique Citeaux</td>
      <td>Marketing Manager</td>
      <td>24, place Kléber</td>
      <td>Strasbourg</td>
      <td>None</td>
      <td>67000</td>
      <td>France</td>
      <td>88.60.15.31</td>
      <td>88.60.15.32</td>
    </tr>
    <tr>
      <th>4</th>
      <td>BONAP</td>
      <td>Bon app'</td>
      <td>Laurence Lebihan</td>
      <td>Owner</td>
      <td>12, rue des Bouchers</td>
      <td>Marseille</td>
      <td>None</td>
      <td>13008</td>
      <td>France</td>
      <td>91.24.45.40</td>
      <td>91.24.45.41</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    SELECT * FROM customers
    WHERE country NOT IN ('Germany', 'France', 'UK') LIMIT 5;

    ====================================================================================================



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
      <th>customer_id</th>
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
      <td>ANATR</td>
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
      <td>ANTON</td>
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
      <td>BERGS</td>
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
      <th>3</th>
      <td>BOLID</td>
      <td>Bólido Comidas preparadas</td>
      <td>Martín Sommer</td>
      <td>Owner</td>
      <td>C/ Araquil, 67</td>
      <td>Madrid</td>
      <td>None</td>
      <td>28023</td>
      <td>Spain</td>
      <td>(91) 555 22 82</td>
      <td>(91) 555 91 99</td>
    </tr>
    <tr>
      <th>4</th>
      <td>BOTTM</td>
      <td>Bottom-Dollar Markets</td>
      <td>Elizabeth Lincoln</td>
      <td>Accounting Manager</td>
      <td>23 Tsawassen Blvd.</td>
      <td>Tsawassen</td>
      <td>BC</td>
      <td>T2F 8M4</td>
      <td>Canada</td>
      <td>(604) 555-4729</td>
      <td>(604) 555-3745</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    SELECT * FROM customers
    WHERE country IN (SELECT country FROM suppliers) LIMIT 5;

    ====================================================================================================



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
      <th>customer_id</th>
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
      <td>ALFKI</td>
      <td>Alfreds Futterkiste</td>
      <td>Maria Anders</td>
      <td>Sales Representative</td>
      <td>Obere Str. 57</td>
      <td>Berlin</td>
      <td>None</td>
      <td>12209</td>
      <td>Germany</td>
      <td>030-0074321</td>
      <td>030-0076545</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AROUT</td>
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
      <th>2</th>
      <td>BERGS</td>
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
      <th>3</th>
      <td>BLAUS</td>
      <td>Blauer See Delikatessen</td>
      <td>Hanna Moos</td>
      <td>Sales Representative</td>
      <td>Forsterstr. 57</td>
      <td>Mannheim</td>
      <td>None</td>
      <td>68306</td>
      <td>Germany</td>
      <td>0621-08460</td>
      <td>0621-08924</td>
    </tr>
    <tr>
      <th>4</th>
      <td>BLONP</td>
      <td>Blondesddsl père et fils</td>
      <td>Frédérique Citeaux</td>
      <td>Marketing Manager</td>
      <td>24, place Kléber</td>
      <td>Strasbourg</td>
      <td>None</td>
      <td>67000</td>
      <td>France</td>
      <td>88.60.15.31</td>
      <td>88.60.15.32</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    SELECT * FROM products
    WHERE unit_price BETWEEN 10 AND 20 LIMIT 5;

    ====================================================================================================



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
      <th>product_id</th>
      <th>product_name</th>
      <th>supplier_id</th>
      <th>category_id</th>
      <th>quantity_per_unit</th>
      <th>unit_price</th>
      <th>units_in_stock</th>
      <th>units_on_order</th>
      <th>reorder_level</th>
      <th>discontinued</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Chai</td>
      <td>8</td>
      <td>1</td>
      <td>10 boxes x 30 bags</td>
      <td>18.00</td>
      <td>39</td>
      <td>0</td>
      <td>10</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Chang</td>
      <td>1</td>
      <td>1</td>
      <td>24 - 12 oz bottles</td>
      <td>19.00</td>
      <td>17</td>
      <td>40</td>
      <td>25</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Aniseed Syrup</td>
      <td>1</td>
      <td>2</td>
      <td>12 - 550 ml bottles</td>
      <td>10.00</td>
      <td>13</td>
      <td>70</td>
      <td>25</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>Genen Shouyu</td>
      <td>6</td>
      <td>2</td>
      <td>24 - 250 ml bottles</td>
      <td>13.00</td>
      <td>39</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>16</td>
      <td>Pavlova</td>
      <td>7</td>
      <td>3</td>
      <td>32 - 500 g boxes</td>
      <td>17.45</td>
      <td>29</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    SELECT * FROM products
    WHERE unit_price NOT BETWEEN 10 AND 20 LIMIT 5;

    ====================================================================================================



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
      <th>product_id</th>
      <th>product_name</th>
      <th>supplier_id</th>
      <th>category_id</th>
      <th>quantity_per_unit</th>
      <th>unit_price</th>
      <th>units_in_stock</th>
      <th>units_on_order</th>
      <th>reorder_level</th>
      <th>discontinued</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>Chef Anton's Cajun Seasoning</td>
      <td>2</td>
      <td>2</td>
      <td>48 - 6 oz jars</td>
      <td>22.00</td>
      <td>53</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>Chef Anton's Gumbo Mix</td>
      <td>2</td>
      <td>2</td>
      <td>36 boxes</td>
      <td>21.35</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>Grandma's Boysenberry Spread</td>
      <td>3</td>
      <td>2</td>
      <td>12 - 8 oz jars</td>
      <td>25.00</td>
      <td>120</td>
      <td>0</td>
      <td>25</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>Uncle Bob's Organic Dried Pears</td>
      <td>3</td>
      <td>7</td>
      <td>12 - 1 lb pkgs.</td>
      <td>30.00</td>
      <td>15</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8</td>
      <td>Northwoods Cranberry Sauce</td>
      <td>3</td>
      <td>2</td>
      <td>12 - 12 oz jars</td>
      <td>40.00</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    SELECT * FROM products
    WHERE (unit_price BETWEEN 10 AND 20) AND category_id NOT IN (1, 2, 3) LIMIT 5;

    ====================================================================================================



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
      <th>product_id</th>
      <th>product_name</th>
      <th>supplier_id</th>
      <th>category_id</th>
      <th>quantity_per_unit</th>
      <th>unit_price</th>
      <th>units_in_stock</th>
      <th>units_on_order</th>
      <th>reorder_level</th>
      <th>discontinued</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>31</td>
      <td>Gorgonzola Telino</td>
      <td>14</td>
      <td>4</td>
      <td>12 - 100 g pkgs</td>
      <td>12.5</td>
      <td>0</td>
      <td>70</td>
      <td>20</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>36</td>
      <td>Inlagd Sill</td>
      <td>17</td>
      <td>8</td>
      <td>24 - 250 g  jars</td>
      <td>19.0</td>
      <td>112</td>
      <td>0</td>
      <td>20</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>40</td>
      <td>Boston Crab Meat</td>
      <td>19</td>
      <td>8</td>
      <td>24 - 4 oz tins</td>
      <td>18.4</td>
      <td>123</td>
      <td>0</td>
      <td>30</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>42</td>
      <td>Singaporean Hokkien Fried Mee</td>
      <td>20</td>
      <td>5</td>
      <td>32 - 1 kg pkgs.</td>
      <td>14.0</td>
      <td>26</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>46</td>
      <td>Spegesild</td>
      <td>21</td>
      <td>8</td>
      <td>4 - 450 g glasses</td>
      <td>12.0</td>
      <td>95</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    select * from products
    where product_name between 'Carnarvon Tigers' and 'Mozzarella di Giovanni'
    order by product_name LIMIT 5;

    ====================================================================================================



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
      <th>product_id</th>
      <th>product_name</th>
      <th>supplier_id</th>
      <th>category_id</th>
      <th>quantity_per_unit</th>
      <th>unit_price</th>
      <th>units_in_stock</th>
      <th>units_on_order</th>
      <th>reorder_level</th>
      <th>discontinued</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18</td>
      <td>Carnarvon Tigers</td>
      <td>7</td>
      <td>8</td>
      <td>16 kg pkg.</td>
      <td>62.5</td>
      <td>42</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Chai</td>
      <td>8</td>
      <td>1</td>
      <td>10 boxes x 30 bags</td>
      <td>18.0</td>
      <td>39</td>
      <td>0</td>
      <td>10</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Chang</td>
      <td>1</td>
      <td>1</td>
      <td>24 - 12 oz bottles</td>
      <td>19.0</td>
      <td>17</td>
      <td>40</td>
      <td>25</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>39</td>
      <td>Chartreuse verte</td>
      <td>18</td>
      <td>1</td>
      <td>750 cc per bottle</td>
      <td>18.0</td>
      <td>69</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Chef Anton's Cajun Seasoning</td>
      <td>2</td>
      <td>2</td>
      <td>48 - 6 oz jars</td>
      <td>22.0</td>
      <td>53</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    select * from orders
    where order_date between '07/04/1996' and '07/09/1996' LIMIT 5;

    ====================================================================================================



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
      <th>ship_city</th>
      <th>ship_region</th>
      <th>ship_postal_code</th>
      <th>ship_country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10248</td>
      <td>VINET</td>
      <td>5</td>
      <td>1996-07-04</td>
      <td>1996-08-01</td>
      <td>1996-07-16</td>
      <td>3</td>
      <td>32.38</td>
      <td>Vins et alcools Chevalier</td>
      <td>59 rue de l'Abbaye</td>
      <td>Reims</td>
      <td>None</td>
      <td>51100</td>
      <td>France</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10249</td>
      <td>TOMSP</td>
      <td>6</td>
      <td>1996-07-05</td>
      <td>1996-08-16</td>
      <td>1996-07-10</td>
      <td>1</td>
      <td>11.61</td>
      <td>Toms Spezialitäten</td>
      <td>Luisenstr. 48</td>
      <td>Münster</td>
      <td>None</td>
      <td>44087</td>
      <td>Germany</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10250</td>
      <td>HANAR</td>
      <td>4</td>
      <td>1996-07-08</td>
      <td>1996-08-05</td>
      <td>1996-07-12</td>
      <td>2</td>
      <td>65.83</td>
      <td>Hanari Carnes</td>
      <td>Rua do Paço, 67</td>
      <td>Rio de Janeiro</td>
      <td>RJ</td>
      <td>05454-876</td>
      <td>Brazil</td>
    </tr>
    <tr>
      <th>3</th>
      <td>10251</td>
      <td>VICTE</td>
      <td>3</td>
      <td>1996-07-08</td>
      <td>1996-08-05</td>
      <td>1996-07-15</td>
      <td>1</td>
      <td>41.34</td>
      <td>Victuailles en stock</td>
      <td>2, rue du Commerce</td>
      <td>Lyon</td>
      <td>None</td>
      <td>69004</td>
      <td>France</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10252</td>
      <td>SUPRD</td>
      <td>4</td>
      <td>1996-07-09</td>
      <td>1996-08-06</td>
      <td>1996-07-11</td>
      <td>2</td>
      <td>51.30</td>
      <td>Suprêmes délices</td>
      <td>Boulevard Tirou, 255</td>
      <td>Charleroi</td>
      <td>None</td>
      <td>B-6000</td>
      <td>Belgium</td>
    </tr>
  </tbody>
</table>
</div>


#### **Tangente sobre diferentes bancos**

O comando SQL que você mencionou é específico para PostgreSQL e não necessariamente padrão em todos os SGBDs (Sistemas de Gerenciamento de Banco de Dados). Cada SGBD pode ter funções e formatos de data ligeiramente diferentes. No entanto, a estrutura básica do comando `SELECT` e a cláusula `WHERE` usando `BETWEEN` são bastante universais.

Aqui estão algumas variantes para outros SGBDs populares:

### SQL Server

Para formatar datas em SQL Server, você usaria a função `CONVERT` ou `FORMAT` (a partir do SQL Server 2012):

```sql
-- Usando CONVERT
SELECT CONVERT(VARCHAR, order_date, 120) FROM orders
WHERE order_date BETWEEN '1996-04-07' AND '1996-09-07';

-- Usando FORMAT
SELECT FORMAT(order_date, 'yyyy-MM-dd') FROM orders
WHERE order_date BETWEEN '1996-04-07' AND '1996-09-07';
```

### MySQL

MySQL utiliza a função `DATE_FORMAT` para formatar datas:

```sql
SELECT DATE_FORMAT(order_date, '%Y-%m-%d') FROM orders
WHERE order_date BETWEEN '1996-04-07' AND '1996-09-07';
```

### Oracle

Oracle também usa a função `TO_CHAR` como PostgreSQL para formatação de datas:

```sql
SELECT TO_CHAR(order_date, 'YYYY-MM-DD') FROM orders
WHERE order_date BETWEEN TO_DATE('1996-04-07', 'YYYY-MM-DD') AND TO_DATE('1996-09-07', 'YYYY-MM-DD');
```

### SQLite

SQLite não tem uma função dedicada para formatar datas, mas você pode usar funções de string para manipular formatos de data padrão:

```sql
SELECT strftime('%Y-%m-%d', order_date) FROM orders
WHERE order_date BETWEEN '1996-04-07' AND '1996-09-07';
```

#### **Funções Agregadas** (COUNT, MAX, MIN, SUM, AVG): Usadas para realizar cálculos em um conjunto de valores.

As funções agregadas são uma ferramenta fundamental na linguagem SQL, utilizadas para realizar cálculos sobre um conjunto de valores e retornar um único valor resultante. Essas funções são especialmente úteis em operações que envolvem a análise estatística de dados, como a obtenção de médias, somas, valores máximos e mínimos, entre outros. Ao operar em conjuntos de dados, as funções agregadas permitem extrair insights significativos, suportar decisões de negócios, e simplificar dados complexos em informações gerenciáveis.

As funções agregadas geralmente são usadas em consultas SQL com a cláusula GROUP BY, que agrupa linhas que têm os mesmos valores em colunas especificadas. No entanto, podem ser usadas sem GROUP BY para resumir todos os dados de uma tabela. Aqui estão as principais funções agregadas e como são aplicadas:

```sql
-- Exemplo de MIN()
SELECT MIN(unit_price) AS preco_minimo
FROM products;

-- Exemplo de MAX()
SELECT MAX(unit_price) AS preco_maximo
FROM products;

-- Exemplo de COUNT()
SELECT COUNT(*) AS total_de_produtos
FROM products;

-- Exemplo de AVG()
SELECT AVG(unit_price) AS preco_medio
FROM products;

-- Exemplo de SUM()
SELECT SUM(quantity) AS quantidade_total_de_order_details
FROM order_details;
```

### Práticas Recomendadas

* **Precisão de dados**: Ao usar `AVG()` e `SUM()`, esteja ciente do tipo de dados da coluna para evitar imprecisões, especialmente com dados flutuantes.
* **NULLs**: Lembre-se de que a maioria das funções agregadas ignora valores `NULL`, exceto `COUNT(*)`, que conta todas as linhas, incluindo aquelas com valores `NULL`.
* **Performance**: Em tabelas muito grandes, operações agregadas podem ser custosas em termos de desempenho. Considere usar índices adequados ou realizar pré-agregações quando aplicável.
* **Clareza**: Ao usar `GROUP BY`, assegure-se de que todas as colunas não agregadas na sua cláusula `SELECT` estejam incluídas na cláusula `GROUP BY`.

### Exemplo de MIN() com GROUP BY

```sql
-- Calcula o menor preço unitário de produtos em cada categoria
SELECT category_id, MIN(unit_price) AS preco_minimo
FROM products
GROUP BY category_id;
```

### Exemplo de MAX() com GROUP BY

```sql
-- Calcula o maior preço unitário de produtos em cada categoria
SELECT category_id, MAX(unit_price) AS preco_maximo
FROM products
GROUP BY category_id;
```

### Exemplo de COUNT() com GROUP BY

```sql
-- Conta o número total de produtos em cada categoria
SELECT category_id, COUNT(*) AS total_de_produtos
FROM products
GROUP BY category_id;
```

### Exemplo de AVG() com GROUP BY

```sql
-- Calcula o preço médio unitário de produtos em cada categoria
SELECT category_id, AVG(unit_price) AS preco_medio
FROM products
GROUP BY category_id;
```

### Exemplo de SUM() com GROUP BY

```sql
-- Calcula a quantidade total de produtos pedidos por pedido
SELECT order_id, SUM(quantity) AS quantidade_total_por_pedido
FROM order_details
GROUP BY order_id;
```


```python
q1 = '''
SELECT category_id, MIN(unit_price) AS preco_minimo
FROM products
GROUP BY category_id;
'''
q2 = '''
SELECT category_id, MAX(unit_price) AS preco_maximo
FROM products
GROUP BY category_id;
'''
q3 = '''
SELECT category_id, COUNT(*) AS total_de_produtos
FROM products
GROUP BY category_id;
'''
q4 = '''
SELECT category_id, AVG(unit_price) AS preco_medio
FROM products
GROUP BY category_id;
'''
q5 = '''
SELECT order_id, SUM(quantity) AS quantidade_total_por_pedido
FROM order_details
GROUP BY order_id;
'''

queries = [q1,q2,q3,q4,q5]

# Executando todas a queries:
for query in queries:
    print(100 * "=")
    print(f"Resultado da query:{query}")
    print(100 * "=")
    display(pd.read_sql(query,conn))
```

    ====================================================================================================
    Resultado da query:
    SELECT category_id, MIN(unit_price) AS preco_minimo
    FROM products
    GROUP BY category_id;

    ====================================================================================================



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
      <th>category_id</th>
      <th>preco_minimo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8</td>
      <td>6.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>10.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>4.50</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>7.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>2.50</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>10.00</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>7.45</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3</td>
      <td>9.20</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    SELECT category_id, MAX(unit_price) AS preco_maximo
    FROM products
    GROUP BY category_id;

    ====================================================================================================



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
      <th>category_id</th>
      <th>preco_maximo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8</td>
      <td>62.50</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>53.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>263.50</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>38.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>55.00</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>43.90</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>123.79</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3</td>
      <td>81.00</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    SELECT category_id, COUNT(*) AS total_de_produtos
    FROM products
    GROUP BY category_id;

    ====================================================================================================



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
      <th>category_id</th>
      <th>total_de_produtos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>7</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>10</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>12</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3</td>
      <td>13</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    SELECT category_id, AVG(unit_price) AS preco_medio
    FROM products
    GROUP BY category_id;

    ====================================================================================================



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
      <th>category_id</th>
      <th>preco_medio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8</td>
      <td>20.682500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>32.370000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>37.979167</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>20.250000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>28.730000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>22.854167</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>54.006667</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3</td>
      <td>25.160000</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    SELECT order_id, SUM(quantity) AS quantidade_total_por_pedido
    FROM order_details
    GROUP BY order_id;

    ====================================================================================================



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
      <th>order_id</th>
      <th>quantidade_total_por_pedido</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11038</td>
      <td>37</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10782</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10725</td>
      <td>22</td>
    </tr>
    <tr>
      <th>3</th>
      <td>10423</td>
      <td>34</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10518</td>
      <td>29</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>825</th>
      <td>10707</td>
      <td>89</td>
    </tr>
    <tr>
      <th>826</th>
      <td>10826</td>
      <td>50</td>
    </tr>
    <tr>
      <th>827</th>
      <td>10371</td>
      <td>6</td>
    </tr>
    <tr>
      <th>828</th>
      <td>10575</td>
      <td>58</td>
    </tr>
    <tr>
      <th>829</th>
      <td>10809</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
<p>830 rows × 2 columns</p>
</div>


# Desafio

## 1. Obter todas as colunas das tabelas Clientes, Pedidos e Fornecedores


```python
q1 = '''
SELECT * FROM customers  LIMIT 5;'''
q2 ='''
SELECT * FROM orders  LIMIT 5;'''
q3='''
SELECT * FROM suppliers LIMIT 5;'''
queries = [q1,q2,q3]

# Executando todas a queries:
for query in queries:
    print(100 * "=")
    print(f"Resultado da query:{query}")
    print(100 * "=")
    display(pd.read_sql(query,conn))
```

    ====================================================================================================
    Resultado da query:
    SELECT * FROM customers  LIMIT 5;
    ====================================================================================================



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
      <th>customer_id</th>
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
      <td>ALFKI</td>
      <td>Alfreds Futterkiste</td>
      <td>Maria Anders</td>
      <td>Sales Representative</td>
      <td>Obere Str. 57</td>
      <td>Berlin</td>
      <td>None</td>
      <td>12209</td>
      <td>Germany</td>
      <td>030-0074321</td>
      <td>030-0076545</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ANATR</td>
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
      <th>2</th>
      <td>ANTON</td>
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
      <th>3</th>
      <td>AROUT</td>
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
      <td>BERGS</td>
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
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    SELECT * FROM orders  LIMIT 5;
    ====================================================================================================



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
      <th>ship_city</th>
      <th>ship_region</th>
      <th>ship_postal_code</th>
      <th>ship_country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10248</td>
      <td>VINET</td>
      <td>5</td>
      <td>1996-07-04</td>
      <td>1996-08-01</td>
      <td>1996-07-16</td>
      <td>3</td>
      <td>32.38</td>
      <td>Vins et alcools Chevalier</td>
      <td>59 rue de l'Abbaye</td>
      <td>Reims</td>
      <td>None</td>
      <td>51100</td>
      <td>France</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10249</td>
      <td>TOMSP</td>
      <td>6</td>
      <td>1996-07-05</td>
      <td>1996-08-16</td>
      <td>1996-07-10</td>
      <td>1</td>
      <td>11.61</td>
      <td>Toms Spezialitäten</td>
      <td>Luisenstr. 48</td>
      <td>Münster</td>
      <td>None</td>
      <td>44087</td>
      <td>Germany</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10250</td>
      <td>HANAR</td>
      <td>4</td>
      <td>1996-07-08</td>
      <td>1996-08-05</td>
      <td>1996-07-12</td>
      <td>2</td>
      <td>65.83</td>
      <td>Hanari Carnes</td>
      <td>Rua do Paço, 67</td>
      <td>Rio de Janeiro</td>
      <td>RJ</td>
      <td>05454-876</td>
      <td>Brazil</td>
    </tr>
    <tr>
      <th>3</th>
      <td>10251</td>
      <td>VICTE</td>
      <td>3</td>
      <td>1996-07-08</td>
      <td>1996-08-05</td>
      <td>1996-07-15</td>
      <td>1</td>
      <td>41.34</td>
      <td>Victuailles en stock</td>
      <td>2, rue du Commerce</td>
      <td>Lyon</td>
      <td>None</td>
      <td>69004</td>
      <td>France</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10252</td>
      <td>SUPRD</td>
      <td>4</td>
      <td>1996-07-09</td>
      <td>1996-08-06</td>
      <td>1996-07-11</td>
      <td>2</td>
      <td>51.30</td>
      <td>Suprêmes délices</td>
      <td>Boulevard Tirou, 255</td>
      <td>Charleroi</td>
      <td>None</td>
      <td>B-6000</td>
      <td>Belgium</td>
    </tr>
  </tbody>
</table>
</div>


    ====================================================================================================
    Resultado da query:
    SELECT * FROM suppliers LIMIT 5;
    ====================================================================================================



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
      <th>supplier_id</th>
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
      <th>homepage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Exotic Liquids</td>
      <td>Charlotte Cooper</td>
      <td>Purchasing Manager</td>
      <td>49 Gilbert St.</td>
      <td>London</td>
      <td>None</td>
      <td>EC1 4SD</td>
      <td>UK</td>
      <td>(171) 555-2222</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>New Orleans Cajun Delights</td>
      <td>Shelley Burke</td>
      <td>Order Administrator</td>
      <td>P.O. Box 78934</td>
      <td>New Orleans</td>
      <td>LA</td>
      <td>70117</td>
      <td>USA</td>
      <td>(100) 555-4822</td>
      <td>None</td>
      <td>#CAJUN.HTM#</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Grandma Kelly's Homestead</td>
      <td>Regina Murphy</td>
      <td>Sales Representative</td>
      <td>707 Oxford Rd.</td>
      <td>Ann Arbor</td>
      <td>MI</td>
      <td>48104</td>
      <td>USA</td>
      <td>(313) 555-5735</td>
      <td>(313) 555-3349</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Tokyo Traders</td>
      <td>Yoshi Nagase</td>
      <td>Marketing Manager</td>
      <td>9-8 Sekimai Musashino-shi</td>
      <td>Tokyo</td>
      <td>None</td>
      <td>100</td>
      <td>Japan</td>
      <td>(03) 3555-5011</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Cooperativa de Quesos 'Las Cabras'</td>
      <td>Antonio del Valle Saavedra</td>
      <td>Export Administrator</td>
      <td>Calle del Rosal 4</td>
      <td>Oviedo</td>
      <td>Asturias</td>
      <td>33007</td>
      <td>Spain</td>
      <td>(98) 598 76 54</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>


## 2. Obter todos os Clientes em ordem alfabética por país e nome


```python
query = '''
SELECT *
FROM customers
ORDER BY country, contact_name LIMIT 5;
'''
pd.read_sql(query, conn)
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
      <th>customer_id</th>
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
      <td>CACTU</td>
      <td>Cactus Comidas para llevar</td>
      <td>Patricio Simpson</td>
      <td>Sales Agent</td>
      <td>Cerrito 333</td>
      <td>Buenos Aires</td>
      <td>None</td>
      <td>1010</td>
      <td>Argentina</td>
      <td>(1) 135-5555</td>
      <td>(1) 135-4892</td>
    </tr>
    <tr>
      <th>1</th>
      <td>RANCH</td>
      <td>Rancho grande</td>
      <td>Sergio Gutiérrez</td>
      <td>Sales Representative</td>
      <td>Av. del Libertador 900</td>
      <td>Buenos Aires</td>
      <td>None</td>
      <td>1010</td>
      <td>Argentina</td>
      <td>(1) 123-5555</td>
      <td>(1) 123-5556</td>
    </tr>
    <tr>
      <th>2</th>
      <td>OCEAN</td>
      <td>Océano Atlántico Ltda.</td>
      <td>Yvonne Moncada</td>
      <td>Sales Agent</td>
      <td>Ing. Gustavo Moncada 8585 Piso 20-A</td>
      <td>Buenos Aires</td>
      <td>None</td>
      <td>1010</td>
      <td>Argentina</td>
      <td>(1) 135-5333</td>
      <td>(1) 135-5535</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PICCO</td>
      <td>Piccolo und mehr</td>
      <td>Georg Pipps</td>
      <td>Sales Manager</td>
      <td>Geislweg 14</td>
      <td>Salzburg</td>
      <td>None</td>
      <td>5020</td>
      <td>Austria</td>
      <td>6562-9722</td>
      <td>6562-9723</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ERNSH</td>
      <td>Ernst Handel</td>
      <td>Roland Mendel</td>
      <td>Sales Manager</td>
      <td>Kirchgasse 6</td>
      <td>Graz</td>
      <td>None</td>
      <td>8010</td>
      <td>Austria</td>
      <td>7675-3425</td>
      <td>7675-3426</td>
    </tr>
  </tbody>
</table>
</div>



## 3. Obter os 5 pedidos mais antigos


```python
query = '''
SELECT *
FROM orders
ORDER BY order_date
LIMIT 5;
'''
pd.read_sql(query, conn)
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
      <th>ship_city</th>
      <th>ship_region</th>
      <th>ship_postal_code</th>
      <th>ship_country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10248</td>
      <td>VINET</td>
      <td>5</td>
      <td>1996-07-04</td>
      <td>1996-08-01</td>
      <td>1996-07-16</td>
      <td>3</td>
      <td>32.38</td>
      <td>Vins et alcools Chevalier</td>
      <td>59 rue de l'Abbaye</td>
      <td>Reims</td>
      <td>None</td>
      <td>51100</td>
      <td>France</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10249</td>
      <td>TOMSP</td>
      <td>6</td>
      <td>1996-07-05</td>
      <td>1996-08-16</td>
      <td>1996-07-10</td>
      <td>1</td>
      <td>11.61</td>
      <td>Toms Spezialitäten</td>
      <td>Luisenstr. 48</td>
      <td>Münster</td>
      <td>None</td>
      <td>44087</td>
      <td>Germany</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10250</td>
      <td>HANAR</td>
      <td>4</td>
      <td>1996-07-08</td>
      <td>1996-08-05</td>
      <td>1996-07-12</td>
      <td>2</td>
      <td>65.83</td>
      <td>Hanari Carnes</td>
      <td>Rua do Paço, 67</td>
      <td>Rio de Janeiro</td>
      <td>RJ</td>
      <td>05454-876</td>
      <td>Brazil</td>
    </tr>
    <tr>
      <th>3</th>
      <td>10251</td>
      <td>VICTE</td>
      <td>3</td>
      <td>1996-07-08</td>
      <td>1996-08-05</td>
      <td>1996-07-15</td>
      <td>1</td>
      <td>41.34</td>
      <td>Victuailles en stock</td>
      <td>2, rue du Commerce</td>
      <td>Lyon</td>
      <td>None</td>
      <td>69004</td>
      <td>France</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10252</td>
      <td>SUPRD</td>
      <td>4</td>
      <td>1996-07-09</td>
      <td>1996-08-06</td>
      <td>1996-07-11</td>
      <td>2</td>
      <td>51.30</td>
      <td>Suprêmes délices</td>
      <td>Boulevard Tirou, 255</td>
      <td>Charleroi</td>
      <td>None</td>
      <td>B-6000</td>
      <td>Belgium</td>
    </tr>
  </tbody>
</table>
</div>



## 4. Obter a contagem de todos os Pedidos feitos durante 1997


```python
query = '''
SELECT COUNT(*) AS "Number of Orders During 1997"
FROM orders
WHERE order_date BETWEEN '1997-1-1' AND '1997-12-31';
'''
pd.read_sql(query, conn)
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
      <th>Number of Orders During 1997</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>408</td>
    </tr>
  </tbody>
</table>
</div>



## 5. Obter os nomes de todas as pessoas de contato onde a pessoa é um gerente, em ordem alfabética


```python
query = '''
SELECT contact_name
FROM customers
WHERE contact_title LIKE '%Manager%'
ORDER BY contact_name LIMIT 5;
'''
pd.read_sql(query, conn)
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
      <th>contact_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alejandra Camino</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Annette Roulet</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Art Braunschweiger</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bernardo Batista</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Carine Schmitt</td>
    </tr>
  </tbody>
</table>
</div>



## 6. Obter todos os pedidos feitos em 19 de maio de 1997


```python
query = '''
SELECT *
FROM orders
WHERE order_date = '1997-05-19';
'''
pd.read_sql(query, conn)
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
      <th>ship_city</th>
      <th>ship_region</th>
      <th>ship_postal_code</th>
      <th>ship_country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10540</td>
      <td>QUICK</td>
      <td>3</td>
      <td>1997-05-19</td>
      <td>1997-06-16</td>
      <td>1997-06-13</td>
      <td>3</td>
      <td>1007.64</td>
      <td>QUICK-Stop</td>
      <td>Taucherstraße 10</td>
      <td>Cunewalde</td>
      <td>None</td>
      <td>01307</td>
      <td>Germany</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10541</td>
      <td>HANAR</td>
      <td>2</td>
      <td>1997-05-19</td>
      <td>1997-06-16</td>
      <td>1997-05-29</td>
      <td>1</td>
      <td>68.65</td>
      <td>Hanari Carnes</td>
      <td>Rua do Paço, 67</td>
      <td>Rio de Janeiro</td>
      <td>RJ</td>
      <td>05454-876</td>
      <td>Brazil</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
