# Orientação a Objetos (OOP) versus Programação Funcional

## Orientação a Objetos (OOP):
A Orientação a Objetos (OOP) é um paradigma de programação que se baseia no conceito de "objetos", que podem conter dados na forma de campos (também conhecidos como atributos ou propriedades) e códigos na forma de procedimentos (métodos ou funções). Os objetos são instâncias de classes, que definem as estruturas e comportamentos dos objetos. Os principais conceitos da OOP incluem encapsulamento, herança e polimorfismo.

### Características da OOP:
1. **Encapsulamento:** O encapsulamento permite ocultar detalhes de implementação dentro de um objeto, expondo apenas a interface pública.
2. **Herança:** A herança permite que uma classe herde características e comportamentos de outra classe, promovendo a reutilização de código e a organização hierárquica de classes.
3. **Polimorfismo:** O polimorfismo permite que objetos de diferentes classes sejam tratados de maneira uniforme, fornecendo interfaces comuns para comportamentos diferentes.

## Programação Funcional:
A Programação Funcional é outro paradigma de programação que se concentra na avaliação de funções matemáticas e na aplicação de funções para transformar dados. Na programação funcional, as funções são tratadas como cidadãos de primeira classe, o que significa que elas podem ser atribuídas a variáveis, passadas como argumentos para outras funções e retornadas como resultados de outras funções.

### Características da Programação Funcional:
1. **Imutabilidade:** As estruturas de dados são imutáveis, o que significa que não podem ser modificadas após serem criadas. Em vez disso, as funções de transformação retornam novas estruturas de dados.
2. **Funções Puras:** As funções na programação funcional são consideradas "puras" se retornarem o mesmo resultado para os mesmos argumentos e não tiverem efeitos colaterais observáveis.
3. **Recursão:** A recursão é comumente usada na programação funcional em vez de loops iterativos.

## Diferenças entre OOP e Programação Funcional:
1. **Abordagem de Solução de Problemas:** Na OOP, os problemas são resolvidos pensando-se em objetos e suas interações, enquanto na programação funcional, os problemas são resolvidos pensando-se em funções e suas composições.
2. **Estado e Mutabilidade:** Na OOP, os objetos podem manter estados mutáveis, enquanto na programação funcional, as estruturas de dados geralmente são imutáveis.
3. **Ênfase na Mutabilidade:** Na OOP, a mutabilidade é frequentemente aceita e até mesmo incentivada, enquanto na programação funcional, a ênfase é na imutabilidade e na evitação de efeitos colaterais.

## Conclusão:
Tanto a Orientação a Objetos quanto a Programação Funcional são paradigmas de programação poderosos, cada um com suas próprias vantagens e casos de uso. A escolha entre eles depende do problema em questão, das preferências pessoais e das necessidades do projeto. Em muitos casos, é possível combinar elementos de ambos os paradigmas para criar soluções mais flexíveis e eficientes.

## Exemplo 01:

### criando um exemplo de arquivo csv para os testes:


```python
# Setando a raiz do projeto
import os
os.getcwd()
```




    '/home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/aula_11/notebook'




```python
os.chdir('/home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/aula_11')
```


```python
import site
print(site.getsitepackages())
```

    ['/home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.10/site-packages']


### Instalação da lib faker


```python
!poetry add faker -q
```


```python
import pandas as pd
from faker import Faker
import random

# Inicializa o Faker
fake = Faker('pt_BR')

# Gera dados de exemplo
dados = {
    'id': range(1, 11),
    'preço': [fake.numerify(text='##,##') for _ in range(10)],
    'estado': [fake.state_abbr() for _ in range(10)],
    'data': [fake.date(pattern="%d/%m/%Y") for _ in range(10)]
}

# Cria o dataframe
df = pd.DataFrame(dados)

# Salva o dataframe em um arquivo CSV com as colunas especificadas
df.to_csv('data/exemplo.csv', index=False)

```

### verificando o arquivo criado:


```python
# %load data/exemplo.csv
id,preço,estado,data
1,"55,41",BA,30/04/2009
2,"34,79",MG,13/11/1980
3,"02,14",AC,28/10/1986
4,"06,47",PR,07/08/2002
5,"24,07",PI,30/01/2001
6,"00,78",AM,14/10/1999
7,"41,09",AM,29/11/1975
8,"46,84",MT,27/01/1989
9,"06,03",TO,02/02/1993
10,"39,32",RN,11/09/2005

```

### Vamos realizar a seguinte estapa:

* **Extrair o arquivo.**
* **Realizar um filtro por Estado e por preço.**


```python

import pandas as pd


df = pd.read_csv('data/exemplo.csv')

df_filtrado = df[df['estado'] == 'AM']

df_filtrado = df[df['preço'] == '41,09']


print(df_filtrado)
```

       id  preço estado        data
    6   7  41,09     AM  29/11/1975


### Agora vamos realizar o mesmo filtro usando classes:


```python
import pandas as pd

class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.df_filtrado = None

    def carregar_csv(self) -> pd.DataFrame:
        self.df = pd.read_csv(self.file_path)
        return self.df

    def filtrar_por(self, colunas: list, atributos: list) -> pd.DataFrame:
        if len(colunas) != len(atributos):
            raise ValueError("O número de colunas e atributos não coincide")

        if not colunas:
            return self.df

        coluna_atual = colunas[0]
        atributo_atual = atributos[0]

        df_filtrado = self.df[self.df[coluna_atual] == atributo_atual]

        if len(colunas) == 1:
            return df_filtrado
        else:
            return self.filtrar_por(colunas[1:], atributos[1:])

```

CsvProcessor
=============

Esta classe fornece funcionalidades básicas para processar arquivos CSV.

Métodos
-------

- `__init__(file_path: str)`: Construtor da classe. Recebe o caminho do arquivo CSV como argumento.
- `carregar_csv() -> pd.DataFrame`: Carrega o arquivo CSV especificado e retorna um DataFrame pandas.
- `filtrar_por(colunas: list, atributos: list) -> pd.DataFrame`: Filtra o DataFrame por valores específicos nas colunas especificadas e retorna o DataFrame resultante.

### Exemplo de uso:


```python
# Criar uma instância de CsvProcessor com o caminho do arquivo CSV
processor = CsvProcessor('data/exemplo.csv')

# Carregar o arquivo CSV em um DataFrame
df = processor.carregar_csv()

# Filtrar o DataFrame por valores específicos nas colunas 'coluna1' e 'coluna2'
processor.filtrar_por(['estado', 'preço'], ['AM', '41,09'])
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
      <th>id</th>
      <th>preço</th>
      <th>estado</th>
      <th>data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>41,09</td>
      <td>AM</td>
      <td>29/11/1975</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
