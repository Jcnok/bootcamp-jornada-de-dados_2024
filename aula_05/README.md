# Projeto 01: Um Bilhão de Linhas: Desafio de Processamento de Dados com Python

![imagem_01](./img/bootcamp.jpg)

## Introdução

O objetivo deste projeto é demonstrar como processar eficientemente um arquivo de dados massivo contendo 1 bilhão de linhas (~14GB), especificamente para calcular estatísticas (Incluindo agregação e ordenação que são operações pesadas) utilizando Python. 

Este desafio foi inspirado no [The One Billion Row Challenge](https://github.com/gunnarmorling/1brc), originalmente proposto para Java, foi adaptado para o [bootcamp da jornada de dados 2024](https://www.jornadadedados2024.com.br/workshops)

O arquivo de dados consiste em medições de temperatura de várias cidades(dados ficticios). Cada registro segue o formato `<string: nome da estação>;<double: medição>`, com a temperatura sendo apresentada com precisão de uma casa decimal.

Aqui estão dez linhas de exemplo do arquivo:

```
Hamburg;12.0
Bulawayo;8.9
Palembang;38.8
St. Johns;15.2
Cracow;12.6
Bridgetown;26.9
Istanbul;6.2
Roseau;34.4
Conakry;31.2
Istanbul;23.0
```

O desafio é desenvolver um programa Python capaz de ler esse arquivo e calcular a temperatura mínima, média (arredondada para uma casa decimal) e máxima para cada cidade, exibindo os resultados em uma tabela ordenada por nome da estação.

| city      | min_temperature | mean_temperature | max_temperature |
|--------------|-----------------|------------------|-----------------|
| Abha         | -31.1           | 18.0             | 66.5            |
| Abidjan      | -25.9           | 26.0             | 74.6            |
| Abéché       | -19.8           | 29.4             | 79.9            |
| Accra        | -24.8           | 26.4             | 76.3            |
| Addis Ababa  | -31.8           | 16.0             | 63.9            |
| ...          | ...             | ...              | ...             |
| Zagreb       | -39.2           | 10.7             | 58.1            |
| Zanzibar City| -26.5           | 26.0             | 75.2            |
| Zürich       | -42.0           | 9.3              | 63.6            |
| Ürümqi       | -42.1           | 7.4              | 56.7            |
| İzmir        | -34.4           | 17.9             | 67.9            |



## Sobre:

Abaixo um índice como todas as etapas para resolução do projeto, desde informações sobre as configurações desktop, sobre a memória, ssd, como gerar os dados, dependências e o resultado do tempo de execução de cada script utilizados.

## índice

<a id="voltar"></a>

1.  **[Decoradores](#ancora01)**
2.  **[Scripts para gerar os dados.](#ancora02)**
3.  **[Pandas - min, max e mean em 1 bilhão de linhas](#ancora03)**
4.  **[Polars - min, max e mean em 1 bilhão de linhas](#ancora04)**
5.  **[Duckdb - min, max e mean em 1 bilhão de linhas](#ancora05)**
6.  **[Dask - min, max e mean em 1 bilhão de linhas](#ancora06)**
7.  **[Pyspark - min, max e mean em 1 bilhão de linhas.](#ancora07)**
8.  **[desenvolvimento](#ancora08)**
9.  **[desenvolvimento](#ancora09)**
10. **[desenvolvimento](#ancora10)**
11. **[desenvolvimento](#ancora11)**
12. **[desenvolvimento](#ancora12)**
13. **[desenvolvimento](#ancora13)**
14. **[desenvolvimento](#ancora14)**
15. **[desenvolvimento](#ancora15)**
16. **[desenvolvimento](#desafio)**


<a id="ancora01"></a>
## Decoradores

**O decorator timer serve para medir o tempo de execução de uma função e registrar o resultado em um arquivo CSV. Ele também imprime o tempo de execução no console.**

**Porquê usar decorators?**
* Nesse exemplo precisamos medir o tempo de cada uma das funções que serão criadas para determinar a melhor performance, dessa forma podemos criar uma função mais limpa e organizada onde iremos chamar o decorator para exibir e registrar as informações do tempo de execução da cada uma das funções, isso evita a duplicidade de código.

* Funcionalidades:

    - Mede o tempo de execução da função decorada.
    - Formata o tempo em horas, minutos e segundos.
    - Registra o nome da função e o tempo de execução em um arquivo CSV chamado tempos_execucao.csv.
    - Imprime o nome da função e o tempo de execução no console.
* Vantagens de usar decorators:

    - Códigos mais concisos e reutilizáveis.
    - Evita a duplicação de código para medição de tempo.
    - Facilita a comparação do tempo de execução de diferentes funções.
    - Permite a criação de logs de performance.

* **Decorator para salvar os resultado em um csv**.


```python
%%writefile src/utils/decorators.py 
#decorator para registrar o tempo de execução da função em um .csv
import time
import csv
import threading  # Importe o módulo threading aqui

def timer_to_csv(func):
    def format_time(segundos: int): 
        """
        Formata os milisegundos em hora:minuto:segundo
        """
        if segundos < 60:
            return f"{segundos:.3f} segundos"
        elif segundos < 3600:
            minutos, segundos = divmod(segundos, 60)
            return f"{int(minutos)} minutos {int(segundos)} segundos"
        else:
            horas, remainder = divmod(segundos, 3600)
            minutos, segundos = divmod(remainder, 60)
            if minutos == 0:
                return f"{int(horas)} horas {int(segundos)} segundos"
            else:
                return f"{int(horas)} horas {int(minutos)} minutos {int(segundos)} segundos"
    
    def print_elapsed_time(start_time, finished_flag):
        while not finished_flag.is_set():
            elapsed_time = time.time() - start_time
            print(f"Tempo decorrido: {format_time(elapsed_time)}", end="\r")
            time.sleep(1)  # Atualiza a cada segundo

    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        # Inicializa um sinalizador booleano para indicar se a função terminou
        finished_flag = threading.Event()
        
        # Iniciar uma thread para imprimir o tempo decorrido em tempo real
        thread = threading.Thread(target=print_elapsed_time, args=(start_time, finished_flag))
        thread.start()
        
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"Tempo total de execução: {format_time(elapsed_time)}")
        
        # Sinaliza que a função terminou
        finished_flag.set()
        
        # Salvando o nome da função e o tempo de execução em um arquivo CSV
        with open('data/tempos_execucao.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([func.__name__, format_time(elapsed_time)])
        
        return result    
    return wrapper

```

    Overwriting src/utils/decorators.py


[voltar](#voltar)

<a id="ancora02"></a>
## Scripts para gerar os dados.

### Scrip python para gerar dados aleatórios
* **O script foi retirado do desafio [The One Billion Row Challenge](https://github.com/gunnarmorling/1brc), originalmente proposto para Java.**
* **Algumas alterações foram realizadas, como por exemplo a temp máxima e mínima foram alterados para valores históricos reais.**


```python
%%time
# Script para gerar 1 bilhão de linhas com dados aleatórios.
# Based on https://github.com/gunnarmorling/1brc/blob/main/src/main/java/dev/morling/onebrc/Createtempments.java

import os
import sys
import random
import time


def check_args(file_args):
    """
    Sanity checks out input and prints out usage if input is not na positive integer
    """
    try:
        if len(file_args) != 2 or int(file_args[1]) <= 0:
            raise Exception()
    except:
        print("Usage:  create_tempments.sh <positive integer number of records to create>")
        print("        You can use underscore notation for large number of records.")
        print("        For example:  1_000_000_000 for one billion")
        exit()


def build_weather_city_name_list():
    """
    Grabs the weather city names from example data provided in repo and dedups
    
    """   
    city_names = []
    with open('data/weather_stations.csv', 'r') as file:

        file_contents = file.read()
    for city in file_contents.splitlines():
        if "#" in city:
            next
        else:
            city_names.append(city.split(';')[0])
    return list(set(city_names))


def convert_bytes(num):
    """
    Convert bytes to a human-readable format (e.g., KiB, MiB, GiB)
    """
    for x in ['bytes', 'KiB', 'MiB', 'GiB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def format_elapsed_time(seconds):
    """
    Format elapsed time in a human-readable format
    """
    if seconds < 60:
        return f"{seconds:.3f} seconds"
    elif seconds < 3600:
        minutes, seconds = divmod(seconds, 60)
        return f"{int(minutes)} minutes {int(seconds)} seconds"
    else:
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if minutes == 0:
            return f"{int(hours)} hours {int(seconds)} seconds"
        else:
            return f"{int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds"


def estimate_file_size(weather_city_names, num_rows_to_create):
    """
    Tries to estimate how large a file the test data will be
    """
    total_name_bytes = sum(len(s.encode("utf-8")) for s in weather_city_names)
    avg_name_bytes = total_name_bytes / float(len(weather_city_names))

    # avg_temp_bytes = sum(len(str(n / 10.0)) for n in range(-999, 1000)) / 1999
    avg_temp_bytes = 4.400200100050025

    # add 2 for separator and newline
    avg_line_length = avg_name_bytes + avg_temp_bytes + 2

    human_file_size = convert_bytes(num_rows_to_create * avg_line_length)

    return f"Estimated max file size is:  {human_file_size}."


def build_test_data(weather_city_names, num_rows_to_create):
    """
    Generates and writes to file the requested length of test data
    """
    start_time = time.time()
    coldest_temp = -89.2
    hottest_temp = 56.7
    city_names_10k_max = random.choices(weather_city_names, k=10_000)
    batch_size = 10000 # instead of writing line by line to file, process a batch of citys and put it to disk
    chunks = num_rows_to_create // batch_size
    print('Building test data...')

    try:
        with open("data/measurements.txt", 'w') as file:
            progress = 0
            for chunk in range(chunks):
                
                batch = random.choices(city_names_10k_max, k=batch_size)
                prepped_deviated_batch = '\n'.join([f"{city};{random.uniform(coldest_temp, hottest_temp):.1f}" for city in batch]) # :.1f should quicker than round on a large scale, because round utilizes mathematical operation
                file.write(prepped_deviated_batch + '\n')

                
                # Update progress bar every 1%
                if (chunk + 1) * 100 // chunks != progress:
                    progress = (chunk + 1) * 100 // chunks
                    bars = '=' * (progress // 2)
                    sys.stdout.write(f"\r[{bars:<50}] {progress}%")
                    sys.stdout.flush()
        sys.stdout.write('\n')
    except Exception as e:
        print("Something went wrong. Printing error info and exiting...")
        print(e)
        exit()
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    file_size = os.path.getsize("data/measurements.txt")
    human_file_size = convert_bytes(file_size)
 
    print("Test data successfully written to data/measurements.txt")
    print(f"Actual file size:  {human_file_size}")
    print(f"Elapsed time: {format_elapsed_time(elapsed_time)}")


def main():
    """
    main program function
    """
    num_rows_to_create = 500_000_000
    weather_city_names = []
    weather_city_names = build_weather_city_name_list()
    print(estimate_file_size(weather_city_names, num_rows_to_create))
    build_test_data(weather_city_names, num_rows_to_create)
    print("Test data build complete.")


if __name__ == "__main__":
    main()
exit()
```

    Estimated max file size is:  7.4 GiB.
    Building test data...
    [==================================================] 100%
    Test data successfully written to data/measurements1.txt
    Actual file size:  7.4 GiB
    Elapsed time: 7 minutes 45 seconds
    Test data build complete.
    CPU times: user 7min 34s, sys: 11.1 s, total: 7min 45s
    Wall time: 7min 45s


#### Como executar o script:
$`cd aula_05/src/` #para acessar a pasta dos scripts. 

$`python data_generate.py`#para criar os dados na pasta 'data/mesurements.txt'

* **obs**: O script depende do arquivo 'data/weather_stations.csv' para gerar os dados das cidades.



* **Agora com os dados de 1 bilhao gerados vamos ver quem se sai melhor para as configuracoes da minha maquina**.

[voltar](#voltar)

<a id="ancora03"></a>
## Pandas - min, max e mean em 1 bilhão de linhas


```python
# Instalando a lib pandas.
!poetry add pandas tabulate -q
```

### Documentação do Script Python: Calculando Mínimo, Máximo e Média para um Bilhão de Linhas

Este script calcula a temperatura mínima, máxima e média para cada cidade em um grande conjunto de dados contendo um bilhão de linhas. Ele utiliza as bibliotecas Pandas, multiprocessing e tqdm.

**Funcionalidade:**

1. **Leitura de dados:** 
    * Lê dados de um arquivo CSV (`data/measurements.txt`) com colunas nomeadas `cidade` e `temp`.
    * Emprega fragmentação para processar os dados em partes menores e gerenciáveis.

2. **Processamento paralelo:**
    * Aproveita o multiprocessing para distribuir a carga de trabalho entre os núcleos de CPU disponíveis.
    * Cada fragmento é processado independentemente pela função `process_chunk`.

3. **Agregação:**
    * Dentro de cada fragmento, a função `process_chunk` usa Pandas para:
        * Agrupar dados por `cidade`.
        * Calcular o `max`, `min` e `mean` da coluna `temp`.
        * Redefinir o índice para obter um DataFrame limpo.

4. **Agregação de resultados:**
    * Resultados de fragmentos individuais são concatenados em um único DataFrame.
    * Uma agregação final é realizada para calcular o `max`, `min` e `mean` geral para cada cidade.
    * O DataFrame final é classificado por `cidade`.

5. **Visualização do progresso:**
    * A biblioteca tqdm fornece uma barra de progresso para visualizar o processamento dos fragmentos.

**Principais características:**

* **Processamento eficiente de grandes conjuntos de dados:** A fragmentação e o multiprocessing permitem lidar com dados massivos com eficiência.
* **Desempenho otimizado:** A utilização de vários núcleos reduz significativamente o tempo de processamento.

**Observações:**

* Certifique-se de que a variável `filename` aponte para o local correto do arquivo de dados `data/measurements.txt`.
* Ajuste `chunksize` dependendo da memória do seu sistema e dos recursos de processamento.

**Documentação**: [Pandas](https://pandas.pydata.org/docs/)

**Como executar o script:**

1. **Terminal Bash digite:** `cd aula_05`
2. **Execute o script:** Digite o seguinte comando e pressione Enter: 
```bash
python src/pandas_df.py



```python
!python src/pandas_df.py
```

    Iniciando o processamento do arquivo.
    Tempo total de execução: 12 minutos 19 segundos
                      city   max   min   mean
    0             A Coruña  56.7 -89.2 -16.29
    1               Aachen  56.7 -89.2 -16.27
    2                Aalst  56.7 -89.2 -16.50
    3                Aarau  56.7 -89.2 -16.14
    4                Abaré  56.7 -89.2 -16.42
    ...                ...   ...   ...    ...
    8849  ‘Alīābād-e Katūl  56.7 -89.2 -16.22
    8850            ‘Amrān  56.7 -89.2 -16.08
    8851           ‘Anadān  56.7 -89.2 -16.26
    8852   ’Ayn Bni Mathar  56.7 -89.2 -16.10
    8853   ’Tlat Bni Oukil  56.7 -89.2 -16.25
    
    [8854 rows x 4 columns]


### Script Pandas_df:


```python
%%writefile src/pandas_df.py
import pandas as pd 
import time
from multiprocessing import Pool, cpu_count
from utils.decorators import timer_to_csv  # Importa o decorador
#from tabulate import tabulate

CONCURRENCY = cpu_count()

total_linhas = 1_000_000_000  # Total de linhas conhecido
chunksize = 1_000_000  # Define o tamanho do chunk
filename = "data/measurements.txt"  # Certifique-se de que este é o caminho correto para o arquivo


def process_chunk(chunk):
    # Agrega os dados dentro do chunk usando Pandas
    aggregated = chunk.groupby('city')['temp'].agg(['max','min','mean']).reset_index()
    return aggregated

@timer_to_csv  # Aplica o decorador
def create_df_with_pandas(filename, total_linhas, chunksize=chunksize):
    total_chunks = total_linhas // chunksize + (1 if total_linhas % chunksize else 0)

    with pd.read_csv(filename, sep=';', header=None, names=['city', 'temp'], chunksize=chunksize) as reader:
        with Pool(CONCURRENCY) as pool:
            results = []
            for result in pool.imap(process_chunk, reader):
                results.append(result)

    final_df = pd.concat(results, ignore_index=True)

    final_aggregated_df = final_df.groupby('city').agg({
        'max': 'max',
        'min': 'min',
        'mean': 'mean'
        
    }).reset_index().round(2).sort_values('city')

    return final_aggregated_df

if __name__ == "__main__":    
    print("Iniciando o processamento do arquivo.")
    printcreate_df_with_pandas(filename, total_linhas, chunksize)
    #print(tabulate(df, headers='keys', tablefmt='pretty'))
     
```

[voltar](#voltar)

<a id="ancora04"></a>
## Polars - min, max e mean em 1 bilhão de linhas


```python
# Instalando a lib polars
!poetry add polars
```

### Documentação do Script `polars_df.py`

Este script Python utiliza a biblioteca Polars para calcular de forma eficiente a temperatura mínima, máxima e média para cada cidade em um conjunto de dados grande (por exemplo, um bilhão de linhas). 

**Funcionalidade:**

1. **Importações:**
    * Importa a função `timer_to_csv` do módulo `utils.decorators`. 
    * Importa a biblioteca `polars` como `pl`.

2. **Configuração do Polars:**
    * Define o tamanho do chunk para processamento de streaming como 100.000 linhas usando `pl.Config.set_streaming_chunk_size(100000)`. Isso otimiza o uso de memória ao lidar com grandes conjuntos de dados.

3. **Função `polars_df()`:**
    * Esta função é decorada com `@timer_to_csv`, que mede o tempo de execução e salva os resultados em um arquivo CSV.
    * Lê o arquivo CSV `data/measurements.txt` com as seguintes características:
        * Separador: `;`
        * Sem cabeçalho (`has_header=False`)
        * Esquema de colunas: `{"city": pl.String, "temp": pl.Float64}`
    * Agrupa os dados por `city`.
    * Calcula as seguintes estatísticas para cada cidade:
        * Temperatura máxima (`max_temp`)
        * Temperatura mínima (`min_temp`)
        * Temperatura média (`mean_temp`)
    * Ordena os resultados por `city`.
    * Coleta os resultados em um DataFrame Polars usando `collect(streaming=True)` para processamento eficiente de grandes conjuntos de dados.
    * Retorna o DataFrame Polars resultante.

4. **Execução principal:**
    * Se o script for executado diretamente (e não importado como um módulo), a função `polars_df()` é chamada e o DataFrame resultante é impresso no console.

**Principais características:**

* **Processamento eficiente de grandes conjuntos de dados:** O Polars é otimizado para lidar com grandes conjuntos de dados, utilizando processamento em chunks e técnicas eficientes de gerenciamento de memória.
* **Sintaxe expressiva:** A API do Polars permite realizar a análise de dados de forma concisa e legível.
* **Desempenho:** O Polars é frequentemente mais rápido que o Pandas, especialmente em grandes conjuntos de dados.

**Documentação:** [Polars](https://docs.pola.rs/#philosophy)

Este script demonstra como o Polars pode ser usado para processar grandes conjuntos de dados de forma eficiente e calcular estatísticas básicas. 

**Como executar o script:**

1. **Terminal Bash digite:** `cd aula_05`
2. **Execute o script:** Digite o seguinte comando e pressione Enter: 
```bash
python src/polars_df.py


```python
!python src/polars_df.py
```

    Tempo total de execução: 47.205 segundos
    shape: (8_854, 4)
    ┌──────────────────┬──────────┬──────────┬────────────┐
    │ city             ┆ max_temp ┆ min_temp ┆ mean_temp  │
    │ ---              ┆ ---      ┆ ---      ┆ ---        │
    │ str              ┆ f64      ┆ f64      ┆ f64        │
    ╞══════════════════╪══════════╪══════════╪════════════╡
    │ A Coruña         ┆ 56.7     ┆ -89.2    ┆ -16.284529 │
    │ Aachen           ┆ 56.7     ┆ -89.2    ┆ -16.263415 │
    │ Aalst            ┆ 56.7     ┆ -89.2    ┆ -16.487183 │
    │ Aarau            ┆ 56.7     ┆ -89.2    ┆ -16.132312 │
    │ Abaré            ┆ 56.7     ┆ -89.2    ┆ -16.397278 │
    │ …                ┆ …        ┆ …        ┆ …          │
    │ ‘Alīābād-e Katūl ┆ 56.7     ┆ -89.2    ┆ -16.228978 │
    │ ‘Amrān           ┆ 56.7     ┆ -89.2    ┆ -16.081336 │
    │ ‘Anadān          ┆ 56.7     ┆ -89.2    ┆ -16.288188 │
    │ ’Ayn Bni Mathar  ┆ 56.7     ┆ -89.2    ┆ -16.094876 │
    │ ’Tlat Bni Oukil  ┆ 56.7     ┆ -89.2    ┆ -16.255552 │
    └──────────────────┴──────────┴──────────┴────────────┘


### Script Polars_df.py


```python
%%writefile src/polars_df.py
# Polars => script para caluclar min, max e mean em um bilhão de linhas.
from utils.decorators import timer_to_csv
import polars as pl
@timer_to_csv
def polars_df(): 
    pl.Config.set_streaming_chunk_size(100000)
    # Leitura do arquivo CSV e definição do schema
    return (pl.scan_csv("data/measurements.txt", separator=";", has_header=False,
                        schema={"city": pl.String, "temp": pl.Float64})
                        .group_by("city").agg(
                                                 max_temp=pl.col("temp").max(),
                                                 min_temp=pl.col("temp").min(),
                                                 mean_temp=pl.col("temp").mean()
                                                ).sort("city").collect(streaming=True)
           )   
if __name__ == "__main__":    
    df = polars_df()
    print(df)
   

```

    Overwriting src/polars_df.py


[voltar](#voltar)

<a id="ancora05"></a>
## Duckdb - min, max e mean em 1 bilhão de linhas


```python
!poetry add duckdb
```

### Documentação do Script `duckdb_df.py`

Este script Python utiliza a biblioteca DuckDB para calcular de forma eficiente a temperatura mínima, máxima e média para cada cidade em um conjunto de dados grande (por exemplo, um bilhão de linhas). 

**Funcionalidade:**

1. **Importações:**
    * Importa a função `timer_to_csv` do módulo `utils.decorators`. 
    * Importa a biblioteca `duckdb`.

2. **Função `duckdb_df()`:**
    * Esta função é decorada com `@timer_to_csv`, que mede o tempo de execução e salva os resultados em um arquivo CSV.
    * Executa uma consulta SQL no DuckDB para:
        * Ler o arquivo CSV `data/measurements.txt` com as seguintes características:
            * Detecção automática de tipo de dados desativada (`AUTO_DETECT=FALSE`)
            * Separador: `;`
            * Colunas: `city` (VARCHAR) e `temp` (DECIMAL)
        * Agrupar os dados por `city`.
        * Calcular as seguintes estatísticas para cada cidade:
            * Temperatura máxima (`max_temp`)
            * Temperatura mínima (`min_temp`)
            * Temperatura média (`mean_temp`) - convertida para DECIMAL
        * Ordenar os resultados por `city`.
    * Exibe os resultados da consulta no console.

3. **Execução principal:**
    * Se o script for executado diretamente (e não importado como um módulo), a função `duckdb_df()` é chamada.

**Documentação:** [Duckdb](https://duckdb.org/docs/)

**Como executar o script:**

1. **Terminal Bash digite:** `cd aula_05`
2. **Execute o script:** Digite o seguinte comando e pressione Enter: 
```bash
python src/duckdb_df.py


```python
!python src/duckdb_df.py
```

                      city  max_temp  min_temp  mean_temp
    0             A Coruña      56.7     -89.2    -16.285
    1               Aachen      56.7     -89.2    -16.263
    2                Aalst      56.7     -89.2    -16.487
    3                Aarau      56.7     -89.2    -16.132
    4                Abaré      56.7     -89.2    -16.397
    ...                ...       ...       ...        ...
    8849  ‘Alīābād-e Katūl      56.7     -89.2    -16.229
    8850            ‘Amrān      56.7     -89.2    -16.081
    8851           ‘Anadān      56.7     -89.2    -16.288
    8852   ’Ayn Bni Mathar      56.7     -89.2    -16.095
    8853   ’Tlat Bni Oukil      56.7     -89.2    -16.256
    
    [8854 rows x 4 columns]
    Tempo total de execução: 19.372 segundos


### Script Duck_db:


```python
%%writefile src/duckdb_df.py
# Duckdb => script para caluclar min, max e mean em um bilhão de linhas.
from utils.decorators import timer_to_csv
import duckdb
@timer_to_csv
def create_duckdb(): 
    conn = duckdb.connect(':memory:')    
    print(conn.execute("""
            SELECT city,
                MAX(temp) AS max_temp,
                MIN(temp) AS min_temp,
                CAST(AVG(temp) AS DECIMAL()) AS mean_temp                
            FROM read_csv("data/measurements.txt", AUTO_DETECT=FALSE, sep=';', columns={'city':VARCHAR, 'temp': 'DECIMAL'})
            GROUP BY city
            ORDER BY city
        """).df())
    
if __name__ == "__main__":
    create_duckdb()   
```

    Overwriting src/duckdb_df.py


[voltar](#voltar)

<a id="ancora06"></a>
## Dask - min, max e mean em 1 bilhão de linhas


```python
#necessário Instalar.
!pip install dask-expr
```

### Documentação do Script Dask:

**Descrição:**

Este script demonstra como calcular a temperatura mínima, máxima e média para cada cidade em um conjunto de dados massivo contendo um bilhão de linhas. Ele utiliza as bibliotecas Dask para otimizar o processamento e fornecer uma experiência interativa.

**Funcionalidade:**

**1. Leitura de dados:**

* Lê dados de um arquivo CSV (`data/measurements.txt`) com colunas nomeadas `city` e `temp`.
* Emprega a biblioteca Dask para ler o arquivo em um DataFrame particionado, permitindo processamento eficiente em grandes conjuntos de dados.

**2. Processamento paralelo:**

* O Dask gerencia o particionamento e o processamento paralelo do DataFrame em diferentes threads ou processos.
* Cada partição é processada independentemente pela função `process_chunk`.

**3. Agregação:**

* Dentro de cada partição, a função `process_chunk` usa Pandas para:
    * Agrupar dados por `city`.
    * Calcular o `max`, `min` e `mean` da coluna `temp`.
    * Redefinir o índice para obter um DataFrame limpo.

**4. Agregação de resultados:**

* Os resultados de cada partição são combinados em um único DataFrame.
* Uma agregação final é realizada para calcular o `max`, `min` e `mean` geral para cada cidade.
* O DataFrame final é ordenado por `city`.

**Características:**

* **Processamento eficiente de grandes conjuntos de dados:** O Dask permite lidar com dados massivos de forma eficiente e escalável.
* **Desempenho otimizado:** O processamento paralelo em partições reduz significativamente o tempo de processamento.

**Observações:**

* Certifique-se de que a variável `filename` aponte para o local correto do arquivo de dados `data/measurements.txt`.
* Ajuste o tamanho da partição (`chunksize`) de acordo com a memória do seu sistema e os recursos de processamento.
* Se necessário, configure o Dask para usar um cluster de computação para aumentar ainda mais o desempenho.

**Documentação:** [Dask](https://docs.dask.org/en/stable/)

**Execução:**

1. **Navegue até o diretório do script:** `cd aula_05`
2. **Execute o script:** `python src/dask_df.py`



```python
!python src/dask_df.py
```

                      temp             dos
                       max   min   mean
    city                               
    A Coruña          56.7 -89.2 -16.28
    Aachen            56.7 -89.2 -16.26
    Aalst             56.7 -89.2 -16.49
    Aarau             56.7 -89.2 -16.13
    Abaré             56.7 -89.2 -16.40
    ...                ...   ...    ...
    ‘Alīābād-e Katūl  56.7 -89.2 -16.23
    ‘Amrān            56.7 -89.2 -16.08
    ‘Anadān           56.7 -89.2 -16.29
    ’Ayn Bni Mathar   56.7 -89.2 -16.09
    ’Tlat Bni Oukil   56.7 -89.2 -16.26
    
    [8854 rows x 3 columns]
    Tempo total de execução: 7 minutos 41 segundos


### Script Dask_df:


```python
%%writefile src/dask_df.py
# Dask => script para caluclar min, max e mean em um bilhão de linhas.
from utils.decorators import timer_to_csv
import dask
dask.config.set({'dataframe.query-planning': True})
import dask.dataframe as dd
@timer_to_csv
def dask_df():    
    # Ler o arquivo txt diretamente em um DataFrame Dask
    df = dd.read_csv('data/measurements.txt', delimiter=';', 
                     header=None, names=['city', 'temp'])
    # min, max, e mean pela cidade ordenado pelo index
    return print(df.groupby('city').
                   agg({'temp': ['max','min','mean']}).
                   compute().round(2).sort_index())

if __name__ == "__main__":
    dask_df()
```

    Writing src/dask_df.py


[voltar](#voltar)

<a id="ancora07"></a>
## Pyspark - min, max e mean em 1 bilhão de linhas.


```python
#instalação da lib
!poetry add pyspark
```

### Documentação do Script PySpark:

**Descrição:**

Este script demonstra como calcular a temperatura mínima, máxima e média para cada cidade em um conjunto de dados massivo contendo um bilhão de linhas utilizando a biblioteca PySpark.

**Funcionalidade:**

**1. Inicialização da sessão Spark:**

* Cria um objeto `SparkSession` para interagir com o cluster Spark.
* Define o nome da aplicação como "Temperature Analysis".

**2. Leitura de dados:**

* Lê o arquivo CSV `data/measurements.txt` diretamente em um DataFrame Spark.
* Especifica que o arquivo não possui cabeçalho e usa ponto-e-vírgula como delimitador.
* Define os nomes das colunas como "City" e "Temperature".

**3. Conversão de tipo:**

* Converte a coluna "Temperature" para o tipo numérico `float` para possibilitar cálculos.

**4. Cálculo de estatísticas:**

* Agrupa o DataFrame por "City".
* Calcula o máximo, mínimo e média da temperatura para cada cidade utilizando funções Spark SQL.
* Arredonda o valor médio da temperatura para duas casas decimais.

**5. Ordenação:**

* Ordena as estatísticas pela coluna "City".

**6. Exibição de resultados:**

* Imprime o DataFrame com as estatísticas na tela.

**7. Encerramento da sessão Spark:**

* Libera recursos utilizados pelo Spark.

**Características:**

* **Processamento distribuído:** PySpark distribui o processamento por múltiplos nós em um cluster, permitindo lidar com conjuntos de dados massivos de maneira eficiente.
* **Otimização para grandes dados:** PySpark oferece otimizações específicas para manipular grandes volumes de dados.
* **Linguagem SQL familiar:** Usa Spark SQL para realizar consultas e transformações nos dados, facilitando a utilização para quem conhece SQL.

**Observações:**

* Certifique-se de ter o PySpark instalado e configurado corretamente.
* O arquivo `data/measurements.txt` deve existir no caminho especificado.
* A função `timer_to_csv` salva o tempo de execução em um arquivo CSV.

**Documentação:** [pyspark](https://spark.apache.org/docs/latest/api/python/index.html)

**Execução:**

1. **Navegue até o diretório do script:** `cd aula_05`
2. **Execute o script:** `python src/pyspark_df.py`


```python
!python src/pyspark_df.py
```

    24/03/23 00:04:12 WARN Utils: Your hostname, DESKTOP-AN64GAS resolves to a loopback address: 127.0.1.1; using 172.25.237.139 instead (on interface eth0)
    24/03/23 00:04:12 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
    Setting default log level to "WARN".
    To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
    24/03/23 00:04:14 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
    +------------+---------------+---------------+---------------+                  
    |        City|Max Temperature|Min Temperature|Avg Temperature|
    +------------+---------------+---------------+---------------+
    |    A Coruña|           56.7|          -89.2|         -16.28|
    |      Aachen|           56.7|          -89.2|         -16.26|
    |       Aalst|           56.7|          -89.2|         -16.49|
    |       Aarau|           56.7|          -89.2|         -16.13|
    |       Abaré|           56.7|          -89.2|          -16.4|
    |   Abbeville|           56.7|          -89.2|         -16.17|
    |  Abbotsford|           56.7|          -89.2|         -16.42|
    | Aberbargoed|           56.7|          -89.2|         -16.13|
    |     Abidjan|           56.7|          -89.2|         -16.14|
    |    Abingdon|           56.7|          -89.2|         -16.25|
    |        Ablu|           56.7|          -89.2|         -16.18|
    |       Abony|           56.7|          -89.2|         -16.26|
    |     Absecon|           56.7|          -89.2|         -16.35|
    |       Abuja|           56.7|          -89.2|         -16.38|
    |       Abunã|           56.7|          -89.2|         -15.96|
    |      Abuyog|           56.7|          -89.2|         -16.21|
    |Abū Ḩulayfah|           56.7|          -89.2|         -16.41|
    |  Acapetahua|           56.7|          -89.2|         -16.32|
    |     Acarlar|           56.7|          -89.2|          -16.0|
    |       Acará|           56.7|          -89.2|         -16.26|
    +------------+---------------+---------------+---------------+
    only showing top 20 rows
    
    Tempo total de execução: 3 minutos 29 segundos


### Script pyspark_df:


```python
%%writefile src/pyspark_df.py
# Pyspark => script para caluclar min, max e mean em um bilhão de linhas.
from utils.decorators import timer_to_csv
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, min as spark_min, max as spark_max, avg as spark_avg, round as spark_round

@timer_to_csv
def pyspark_df():     
    # Inicializar uma sessão Spark
    spark = SparkSession.builder \
        .appName("Temperature Analysis") \
        .getOrCreate()
    
    # Ler o arquivo CSV diretamente em um DataFrame Spark
    df = spark.read.option("header", "false").option("delimiter", ";").csv("data/measurements.txt") \
        .toDF("City", "Temperature")
    
    # Converter a coluna 'Temperature' para tipo numérico
    df = df.withColumn("Temperature", col("Temperature").cast("float"))
    
    # Calcular estatísticas usando Spark SQL
    statistics = df.groupBy("City") \
        .agg(spark_max("Temperature").alias("Max Temperature"),
             spark_min("Temperature").alias("Min Temperature"),             
             spark_round(spark_avg("Temperature"),2).alias("Avg Temperature"))
    
    # Ordenar as estatísticas pela cidade
    statistics_sorted = statistics.orderBy("City")
    
    # Mostrar as estatísticas
    return statistics_sorted.show()
    
    # Encerrar a sessão Spark
    spark.stop()

if __name__ == "__main__":
    pyspark_df()  

```

    Writing src/pyspark_df.py


[voltar](#voltar)

## Vaex - min, max e mean em 1 bilhão de linhas.

### Preparando o ambiente:
* **[Vaex](https://pypi.org/project/vaex/) tem compatibilidade apenas com a versão: 3.10.13.**
* **Nesse caso será necessario criar um novo ambiente virtual para que a instalação seja possível.**
* **Passos**:
  
  * Verfifique se já possui a versão 3.10.13 com `pyenv versions`
  * 
  * Crie um novo ambiente virtual com a versão python 3.10.13 :
    * `$ poetry env use 3.10.13

* Feche o jupyter lab, acesso o terminal e encerre o ambiente virtual `deactivate` ou se `exit`:
  ```
  $ exit

* Verfifique se já possui a versão 3.10.13 com `pyenv versions`


```python
#Verifica as versão já instaladoas do pyenv.
!pyenv versions
```

      system
      3.10.13
    * 3.11.3 (set by PYENV_VERSION environment variable)
      3.11.5
      3.12.1


* Caso não possua use o comando abaixo:
```bash
$ pyenv update
$ pyenv install 3.10.13

* Verifique os ambientes virtuais já configurados na maquina:mm


```python
!poetry env exit
```

    
    [31;1mThe command "env" does not exist.
    
    Did you mean one of these?
        env use
        env info
        env list
        env remove[39;22m


* Crie um novo ambiente virtual com a versão python 3.10.13:
```bash 
$ 


```python

```

* **Para utilizar o Vaex foi necessário selecionar outro kernel com python 3.10.13.**


```python
!python --version
```

    Python 3.10.13



```python
# Vaex => script para caluclar min, max e mean.
import vaex
@timer
def create_vaex(filename):
    # Leitura do arquivo CSV utilizando Vaex
    df = vaex.from_csv(filename, names=['city', 'temp'], sep=';')

    # Cálculo das estatísticas
    combined_results = df.groupby(df['city']).agg({'temp': ['min', 'max', 'mean']})

    # Exibição dos resultados
    return display(combined_results)
   
if __name__ == "__main__":
    filename = "data/tempments1.txt"
    create_vaex(filename)

```


<table>
<thead>
<tr><th>#                                 </th><th>station         </th><th>measure_min  </th><th>measure_max  </th><th>measure_mean      </th></tr>
</thead>
<tbody>
<tr><td><i style='opacity: 0.6'>0</i>     </td><td>South Dana      </td><td>-45.4        </td><td>96.7         </td><td>34.13404255319149 </td></tr>
<tr><td><i style='opacity: 0.6'>1</i>     </td><td>Benjaminborough </td><td>-47.8        </td><td>98.0         </td><td>27.29387755102041 </td></tr>
<tr><td><i style='opacity: 0.6'>2</i>     </td><td>New Ashley      </td><td>-47.9        </td><td>99.8         </td><td>39.13777777777778 </td></tr>
<tr><td><i style='opacity: 0.6'>3</i>     </td><td>South Angela    </td><td>-48.5        </td><td>99.9         </td><td>45.92227488151659 </td></tr>
<tr><td><i style='opacity: 0.6'>4</i>     </td><td>West Pamela     </td><td>-44.1        </td><td>95.4         </td><td>38.808045977011496</td></tr>
<tr><td>...                               </td><td>...             </td><td>...          </td><td>...          </td><td>...               </td></tr>
<tr><td><i style='opacity: 0.6'>91,357</i></td><td>New Rickyfort   </td><td>95.0         </td><td>95.0         </td><td>95.0              </td></tr>
<tr><td><i style='opacity: 0.6'>91,358</i></td><td>South Ruthfort  </td><td>41.0         </td><td>41.0         </td><td>41.0              </td></tr>
<tr><td><i style='opacity: 0.6'>91,359</i></td><td>Lake Biancafort </td><td>86.4         </td><td>86.4         </td><td>86.4              </td></tr>
<tr><td><i style='opacity: 0.6'>91,360</i></td><td>Port Selenamouth</td><td>-46.7        </td><td>-46.7        </td><td>-46.7             </td></tr>
<tr><td><i style='opacity: 0.6'>91,361</i></td><td>North Haroldland</td><td>93.4         </td><td>93.4         </td><td>93.4              </td></tr>
</tbody>
</table>


    create_vaex Tempo de processamento:0.943 segundos



```python
df = vaex.from_csv('data/measurements.txt', names=['city', 'temp'], sep=';',convert=True,chunk_size=10_000_000 , progress=True)
```

    Converting csv to chunk files
    Saved chunk #0 to data/measurements.txt_chunk_0.hdf5
    Saved chunk #1 to data/measurements.txt_chunk_1.hdf5
    Saved chunk #2 to data/measurements.txt_chunk_2.hdf5
    Saved chunk #3 to data/measurements.txt_chunk_3.hdf5
    Saved chunk #4 to data/measurements.txt_chunk_4.hdf5
    Saved chunk #5 to data/measurements.txt_chunk_5.hdf5
    Saved chunk #6 to data/measurements.txt_chunk_6.hdf5
    Saved chunk #7 to data/measurements.txt_chunk_7.hdf5
    Saved chunk #8 to data/measurements.txt_chunk_8.hdf5
    Saved chunk #9 to data/measurements.txt_chunk_9.hdf5
    Saved chunk #10 to data/measurements.txt_chunk_10.hdf5
    Saved chunk #11 to data/measurements.txt_chunk_11.hdf5
    Saved chunk #12 to data/measurements.txt_chunk_12.hdf5
    Saved chunk #13 to data/measurements.txt_chunk_13.hdf5
    Saved chunk #14 to data/measurements.txt_chunk_14.hdf5
    Saved chunk #15 to data/measurements.txt_chunk_15.hdf5
    Saved chunk #16 to data/measurements.txt_chunk_16.hdf5
    Saved chunk #17 to data/measurements.txt_chunk_17.hdf5
    Saved chunk #18 to data/measurements.txt_chunk_18.hdf5
    Saved chunk #19 to data/measurements.txt_chunk_19.hdf5
    Saved chunk #20 to data/measurements.txt_chunk_20.hdf5
    Saved chunk #21 to data/measurements.txt_chunk_21.hdf5
    Saved chunk #22 to data/measurements.txt_chunk_22.hdf5
    Saved chunk #23 to data/measurements.txt_chunk_23.hdf5
    Saved chunk #24 to data/measurements.txt_chunk_24.hdf5
    Saved chunk #25 to data/measurements.txt_chunk_25.hdf5
    Saved chunk #26 to data/measurements.txt_chunk_26.hdf5
    Saved chunk #27 to data/measurements.txt_chunk_27.hdf5
    Saved chunk #28 to data/measurements.txt_chunk_28.hdf5
    Saved chunk #29 to data/measurements.txt_chunk_29.hdf5
    Saved chunk #30 to data/measurements.txt_chunk_30.hdf5
    Saved chunk #31 to data/measurements.txt_chunk_31.hdf5
    Saved chunk #32 to data/measurements.txt_chunk_32.hdf5
    Saved chunk #33 to data/measurements.txt_chunk_33.hdf5
    Saved chunk #34 to data/measurements.txt_chunk_34.hdf5
    Saved chunk #35 to data/measurements.txt_chunk_35.hdf5
    Saved chunk #36 to data/measurements.txt_chunk_36.hdf5
    Saved chunk #37 to data/measurements.txt_chunk_37.hdf5
    Saved chunk #38 to data/measurements.txt_chunk_38.hdf5
    Saved chunk #39 to data/measurements.txt_chunk_39.hdf5
    Saved chunk #40 to data/measurements.txt_chunk_40.hdf5
    Saved chunk #41 to data/measurements.txt_chunk_41.hdf5
    Saved chunk #42 to data/measurements.txt_chunk_42.hdf5
    Saved chunk #43 to data/measurements.txt_chunk_43.hdf5
    Saved chunk #44 to data/measurements.txt_chunk_44.hdf5
    Saved chunk #45 to data/measurements.txt_chunk_45.hdf5
    Saved chunk #46 to data/measurements.txt_chunk_46.hdf5
    Saved chunk #47 to data/measurements.txt_chunk_47.hdf5
    Saved chunk #48 to data/measurements.txt_chunk_48.hdf5
    Saved chunk #49 to data/measurements.txt_chunk_49.hdf5
    Saved chunk #50 to data/measurements.txt_chunk_50.hdf5
    Saved chunk #51 to data/measurements.txt_chunk_51.hdf5
    Saved chunk #52 to data/measurements.txt_chunk_52.hdf5
    Saved chunk #53 to data/measurements.txt_chunk_53.hdf5
    Saved chunk #54 to data/measurements.txt_chunk_54.hdf5
    Saved chunk #55 to data/measurements.txt_chunk_55.hdf5
    Saved chunk #56 to data/measurements.txt_chunk_56.hdf5
    Saved chunk #57 to data/measurements.txt_chunk_57.hdf5
    Saved chunk #58 to data/measurements.txt_chunk_58.hdf5
    Saved chunk #59 to data/measurements.txt_chunk_59.hdf5
    Saved chunk #60 to data/measurements.txt_chunk_60.hdf5
    Saved chunk #61 to data/measurements.txt_chunk_61.hdf5
    Saved chunk #62 to data/measurements.txt_chunk_62.hdf5
    Saved chunk #63 to data/measurements.txt_chunk_63.hdf5
    Saved chunk #64 to data/measurements.txt_chunk_64.hdf5
    Saved chunk #65 to data/measurements.txt_chunk_65.hdf5
    Saved chunk #66 to data/measurements.txt_chunk_66.hdf5
    Saved chunk #67 to data/measurements.txt_chunk_67.hdf5
    Saved chunk #68 to data/measurements.txt_chunk_68.hdf5
    Saved chunk #69 to data/measurements.txt_chunk_69.hdf5
    Saved chunk #70 to data/measurements.txt_chunk_70.hdf5
    Saved chunk #71 to data/measurements.txt_chunk_71.hdf5
    Saved chunk #72 to data/measurements.txt_chunk_72.hdf5
    Saved chunk #73 to data/measurements.txt_chunk_73.hdf5
    Saved chunk #74 to data/measurements.txt_chunk_74.hdf5
    Saved chunk #75 to data/measurements.txt_chunk_75.hdf5
    Saved chunk #76 to data/measurements.txt_chunk_76.hdf5
    Saved chunk #77 to data/measurements.txt_chunk_77.hdf5
    Saved chunk #78 to data/measurements.txt_chunk_78.hdf5
    Saved chunk #79 to data/measurements.txt_chunk_79.hdf5
    Saved chunk #80 to data/measurements.txt_chunk_80.hdf5
    Saved chunk #81 to data/measurements.txt_chunk_81.hdf5
    Saved chunk #82 to data/measurements.txt_chunk_82.hdf5
    Saved chunk #83 to data/measurements.txt_chunk_83.hdf5
    Saved chunk #84 to data/measurements.txt_chunk_84.hdf5
    Saved chunk #85 to data/measurements.txt_chunk_85.hdf5
    Saved chunk #86 to data/measurements.txt_chunk_86.hdf5
    Saved chunk #87 to data/measurements.txt_chunk_87.hdf5
    Saved chunk #88 to data/measurements.txt_chunk_88.hdf5
    Saved chunk #89 to data/measurements.txt_chunk_89.hdf5
    Saved chunk #90 to data/measurements.txt_chunk_90.hdf5
    Saved chunk #91 to data/measurements.txt_chunk_91.hdf5
    Saved chunk #92 to data/measurements.txt_chunk_92.hdf5
    Saved chunk #93 to data/measurements.txt_chunk_93.hdf5
    Saved chunk #94 to data/measurements.txt_chunk_94.hdf5
    Saved chunk #95 to data/measurements.txt_chunk_95.hdf5
    Saved chunk #96 to data/measurements.txt_chunk_96.hdf5
    Saved chunk #97 to data/measurements.txt_chunk_97.hdf5
    Saved chunk #98 to data/measurements.txt_chunk_98.hdf5
    Saved chunk #99 to data/measurements.txt_chunk_99.hdf5
    Converting 100 chunks into single file data/measurements.txt.hdf5
    export(hdf5) [########################################] 100.00% elapsed time  :   198.26s =  3.3m =  0.1h h                  
     


```python
# Vaex => script para caluclar min, max e mean em um bilhão de linhas.
import vaex
@timer_to_csv
def vaex_df(filename):
    # Leitura do arquivo CSV utilizando Vaex
    df = vaex.open(filename)

    # Cálculo das estatísticas
    combined_results = df.groupby(df['city']).agg({'temp': ['min', 'max', 'mean']})
    
    # Ordenar por 'city'
    combined_results = combined_results.sort(by='city')

    # Exibição dos resultados
    return display(combined_results)
   
if __name__ == "__main__":
    filename = "data/measurements.txt"
    vaex_df(filename)

```


<table>
<thead>
<tr><th>#                                </th><th>station       </th><th>measure_min  </th><th>measure_max  </th><th>measure_mean         </th></tr>
</thead>
<tbody>
<tr><td><i style='opacity: 0.6'>0</i>    </td><td>Aabenraa      </td><td>-99.9        </td><td>99.9         </td><td>-0.062294754104918   </td></tr>
<tr><td><i style='opacity: 0.6'>1</i>    </td><td>Aalten        </td><td>-99.9        </td><td>99.9         </td><td>-0.16175191675246645 </td></tr>
<tr><td><i style='opacity: 0.6'>2</i>    </td><td>Abadiânia     </td><td>-99.9        </td><td>99.9         </td><td>-0.0527721562105517  </td></tr>
<tr><td><i style='opacity: 0.6'>3</i>    </td><td>Abalessa      </td><td>-99.9        </td><td>99.9         </td><td>0.21108942210476792  </td></tr>
<tr><td><i style='opacity: 0.6'>4</i>    </td><td>Abangaritos   </td><td>-99.9        </td><td>99.9         </td><td>0.06377211442610778  </td></tr>
<tr><td>...                              </td><td>...           </td><td>...          </td><td>...          </td><td>...                  </td></tr>
<tr><td><i style='opacity: 0.6'>8,831</i></td><td>’Aïn Abessa   </td><td>-99.9        </td><td>99.9         </td><td>-0.013338384996559474</td></tr>
<tr><td><i style='opacity: 0.6'>8,832</i></td><td>’Aïn Azel     </td><td>-99.9        </td><td>99.9         </td><td>-0.040762228668600346</td></tr>
<tr><td><i style='opacity: 0.6'>8,833</i></td><td>’Aïn Roua     </td><td>-99.9        </td><td>99.9         </td><td>-0.02689839143166584 </td></tr>
<tr><td><i style='opacity: 0.6'>8,834</i></td><td>’s-Gravenzande</td><td>-99.9        </td><td>99.9         </td><td>-0.0809733627077911  </td></tr>
<tr><td><i style='opacity: 0.6'>8,835</i></td><td>’s-Heerenberg </td><td>-99.9        </td><td>99.9         </td><td>0.16826510134457162  </td></tr>
</tbody>
</table>


    create_vaex Tempo de processamento:47.454 segundos



```python

```

## cuDF com pandas via GPU


```python
#verificando a versão do python para esse estudo.
!python --version
```

    Python 3.11.3



```python
# CuDF_Pandas=> script para caluclar min, max e mean em um bilhão de linhas na GPU rtx 3060ti.
# Necessário possuir uma GPU compativel e instalar o pacote RAPIDS da Nvidia.
%load_ext cudf.pandas
import pandas as pd
@timer_to_csv
def cudf_pandas_df():
    # Defina o caminho para o seu arquivo CSV
    file_path = "data/measurements.txt"
    
    # Tamanho do chunk (você pode ajustar conforme necessário)
    chunk_size = 100_000_000  # por exemplo, 1 milhão de linhas por chunk
    
    # Inicialize um DataFrame vazio para armazenar os resultados
    results_df = pd.DataFrame()
    
    # Loop através do arquivo em chunks e calcule as estatísticas
    for chunk in pd.read_csv(file_path,sep=';', header=None, names=['city', 'temp'], chunksize=chunk_size):
        # Calcular as estatísticas por grupo
        grouped_stats = chunk.groupby('city').agg({'temp': ['max','min','mean']}).reset_index()
        # Concatenar os resultados ao DataFrame principal
        results_df = pd.concat([results_df, grouped_stats], ignore_index=True)
    # Removendo o level city    
    results_df = results_df.droplevel(0,axis=1)
    # Renomeando o level 0 para city
    results_df.rename(columns={'':'city'}, inplace=True)
    # Fazendo o groupby geral.
    results_df.groupby('city').agg({ 'max':'max', 'min':'min', 'mean':'mean'}).round(2).sort_values('city')    
    # Resultados finais
    return display(results_df)

if __name__== "__main__":
    print(cudf_pandas_df())
    
```

    Tempo decorrido: 11 minutos 58 segundos


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
      <th>city</th>
      <th>max</th>
      <th>min</th>
      <th>mean</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A Coruña</td>
      <td>56.7</td>
      <td>-89.2</td>
      <td>-16.465922</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Aachen</td>
      <td>56.7</td>
      <td>-89.2</td>
      <td>-16.294465</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Aalst</td>
      <td>56.7</td>
      <td>-89.2</td>
      <td>-16.347356</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Aarau</td>
      <td>56.7</td>
      <td>-89.2</td>
      <td>-15.935726</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Abaré</td>
      <td>56.6</td>
      <td>-89.2</td>
      <td>-16.798837</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>88535</th>
      <td>‘Alīābād-e Katūl</td>
      <td>56.7</td>
      <td>-89.2</td>
      <td>-15.928671</td>
    </tr>
    <tr>
      <th>88536</th>
      <td>‘Amrān</td>
      <td>56.7</td>
      <td>-89.2</td>
      <td>-15.202512</td>
    </tr>
    <tr>
      <th>88537</th>
      <td>‘Anadān</td>
      <td>56.7</td>
      <td>-89.2</td>
      <td>-15.528164</td>
    </tr>
    <tr>
      <th>88538</th>
      <td>’Ayn Bni Mathar</td>
      <td>56.7</td>
      <td>-89.2</td>
      <td>-16.978998</td>
    </tr>
    <tr>
      <th>88539</th>
      <td>’Tlat Bni Oukil</td>
      <td>56.7</td>
      <td>-89.2</td>
      <td>-16.082428</td>
    </tr>
  </tbody>
</table>
<p>88540 rows × 4 columns</p>
</div>


    Tempo total de execução: 11 minutos 58 segundos
    None



```python
# Verificando se o ambiente virtual foi setado corretamente.
import site
site.getsitepackages()
```




    ['/home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages']



* **Para a leitura para 10 milhões de linha foi extremamente rápido, porém para 1 bilhão a memória não suportou.**


```python
# Script usando cudf == pandas mas rápido pq usa a GPU, porém a mem não suport procesar 1bilhão.
import cudf
@timer
def create_cudf(filename):
    
    # Carregar o arquivo CSV e criar os cabeçalhos 'city' e 'temp'
    df = cudf.read_csv(filename, header=None, sep=';', names=['city', 'temp'])
    
    # Agrupar por 'city' e calcular o 'min', 'max' e 'mean' da coluna 'temp'
    grouped_df = df.groupby('city').agg({'temp': ['min', 'max', 'mean']})
    
    # Ordenar o DataFrame pelo índice (city)
    result = grouped_df.sort_index()     
    
    # retorna o resultado
    return print(result)

if __name__ == "__main__":
    filename = "data/tempments1.txt"
    create_cudf(filename)

```

                 measure                 
                     min   max       mean
    station                              
    Aaronberg      -48.6  99.4  37.065909
    Aaronborough   -46.4  98.4  38.725000
    Aaronburgh     -45.4  92.0  33.942000
    Aaronbury      -47.3  98.7  53.363636
    Aaronchester   -49.9  98.8  43.383333
    ...              ...   ...        ...
    Zunigastad     -13.7  57.8  17.450000
    Zunigaton      -44.7  86.1  29.414286
    Zunigatown      45.2  99.4  68.266667
    Zunigaview      -4.1  86.5  60.760000
    Zunigaville     -2.1  57.1  38.450000
    
    [91362 rows x 3 columns]
    create_cudf Tempo de processamento:0.163 segundos



```python
%%time
import dask_cudf as dc

# Carregar o arquivo csv em um dataframe dask_cudf
df = dc.read_csv('data/measurements.txt',sep=';', header=None, names=['city', 'temp'], dtype=['str', 'float32'], blocksize='1024 Mib')

# Agrupar pela coluna 'city' e calcular min, max e mean da coluna 'temp'
grouped_df = df.groupby('city').agg({'temp': ['min', 'max', 'mean']}).compute()

# Ordenar pelo 'city'
sorted_df = grouped_df.sort_index()

# Imprimir as 5 primeiras e últimas linhas
display(sorted_df)
#print(sorted_df.tail(5))

```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    File <timed exec>:1


    File ~/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages/dask_cudf/__init__.py:7
          3 from dask.dataframe import from_delayed
          5 import cudf
    ----> 7 from . import backends
          8 from ._version import __git_commit__, __version__
          9 from .core import DataFrame, Series, concat, from_cudf, from_dask_dataframe


    File ~/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages/dask_cudf/backends.py:47
         44 from cudf.api.types import is_string_dtype
         45 from cudf.utils.nvtx_annotation import _dask_cudf_nvtx_annotate
    ---> 47 from .core import DataFrame, Index, Series
         49 get_parallel_type.register(cudf.DataFrame, lambda _: DataFrame)
         50 get_parallel_type.register(cudf.Series, lambda _: Series)


    File ~/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages/dask_cudf/core.py:714
        693     name = name or ("from_cudf-" + tokenize(data, npartitions or chunksize))
        694     return dd.from_pandas(
        695         data,
        696         npartitions=npartitions,
       (...)
        699         name=name,
        700     )
        703 from_cudf.__doc__ = (
        704     textwrap.dedent(
        705         """
        706         Create a :class:`.DataFrame` from a :class:`cudf.DataFrame`.
        707 
        708         This function is a thin wrapper around
        709         :func:`dask.dataframe.from_pandas`, accepting the same
        710         arguments (described below) excepting that it operates on cuDF
        711         rather than pandas objects.\n
        712         """
        713     )
    --> 714     + textwrap.dedent(dd.from_pandas.__doc__)
        715 )
        718 @_dask_cudf_nvtx_annotate
        719 def from_dask_dataframe(df):
        720     """
        721     Convert a Dask :class:`dask.dataframe.DataFrame` to a Dask-cuDF
        722     one.
       (...)
        731     dask_cudf.DataFrame : A new Dask collection backed by cuDF objects
        732     """


    File ~/.pyenv/versions/3.11.3/lib/python3.11/textwrap.py:435, in dedent(text)
        432 # Look for the longest leading string of spaces and tabs common to
        433 # all lines.
        434 margin = None
    --> 435 text = _whitespace_only_re.sub('', text)
        436 indents = _leading_whitespace_re.findall(text)
        437 for indent in indents:


    TypeError: expected string or bytes-like object, got 'NoneType'


## Dask_cudf com GPU


```python
!poetry add pyarrow==14.0.1 dask==2024.1.1 dask-expr==0.4.0
```


```python
# dask_cudf com blocksize 1gb => script para caluclar min, max e mean em um bilhão de linhas usando a gpu rtx 3060ti.
# Definindo o cluster para usar gpu
from dask.distributed import Client
from dask_cuda import LocalCUDACluster
# create a local CUDA cluster
cluster = LocalCUDACluster()
client = Client(cluster)
import dask_cudf as dc
@timer_to_csv
def dask_cudf_1024():
    # Carregar o arquivo csv em um dataframe dask_cudf
    df = dc.read_csv('data/measurements.txt',sep=';',
                     header=None, names=['city', 'temp'], 
                     dtype=['str', 'float32'], 
                     blocksize='1024 Mib')
    
    # Agrupar pela coluna 'city' e calcular min, max e mean da coluna 'temp'
    return display(df.groupby('city').
                   agg({'temp': ['max','min','mean']}).
                   compute().sort_index().round(2))     
#if __name__=="_main__":
dask_cudf_1024()
```

    /home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages/distributed/node.py:182: UserWarning: Port 8787 is already in use.
    Perhaps you already have a cluster running?
    Hosting the HTTP server on port 43087 instead
      warnings.warn(
    /home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages/dask_cuda/utils.py:170: UserWarning: Cannot get CPU affinity for device with index 0, setting default affinity
      warnings.warn(


    Tempo decorrido: 2 minutos 44 segundos


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">temp</th>
    </tr>
    <tr>
      <th></th>
      <th>max</th>
      <th>min</th>
      <th>mean</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A Coruña</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.28</td>
    </tr>
    <tr>
      <th>Aachen</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.26</td>
    </tr>
    <tr>
      <th>Aalst</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.49</td>
    </tr>
    <tr>
      <th>Aarau</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.13</td>
    </tr>
    <tr>
      <th>Abaré</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.40</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>‘Alīābād-e Katūl</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.23</td>
    </tr>
    <tr>
      <th>‘Amrān</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.08</td>
    </tr>
    <tr>
      <th>‘Anadān</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.29</td>
    </tr>
    <tr>
      <th>’Ayn Bni Mathar</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.09</td>
    </tr>
    <tr>
      <th>’Tlat Bni Oukil</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.26</td>
    </tr>
  </tbody>
</table>
<p>8854 rows × 3 columns</p>
</div>


    Tempo total de execução: 2 minutos 44 segundos



```python
# dask_cudf com blocksize 1024 => script para calcular min, max e mean em um bilhão de linhas usando a gpu rtx 3060ti.
from dask.distributed import Client
from dask_cuda import LocalCUDACluster
import dask_cudf as dc

@timer_to_csv
def dask_cudf_1024():
    # Definindo o cluster para usar gpu
    with LocalCUDACluster() as cluster, Client(cluster) as client:
        # Carregar o arquivo csv em um dataframe dask_cudf
        df = dc.read_csv('data/measurements.txt',
                         sep=';', header=None,
                         names=['city', 'temp'], 
                         dtype={'city': 'str', 'temp': 'float32'},
                         blocksize='1024 MiB')
        
        # Agrupar pela coluna 'city' e calcular min, max e mean da coluna 'temp'
        result = df.groupby('city').agg({'temp': ['max','min','mean']}).compute().sort_index()
        display(result)

dask_cudf_1024()
```

    Tempo decorrido: 0.005 segundos

    /home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages/distributed/node.py:182: UserWarning: Port 8787 is already in use.
    Perhaps you already have a cluster running?
    Hosting the HTTP server on port 35393 instead
      warnings.warn(
    /home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages/dask_cuda/utils.py:170: UserWarning: Cannot get CPU affinity for device with index 0, setting default affinity
      warnings.warn(


    Tempo decorrido: 3 minutos 39 segundos


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">temp</th>
    </tr>
    <tr>
      <th></th>
      <th>max</th>
      <th>min</th>
      <th>mean</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A Coruña</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.284528</td>
    </tr>
    <tr>
      <th>Aachen</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.263413</td>
    </tr>
    <tr>
      <th>Aalst</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.487185</td>
    </tr>
    <tr>
      <th>Aarau</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.132313</td>
    </tr>
    <tr>
      <th>Abaré</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.397280</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>‘Alīābād-e Katūl</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.228978</td>
    </tr>
    <tr>
      <th>‘Amrān</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.081336</td>
    </tr>
    <tr>
      <th>‘Anadān</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.288187</td>
    </tr>
    <tr>
      <th>’Ayn Bni Mathar</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.094877</td>
    </tr>
    <tr>
      <th>’Tlat Bni Oukil</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.255552</td>
    </tr>
  </tbody>
</table>
<p>8854 rows × 3 columns</p>
</div>


    Tempo total de execução: 3 minutos 42 segundos



```python
import psutil

# Obtém o processo JupyterLab
process = psutil.Process()

# Obtém a quantidade total de memória alocada para o processo em bytes
memoria_total = process.memory_info().rss

# Converta bytes para megabytes para uma leitura mais compreensível
memoria_total_mb = memoria_total / (1024 * 1024)

print(f"A memória total alocada para o JupyterLab é de aproximadamente {memoria_total_mb:.2f} MB")

```


```python
# muito util pois imprime os parametros do método.
??cudf.read_csv
```


```python
# dask_cudf com blocksize 256mb => script para caluclar min, max e mean em um bilhão de linhas usando a gpu rtx 3060ti.
# Definindo o cluster para usar gpu
from dask.distributed import Client
from dask_cuda import LocalCUDACluster
# create a local CUDA cluster
cluster = LocalCUDACluster()
client = Client(cluster)
import dask_cudf as dc
@timer_to_csv
def dask_cudf_256():
    # Carregar o arquivo csv em um dataframe dask_cudf
    df = dc.read_csv('data/measurements.txt',
                     sep=';', header=None,
                     names=['city', 'temp'], 
                     dtype=['str', 'float32'],
                     blocksize='256 Mib')
    
    # Agrupar pela coluna 'city' e calcular min, max e mean da coluna 'temp'
    return df.groupby('city').agg({'temp': ['max','min','mean']}).compute().sort_index()

dask_cudf_256()
```

    /home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages/dask_cuda/utils.py:170: UserWarning: Cannot get CPU affinity for device with index 0, setting default affinity
      warnings.warn(


    Tempo total de execução: 5 minutos 17 segundos





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">temp</th>
    </tr>
    <tr>
      <th></th>
      <th>max</th>
      <th>min</th>
      <th>mean</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A Coruña</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.284528</td>
    </tr>
    <tr>
      <th>Aachen</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.263415</td>
    </tr>
    <tr>
      <th>Aalst</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.487185</td>
    </tr>
    <tr>
      <th>Aarau</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.132312</td>
    </tr>
    <tr>
      <th>Abaré</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.397278</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>‘Alīābād-e Katūl</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.228977</td>
    </tr>
    <tr>
      <th>‘Amrān</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.081336</td>
    </tr>
    <tr>
      <th>‘Anadān</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.288187</td>
    </tr>
    <tr>
      <th>’Ayn Bni Mathar</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.094877</td>
    </tr>
    <tr>
      <th>’Tlat Bni Oukil</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.255552</td>
    </tr>
  </tbody>
</table>
<p>8854 rows × 3 columns</p>
</div>




```python
# dask_cudf com blocksize 256mb => script para calcular min, max e mean em um bilhão de linhas usando a gpu rtx 3060ti.
from dask.distributed import Client
from dask_cuda import LocalCUDACluster
import dask_cudf as dc

@timer_to_csv
def dask_cudf_256():
    # Definindo o cluster para usar gpu
    with LocalCUDACluster() as cluster, Client(cluster) as client:
        # Carregar o arquivo csv em um dataframe dask_cudf
        df = dc.read_csv('data/measurements.txt',
                         sep=';', header=None,
                         names=['city', 'temp'], 
                         dtype={'city': 'str', 'temp': 'float32'},
                         blocksize='256 MiB')
        
        # Agrupar pela coluna 'city' e calcular min, max e mean da coluna 'temp'
        result = df.groupby('city').agg({'temp': ['max','min','mean']}).compute().sort_index()
        display(result)

dask_cudf_256()
```

    Tempo decorrido: 0.005 segundos

    /home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages/dask_cuda/utils.py:170: UserWarning: Cannot get CPU affinity for device with index 0, setting default affinity
      warnings.warn(


    Tempo decorrido: 1 minutos 52 segundos


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">temp</th>
    </tr>
    <tr>
      <th></th>
      <th>max</th>
      <th>min</th>
      <th>mean</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A Coruña</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.284528</td>
    </tr>
    <tr>
      <th>Aachen</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.263415</td>
    </tr>
    <tr>
      <th>Aalst</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.487185</td>
    </tr>
    <tr>
      <th>Aarau</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.132312</td>
    </tr>
    <tr>
      <th>Abaré</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.397278</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>‘Alīābād-e Katūl</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.228977</td>
    </tr>
    <tr>
      <th>‘Amrān</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.081336</td>
    </tr>
    <tr>
      <th>‘Anadān</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.288187</td>
    </tr>
    <tr>
      <th>’Ayn Bni Mathar</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.094878</td>
    </tr>
    <tr>
      <th>’Tlat Bni Oukil</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.255551</td>
    </tr>
  </tbody>
</table>
<p>8854 rows × 3 columns</p>
</div>


    Tempo decorrido: 1 minutos 53 segundos

    2024-03-21 01:38:28,923 - distributed.worker - ERROR - Failed to communicate with scheduler during heartbeat.
    Traceback (most recent call last):
      File "/home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages/distributed/comm/tcp.py", line 225, in read
        frames_nosplit_nbytes_bin = await stream.read_bytes(fmt_size)
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    tornado.iostream.StreamClosedError: Stream is closed
    
    The above exception was the direct cause of the following exception:
    
    Traceback (most recent call last):
      File "/home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages/distributed/worker.py", line 1252, in heartbeat
        response = await retry_operation(
                   ^^^^^^^^^^^^^^^^^^^^^^
      File "/home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages/distributed/utils_comm.py", line 455, in retry_operation
        return await retry(
               ^^^^^^^^^^^^
      File "/home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages/distributed/utils_comm.py", line 434, in retry
        return await coro()
               ^^^^^^^^^^^^
      File "/home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages/distributed/core.py", line 1395, in send_recv_from_rpc
        return await send_recv(comm=comm, op=key, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages/distributed/core.py", line 1154, in send_recv
        response = await comm.read(deserializers=deserializers)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages/distributed/comm/tcp.py", line 236, in read
        convert_stream_closed_error(self, e)
      File "/home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages/distributed/comm/tcp.py", line 142, in convert_stream_closed_error
        raise CommClosedError(f"in {obj}: {exc}") from exc
    distributed.comm.core.CommClosedError: in <TCP (closed) ConnectionPool.heartbeat_worker local=tcp://127.0.0.1:50200 remote=tcp://127.0.0.1:35601>: Stream is closed


    Tempo decorrido: 1 minutos 55 segundos

    2024-03-21 01:38:32,062 - distributed.nanny - WARNING - Worker process still alive after 3.199914703369141 seconds, killing


    Tempo total de execução: 1 minutos 56 segundos



```python
df.columns = df.columns.map('_'.join)
```


```python
df.round({'temp_max': 3, 'temp_min': 3, 'temp_mean': 3})
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
      <th>temp_max</th>
      <th>temp_min</th>
      <th>temp_mean</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A Coruña</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.285</td>
    </tr>
    <tr>
      <th>Aachen</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.263</td>
    </tr>
    <tr>
      <th>Aalst</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.487</td>
    </tr>
    <tr>
      <th>Aarau</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.132</td>
    </tr>
    <tr>
      <th>Abaré</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.397</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>‘Alīābād-e Katūl</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.229</td>
    </tr>
    <tr>
      <th>‘Amrān</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.081</td>
    </tr>
    <tr>
      <th>‘Anadān</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.288</td>
    </tr>
    <tr>
      <th>’Ayn Bni Mathar</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.095</td>
    </tr>
    <tr>
      <th>’Tlat Bni Oukil</th>
      <td>56.700001</td>
      <td>-89.199997</td>
      <td>-16.256</td>
    </tr>
  </tbody>
</table>
<p>8854 rows × 3 columns</p>
</div>



* **Alterando para 256 MiB a performance melhorou, mas ainda assim bem longe de superar o DuckDB.**
* **Conforme o benchmarch da documentação ele tem capacidade de superar o sgdb. Talvez alguma configuração pois ainda não li toda a documentação.**

## testes

* não consegue ler 1bilhão.


```python
%%time
import pyarrow.csv as csv

# Definir opções de leitura
read_options = csv.ReadOptions(use_threads=True, column_names=['cidade','temperatura'])
parse_options = csv.ParseOptions(delimiter=';')

# Carregar o arquivo de medidas
table = csv.read_csv('data/tempments1.txt', read_options=read_options, parse_options=parse_options)

# Converter para um DataFrame Arrow
df = table.to_pandas()

# Agrupar por cidade e calcular mínimo, máximo e média das temperaturas
resultados = df.groupby('cidade')['temperatura'].agg(['min', 'max', 'mean'])

# Ordenar os resultados pela cidade
resultados = resultados.sort_index()

# Exibir os resultados
print(resultados)
```

                   min   max       mean
    cidade                             
    Aaronberg    -48.6  99.4  37.065909
    Aaronborough -46.4  98.4  38.725000
    Aaronburgh   -45.4  92.0  33.942000
    Aaronbury    -47.3  98.7  53.363636
    Aaronchester -49.9  98.8  43.383333
    ...            ...   ...        ...
    Zunigastad   -13.7  57.8  17.450000
    Zunigaton    -44.7  86.1  29.414286
    Zunigatown    45.2  99.4  68.266667
    Zunigaview    -4.1  86.5  60.760000
    Zunigaville   -2.1  57.1  38.450000
    
    [91362 rows x 3 columns]
    CPU times: user 1.07 s, sys: 374 ms, total: 1.44 s
    Wall time: 1.46 s



```python

```


```python

```

## Setup and install RAPIDs


```python
!nvidia-smi
```

    Tue Mar 12 18:27:47 2024       
    +-----------------------------------------------------------------------------------------+
    | NVIDIA-SMI 550.40.06              Driver Version: 551.23         CUDA Version: 12.4     |
    |-----------------------------------------+------------------------+----------------------+
    | GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
    | Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
    |                                         |                        |               MIG M. |
    |=========================================+========================+======================|
    |   0  NVIDIA GeForce RTX 3060 Ti     On  |   00000000:03:00.0  On |                  N/A |
    | 34%   42C    P8             16W /  200W |     487MiB /   8192MiB |      0%      Default |
    |                                         |                        |                  N/A |
    +-----------------------------------------+------------------------+----------------------+
                                                                                             
    +-----------------------------------------------------------------------------------------+
    | Processes:                                                                              |
    |  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
    |        ID   ID                                                               Usage      |
    |=========================================================================================|
    |    0   N/A  N/A        37      G   /Xwayland                                   N/A      |
    +-----------------------------------------------------------------------------------------+


* **Veja que interessante o %%load_ext cudf.pandas converte a maioria dos comandos do pandas para processamento em gpu.** 


```python
# Carrega o cudf para pandas
%load_ext cudf.pandas
import pandas as pd
```


```python
# verificando se o cudf foi setado no pandas
pd
```




    <module 'pandas' (ModuleAccelerator(fast=cudf, slow=pandas))>




```python
# verificando se o método read do pandas está em modo fast.
type(pd.read_csv)
```




    cudf.pandas.fast_slow_proxy._FunctionProxy




```python
# Carrega o cudf para pandas
%load_ext cudf.pandas
import pandas as pd
@timer
def dc_read():
    # Carregar o arquivo csv em um dataframe dask_cudf
    df = pd.read_csv('data/tempments1.txt',
                     sep=';', header=None,
                     names=['city', 'temp'], 
                     dtype=['str', 'float32'])
    
    # Agrupar pela coluna 'city' e calcular min, max e mean da coluna 'temp'
    grouped_df = df.groupby('city').agg({'temp': ['min', 'max', 'mean']})
    
    # Ordenar pelo 'city'
    sorted_df = grouped_df.sort_index()    
    
    return sorted_df
dc_read()

```

    The cudf.pandas extension is already loaded. To reload it, use:
      %reload_ext cudf.pandas
    dc_read Tempo de processamento:0.166 segundos





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">measure</th>
    </tr>
    <tr>
      <th></th>
      <th>min</th>
      <th>max</th>
      <th>mean</th>
    </tr>
    <tr>
      <th>station</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Aaronberg</th>
      <td>-48.599998</td>
      <td>99.400002</td>
      <td>37.065918</td>
    </tr>
    <tr>
      <th>Aaronborough</th>
      <td>-46.400002</td>
      <td>98.400002</td>
      <td>38.724998</td>
    </tr>
    <tr>
      <th>Aaronburgh</th>
      <td>-45.400002</td>
      <td>92.000000</td>
      <td>33.942002</td>
    </tr>
    <tr>
      <th>Aaronbury</th>
      <td>-47.299999</td>
      <td>98.699997</td>
      <td>53.363631</td>
    </tr>
    <tr>
      <th>Aaronchester</th>
      <td>-49.900002</td>
      <td>98.800003</td>
      <td>43.383333</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Zunigastad</th>
      <td>-13.700000</td>
      <td>57.799999</td>
      <td>17.449999</td>
    </tr>
    <tr>
      <th>Zunigaton</th>
      <td>-44.700001</td>
      <td>86.099998</td>
      <td>29.414285</td>
    </tr>
    <tr>
      <th>Zunigatown</th>
      <td>45.200001</td>
      <td>99.400002</td>
      <td>68.266668</td>
    </tr>
    <tr>
      <th>Zunigaview</th>
      <td>-4.100000</td>
      <td>86.500000</td>
      <td>60.759998</td>
    </tr>
    <tr>
      <th>Zunigaville</th>
      <td>-2.100000</td>
      <td>57.099998</td>
      <td>38.450001</td>
    </tr>
  </tbody>
</table>
<p>91362 rows × 3 columns</p>
</div>




```python
# reinicia o kernel
# @title
get_ipython().kernel.do_shutdown(restart=True)
```




    {'status': 'ok', 'restart': True}




```python
import cudf
```

Introduction to Dask¶
Dask is a library the allows for parallelized computing. Written in Python, it allows one to compose complex workflows using large data structures like those found in NumPy, Pandas, and cuDF. In the following examples and notebooks, we'll show how to use Dask with cuDF to accelerate common ETL tasks as well as build and train machine learning models like Linear Regression and XGBoost.

To learn more about Dask, check out the documentation here: http://docs.dask.org/en/latest/

Client/Workers
Dask operates by creating a cluster composed of a "client" and multiple "workers". The client is responsible for scheduling work; the workers are responsible for actually executing that work.

Typically, we set the number of workers to be equal to the number of computing resources we have available to us. For CPU based workflows, this might be the number of cores or threads on that particlular machine. For example, we might set n_workers = 8 if we have 8 CPU cores or threads on our machine that can each operate in parallel. This allows us to take advantage of all of our computing resources and enjoy the most benefits from parallelization.

On a system with one or more GPUs, we usually set the number of workers equal to the number of GPUs available to us. Dask is a first class citizen in the world of General Purpose GPU computing and the RAPIDS ecosystem makes it very easy to use Dask with cuDF and XGBoost.

Before we get started with Dask, we need to setup a Local Cluster of workers to execute our work and a Client to coordinate and schedule work for that cluster. As we see below, we can inititate a cluster and client using only few lines of code.


Introdução ao Dask¶ Dask é uma biblioteca que permite computação paralelizada. Escrito em Python, permite compor fluxos de trabalho complexos usando grandes estruturas de dados como as encontradas em NumPy, Pandas e cuDF. Nos exemplos e notebooks a seguir, mostraremos como usar Dask com cuDF para acelerar tarefas comuns de ETL, bem como construir e treinar modelos de aprendizado de máquina como regressão linear e XGBoost. Para saber mais sobre o Dask, confira a documentação aqui: http://docs.dask.org/en/latest/ Client/Workers O Dask opera criando um cluster composto por um "cliente" e vários "trabalhadores". O cliente é responsável pelo agendamento dos trabalhos; os trabalhadores são responsáveis ​​pela execução efetiva desse trabalho. Normalmente, definimos o número de trabalhadores como igual ao número de recursos computacionais que temos disponíveis. Para fluxos de trabalho baseados em CPU, esse pode ser o número de núcleos ou threads naquela máquina específica. Por exemplo, podemos definir n_workers = 8 se tivermos 8 núcleos de CPU ou threads em nossa máquina que podem operar em paralelo. Isso nos permite aproveitar todos os nossos recursos computacionais e aproveitar ao máximo os benefícios da paralelização. Em um sistema com uma ou mais GPUs, normalmente definimos o número de trabalhadores igual ao número de GPUs disponíveis para nós. Dask é um cidadão de primeira classe no mundo da computação GPU de uso geral e o ecossistema RAPIDS torna muito fácil usar o Dask com cuDF e XGBoost. Antes de começarmos com o Dask, precisamos configurar um cluster local de trabalhadores para executar nosso trabalho e um cliente para coordenar e agendar o trabalho para esse cluster. Como vemos abaixo, podemos iniciar um cluster e um cliente usando apenas algumas linhas de código.


```python
import dask; print('Dask Version:', dask.__version__)
from dask.distributed import Client, LocalCluster


# create a local cluster with 4 workers
n_workers = 4
cluster = LocalCluster(n_workers=n_workers)
client = Client(cluster)
```

    Dask Version: 2024.1.1


Let's inspect the client object to view our current Dask status. We should see the IP Address for our Scheduler as well as the the number of workers in our Cluster.

Vamos inspecionar o objeto cliente para visualizar nosso status atual do Dask. Devemos ver o endereço IP do nosso Agendador, bem como o número de trabalhadores no nosso Cluster.


```python
# show current Dask status
client
```




<div>
    <div style="width: 24px; height: 24px; background-color: #e1e1e1; border: 3px solid #9D9D9D; border-radius: 5px; position: absolute;"> </div>
    <div style="margin-left: 48px;">
        <h3 style="margin-bottom: 0px;">Client</h3>
        <p style="color: #9D9D9D; margin-bottom: 0px;">Client-93c82fc9-e021-11ee-b136-6174df56fd34</p>
        <table style="width: 100%; text-align: left;">

        <tr>

            <td style="text-align: left;"><strong>Connection method:</strong> Cluster object</td>
            <td style="text-align: left;"><strong>Cluster type:</strong> distributed.LocalCluster</td>

        </tr>


            <tr>
                <td style="text-align: left;">
                    <strong>Dashboard: </strong> <a href="http://127.0.0.1:8787/status" target="_blank">http://127.0.0.1:8787/status</a>
                </td>
                <td style="text-align: left;"></td>
            </tr>


        </table>




            <details>
            <summary style="margin-bottom: 20px;"><h3 style="display: inline;">Cluster Info</h3></summary>
            <div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-mod-trusted jp-OutputArea-output">
    <div style="width: 24px; height: 24px; background-color: #e1e1e1; border: 3px solid #9D9D9D; border-radius: 5px; position: absolute;">
    </div>
    <div style="margin-left: 48px;">
        <h3 style="margin-bottom: 0px; margin-top: 0px;">LocalCluster</h3>
        <p style="color: #9D9D9D; margin-bottom: 0px;">cdddd731</p>
        <table style="width: 100%; text-align: left;">
            <tr>
                <td style="text-align: left;">
                    <strong>Dashboard:</strong> <a href="http://127.0.0.1:8787/status" target="_blank">http://127.0.0.1:8787/status</a>
                </td>
                <td style="text-align: left;">
                    <strong>Workers:</strong> 4
                </td>
            </tr>
            <tr>
                <td style="text-align: left;">
                    <strong>Total threads:</strong> 24
                </td>
                <td style="text-align: left;">
                    <strong>Total memory:</strong> 7.68 GiB
                </td>
            </tr>

            <tr>
    <td style="text-align: left;"><strong>Status:</strong> running</td>
    <td style="text-align: left;"><strong>Using processes:</strong> True</td>
</tr>


        </table>

        <details>
            <summary style="margin-bottom: 20px;">
                <h3 style="display: inline;">Scheduler Info</h3>
            </summary>

            <div style="">
    <div>
        <div style="width: 24px; height: 24px; background-color: #FFF7E5; border: 3px solid #FF6132; border-radius: 5px; position: absolute;"> </div>
        <div style="margin-left: 48px;">
            <h3 style="margin-bottom: 0px;">Scheduler</h3>
            <p style="color: #9D9D9D; margin-bottom: 0px;">Scheduler-9d79611f-daad-4492-a2bf-cdc7f9c6a0e2</p>
            <table style="width: 100%; text-align: left;">
                <tr>
                    <td style="text-align: left;">
                        <strong>Comm:</strong> tcp://127.0.0.1:43807
                    </td>
                    <td style="text-align: left;">
                        <strong>Workers:</strong> 4
                    </td>
                </tr>
                <tr>
                    <td style="text-align: left;">
                        <strong>Dashboard:</strong> <a href="http://127.0.0.1:8787/status" target="_blank">http://127.0.0.1:8787/status</a>
                    </td>
                    <td style="text-align: left;">
                        <strong>Total threads:</strong> 24
                    </td>
                </tr>
                <tr>
                    <td style="text-align: left;">
                        <strong>Started:</strong> 1 minute ago
                    </td>
                    <td style="text-align: left;">
                        <strong>Total memory:</strong> 7.68 GiB
                    </td>
                </tr>
            </table>
        </div>
    </div>

    <details style="margin-left: 48px;">
        <summary style="margin-bottom: 20px;">
            <h3 style="display: inline;">Workers</h3>
        </summary>


        <div style="margin-bottom: 20px;">
            <div style="width: 24px; height: 24px; background-color: #DBF5FF; border: 3px solid #4CC9FF; border-radius: 5px; position: absolute;"> </div>
            <div style="margin-left: 48px;">
            <details>
                <summary>
                    <h4 style="margin-bottom: 0px; display: inline;">Worker: 0</h4>
                </summary>
                <table style="width: 100%; text-align: left;">
                    <tr>
                        <td style="text-align: left;">
                            <strong>Comm: </strong> tcp://127.0.0.1:44895
                        </td>
                        <td style="text-align: left;">
                            <strong>Total threads: </strong> 6
                        </td>
                    </tr>
                    <tr>
                        <td style="text-align: left;">
                            <strong>Dashboard: </strong> <a href="http://127.0.0.1:41109/status" target="_blank">http://127.0.0.1:41109/status</a>
                        </td>
                        <td style="text-align: left;">
                            <strong>Memory: </strong> 1.92 GiB
                        </td>
                    </tr>
                    <tr>
                        <td style="text-align: left;">
                            <strong>Nanny: </strong> tcp://127.0.0.1:39471
                        </td>
                        <td style="text-align: left;"></td>
                    </tr>
                    <tr>
                        <td colspan="2" style="text-align: left;">
                            <strong>Local directory: </strong> /tmp/dask-scratch-space/worker-ioedatmr
                        </td>
                    </tr>





                </table>
            </details>
            </div>
        </div>

        <div style="margin-bottom: 20px;">
            <div style="width: 24px; height: 24px; background-color: #DBF5FF; border: 3px solid #4CC9FF; border-radius: 5px; position: absolute;"> </div>
            <div style="margin-left: 48px;">
            <details>
                <summary>
                    <h4 style="margin-bottom: 0px; display: inline;">Worker: 1</h4>
                </summary>
                <table style="width: 100%; text-align: left;">
                    <tr>
                        <td style="text-align: left;">
                            <strong>Comm: </strong> tcp://127.0.0.1:35853
                        </td>
                        <td style="text-align: left;">
                            <strong>Total threads: </strong> 6
                        </td>
                    </tr>
                    <tr>
                        <td style="text-align: left;">
                            <strong>Dashboard: </strong> <a href="http://127.0.0.1:42527/status" target="_blank">http://127.0.0.1:42527/status</a>
                        </td>
                        <td style="text-align: left;">
                            <strong>Memory: </strong> 1.92 GiB
                        </td>
                    </tr>
                    <tr>
                        <td style="text-align: left;">
                            <strong>Nanny: </strong> tcp://127.0.0.1:44081
                        </td>
                        <td style="text-align: left;"></td>
                    </tr>
                    <tr>
                        <td colspan="2" style="text-align: left;">
                            <strong>Local directory: </strong> /tmp/dask-scratch-space/worker-t0mykxrk
                        </td>
                    </tr>





                </table>
            </details>
            </div>
        </div>

        <div style="margin-bottom: 20px;">
            <div style="width: 24px; height: 24px; background-color: #DBF5FF; border: 3px solid #4CC9FF; border-radius: 5px; position: absolute;"> </div>
            <div style="margin-left: 48px;">
            <details>
                <summary>
                    <h4 style="margin-bottom: 0px; display: inline;">Worker: 2</h4>
                </summary>
                <table style="width: 100%; text-align: left;">
                    <tr>
                        <td style="text-align: left;">
                            <strong>Comm: </strong> tcp://127.0.0.1:32787
                        </td>
                        <td style="text-align: left;">
                            <strong>Total threads: </strong> 6
                        </td>
                    </tr>
                    <tr>
                        <td style="text-align: left;">
                            <strong>Dashboard: </strong> <a href="http://127.0.0.1:39975/status" target="_blank">http://127.0.0.1:39975/status</a>
                        </td>
                        <td style="text-align: left;">
                            <strong>Memory: </strong> 1.92 GiB
                        </td>
                    </tr>
                    <tr>
                        <td style="text-align: left;">
                            <strong>Nanny: </strong> tcp://127.0.0.1:44181
                        </td>
                        <td style="text-align: left;"></td>
                    </tr>
                    <tr>
                        <td colspan="2" style="text-align: left;">
                            <strong>Local directory: </strong> /tmp/dask-scratch-space/worker-tf388_05
                        </td>
                    </tr>





                </table>
            </details>
            </div>
        </div>

        <div style="margin-bottom: 20px;">
            <div style="width: 24px; height: 24px; background-color: #DBF5FF; border: 3px solid #4CC9FF; border-radius: 5px; position: absolute;"> </div>
            <div style="margin-left: 48px;">
            <details>
                <summary>
                    <h4 style="margin-bottom: 0px; display: inline;">Worker: 3</h4>
                </summary>
                <table style="width: 100%; text-align: left;">
                    <tr>
                        <td style="text-align: left;">
                            <strong>Comm: </strong> tcp://127.0.0.1:44029
                        </td>
                        <td style="text-align: left;">
                            <strong>Total threads: </strong> 6
                        </td>
                    </tr>
                    <tr>
                        <td style="text-align: left;">
                            <strong>Dashboard: </strong> <a href="http://127.0.0.1:43901/status" target="_blank">http://127.0.0.1:43901/status</a>
                        </td>
                        <td style="text-align: left;">
                            <strong>Memory: </strong> 1.92 GiB
                        </td>
                    </tr>
                    <tr>
                        <td style="text-align: left;">
                            <strong>Nanny: </strong> tcp://127.0.0.1:40235
                        </td>
                        <td style="text-align: left;"></td>
                    </tr>
                    <tr>
                        <td colspan="2" style="text-align: left;">
                            <strong>Local directory: </strong> /tmp/dask-scratch-space/worker-jmlptawh
                        </td>
                    </tr>





                </table>
            </details>
            </div>
        </div>


    </details>
</div>

        </details>
    </div>
</div>
            </details>


    </div>
</div>



You can also see the status and more information at the Dashboard, found at http://<ip_address>/status. This can be ignored now since this is pointing to local machine.

With our client and workers setup, it's time to execute our first program in parallel. We'll define a function called add_5_to_x that takes some value x and adds 5 to it.

Você também pode ver o status e mais informações no Dashboard, encontrado em http://<ip_address>/status. Isso pode ser ignorado agora, pois está apontando para a máquina local. Com a configuração do cliente e dos trabalhadores, é hora de executar nosso primeiro programa em paralelo. Definiremos uma função chamada add_5_to_x que recebe algum valor x e adiciona 5 a ele.


```python
def add_5_to_x(x):
    return x + 5
```

Next, we'll iterate through our n_workers and create an execution graph, where each worker is responsible for taking its ID and passing it to the function add_5_to_x. For example, the worker with ID 2 will take its ID and pass it to the function add_5_to_x, resulting in the value 7.

A seguir, iremos iterar através de nossos n_workers e criar um gráfico de execução, onde cada trabalhador é responsável por pegar seu ID e passá-lo para a função add_5_to_x. Por exemplo, o trabalhador com ID 2 pegará seu ID e o passará para a função add_5_to_x, resultando no valor 7.


```python
from dask import delayed


addition_operations = [delayed(add_5_to_x)(i) for i in range(n_workers)]
addition_operations
```




    [Delayed('add_5_to_x-4c0ff802-4d66-41b4-adbb-e3e8542532d9'),
     Delayed('add_5_to_x-ea344c11-d675-4f8b-83c7-c96a0e015da7'),
     Delayed('add_5_to_x-093d2c6d-4eb0-41f3-a38d-f73c23653800'),
     Delayed('add_5_to_x-d9af2829-552e-497b-bc61-fca5a643bcf5')]



The above output shows a list of several Delayed objects. An important thing to note is that the workers aren't actually executing these results - we're just defining the execution graph for our client to execute later. The delayed function wraps our function add_5_to_x and returns a Delayed object. This ensures that this computation is in fact "delayed" - or lazily evaluated - and not executed on the spot i.e. when we define it.

Next, let's sum each one of these intermediate results. We can accomplish this by wrapping Python's built-in sum function using our delayed function and storing this in a variable called total.

A saída acima mostra uma lista de vários objetos atrasados. Uma coisa importante a notar é que os trabalhadores não estão realmente executando esses resultados - estamos apenas definindo o gráfico de execução para nosso cliente executar mais tarde. A função atrasada envolve nossa função add_5_to_x e retorna um objeto Atrasado. Isso garante que este cálculo seja de fato "atrasado" - ou avaliado preguiçosamente - e não executado no local, ou seja, quando o definimos. A seguir, vamos somar cada um desses resultados intermediários. Podemos fazer isso agrupando a função sum integrada do Python usando nossa função atrasada e armazenando isso em uma variável chamada total.


```python
total = delayed(sum)(addition_operations)
total
```




    Delayed('sum-230eb00e-b56e-47c5-98b7-4197ebd243c3')



Using the graphviz library, we can use the visualize method of a Delayed object to visualize our current graph.
Usando a biblioteca graphviz, podemos usar o método de visualização de um objeto Delayed para visualizar nosso gráfico atual.


```python
!pip install graphviz -q
```


```python
import os
try:
    import graphviz
except ModuleNotFoundError:
    os.system('conda install -c conda-forge graphviz -y')
    os.system('conda install -c conda-forge python-graphviz -y')
```


```python
#total.visualize()
```


```python

```

As we mentioned before, none of these results - intermediate or final - have actually been compute. We can compute them using the compute method of our client.
Como mencionamos anteriormente, nenhum desses resultados – intermediários ou finais – foi realmente computado. Podemos calculá-los usando o método de computação do nosso cliente.


```python
from dask.distributed import wait
import time


addition_futures = client.compute(addition_operations, optimize_graph=False, fifo_timeout="0ms")
total_future = client.compute(total, optimize_graph=False, fifo_timeout="0ms")
wait(total_future)  # this will give Dask time to execute the work
```




    DoneAndNotDoneFutures(done={<Future: finished, type: int, key: sum-230eb00e-b56e-47c5-98b7-4197ebd243c3>}, not_done=set())




```python
addition_futures
```




    [<Future: finished, type: int, key: add_5_to_x-4c0ff802-4d66-41b4-adbb-e3e8542532d9>,
     <Future: finished, type: int, key: add_5_to_x-ea344c11-d675-4f8b-83c7-c96a0e015da7>,
     <Future: finished, type: int, key: add_5_to_x-093d2c6d-4eb0-41f3-a38d-f73c23653800>,
     <Future: finished, type: int, key: add_5_to_x-d9af2829-552e-497b-bc61-fca5a643bcf5>]



We can see from the above output that our addition_futures variable is a list of Future objects - not the "actual results" of adding 5 to each of [0, 1, 2, 3]. These Future objects are a promise that at one point a computation will take place and we will be left with a result. Dask is responsible for fulfilling that promise by delegating that task to the appropriate Dask worker and collecting the result.

Let's take a look at our total_future object:

Podemos ver na saída acima que nossa variável add_futures é uma lista de objetos Future - não os "resultados reais" da adição de 5 a cada um de [0, 1, 2, 3]. Esses objetos Future são uma promessa de que em determinado momento ocorrerá um cálculo e teremos um resultado. Dask é responsável por cumprir essa promessa, delegando essa tarefa ao trabalhador Dask apropriado e coletando o resultado. Vamos dar uma olhada em nosso objeto total_future:


```python
print(total_future)
print(type(total_future))
```

    <Future: finished, type: int, key: sum-230eb00e-b56e-47c5-98b7-4197ebd243c3>
    <class 'distributed.client.Future'>


Again, we see that this is an object of type Future as well as metadata about the status of the request (i.e. whether it has finished or not), the type of the result, and a key associated with that operation. To collect and print the result of each of these Future objects, we can call the result() method.
Novamente, vemos que este é um objeto do tipo Future, bem como metadados sobre o status da solicitação (ou seja, se ela foi concluída ou não), o tipo de resultado e uma chave associada a essa operação. Para coletar e imprimir o resultado de cada um desses objetos Future, podemos chamar o método result().


```python
addition_results = [future.result() for future in addition_futures]
print('Addition Results:', addition_results)
```

    Addition Results: [5, 6, 7, 8]


Now we see the results that we want from our addition operations. We can also use the simpler syntax of the client.gather method to collect our results.
Agora vemos os resultados que queremos das nossas operações de adição. Também podemos usar a sintaxe mais simples do método client.gather para coletar nossos resultados.


```python
addition_results = client.gather(addition_futures)
total_result = client.gather(total_future)
print('Addition Results:', addition_results)
print('Total Result:', total_result)
```

    Addition Results: [5, 6, 7, 8]
    Total Result: 26


Awesome! We just wrote our first distributed workflow.

To confirm that Dask is truly executing in parallel, let's define a function that sleeps for 1 second and returns the string "Success!". In serial, this function should take our 4 workers around 4 seconds to execute.

Incrível! Acabamos de escrever nosso primeiro fluxo de trabalho distribuído. Para confirmar que Dask está realmente executando em paralelo, vamos definir uma função que durma por 1 segundo e retorne a string "Sucesso!". Em série, esta função deve levar cerca de 4 segundos para nossos 4 trabalhadores serem executados.


```python
def sleep_1():
    time.sleep(1)
    return 'Success!'
```


```python
%%time

for _ in range(n_workers):
    sleep_1()
```

    CPU times: user 331 ms, sys: 91.9 ms, total: 423 ms
    Wall time: 4 s


As expected, our process takes about 4 seconds to run. Now let's execute this same workflow in parallel using Dask.
Como esperado, nosso processo leva cerca de 4 segundos para ser executado. Agora vamos executar esse mesmo fluxo de trabalho em paralelo usando Dask.




```python
%%time

# define delayed execution graph
sleep_operations = [delayed(sleep_1)() for _ in range(n_workers)]

# use client to perform computations using execution graph
sleep_futures = client.compute(sleep_operations, optimize_graph=False, fifo_timeout="0ms")

# collect and print results
sleep_results = client.gather(sleep_futures)
print(sleep_results)
```

    ['Success!', 'Success!', 'Success!', 'Success!']
    CPU times: user 127 ms, sys: 10 ms, total: 137 ms
    Wall time: 1.03 s


Using Dask, we see that this whole process takes a little over a second - each worker is executing in parallel!
Usando o Dask, vemos que todo esse processo leva pouco mais de um segundo - cada trabalhador está executando em paralelo!

### Dask Cudf
Let's start by creating a local cluster of workers and a client to interact with that cluster.
Vamos começar criando um cluster local de trabalhadores e um cliente para interagir com esse cluster.


```python
from dask.distributed import Client
from dask_cuda import LocalCUDACluster


# create a local CUDA cluster
cluster = LocalCUDACluster()
client = Client(cluster)
client
```

    /home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages/distributed/node.py:182: UserWarning: Port 8787 is already in use.
    Perhaps you already have a cluster running?
    Hosting the HTTP server on port 40393 instead
      warnings.warn(
    /home/jcnok/bootcamps/bootcamp-jornada-de-dados_2024/.venv/lib/python3.11/site-packages/dask_cuda/utils.py:170: UserWarning: Cannot get CPU affinity for device with index 0, setting default affinity
      warnings.warn(





<div>
    <div style="width: 24px; height: 24px; background-color: #e1e1e1; border: 3px solid #9D9D9D; border-radius: 5px; position: absolute;"> </div>
    <div style="margin-left: 48px;">
        <h3 style="margin-bottom: 0px;">Client</h3>
        <p style="color: #9D9D9D; margin-bottom: 0px;">Client-d4105a06-e01c-11ee-8a5c-6174df56fd34</p>
        <table style="width: 100%; text-align: left;">

        <tr>

            <td style="text-align: left;"><strong>Connection method:</strong> Cluster object</td>
            <td style="text-align: left;"><strong>Cluster type:</strong> dask_cuda.LocalCUDACluster</td>

        </tr>


            <tr>
                <td style="text-align: left;">
                    <strong>Dashboard: </strong> <a href="http://127.0.0.1:40393/status" target="_blank">http://127.0.0.1:40393/status</a>
                </td>
                <td style="text-align: left;"></td>
            </tr>


        </table>




            <details>
            <summary style="margin-bottom: 20px;"><h3 style="display: inline;">Cluster Info</h3></summary>
            <div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-mod-trusted jp-OutputArea-output">
    <div style="width: 24px; height: 24px; background-color: #e1e1e1; border: 3px solid #9D9D9D; border-radius: 5px; position: absolute;">
    </div>
    <div style="margin-left: 48px;">
        <h3 style="margin-bottom: 0px; margin-top: 0px;">LocalCUDACluster</h3>
        <p style="color: #9D9D9D; margin-bottom: 0px;">d73dbc79</p>
        <table style="width: 100%; text-align: left;">
            <tr>
                <td style="text-align: left;">
                    <strong>Dashboard:</strong> <a href="http://127.0.0.1:40393/status" target="_blank">http://127.0.0.1:40393/status</a>
                </td>
                <td style="text-align: left;">
                    <strong>Workers:</strong> 1
                </td>
            </tr>
            <tr>
                <td style="text-align: left;">
                    <strong>Total threads:</strong> 1
                </td>
                <td style="text-align: left;">
                    <strong>Total memory:</strong> 7.68 GiB
                </td>
            </tr>

            <tr>
    <td style="text-align: left;"><strong>Status:</strong> running</td>
    <td style="text-align: left;"><strong>Using processes:</strong> True</td>
</tr>


        </table>

        <details>
            <summary style="margin-bottom: 20px;">
                <h3 style="display: inline;">Scheduler Info</h3>
            </summary>

            <div style="">
    <div>
        <div style="width: 24px; height: 24px; background-color: #FFF7E5; border: 3px solid #FF6132; border-radius: 5px; position: absolute;"> </div>
        <div style="margin-left: 48px;">
            <h3 style="margin-bottom: 0px;">Scheduler</h3>
            <p style="color: #9D9D9D; margin-bottom: 0px;">Scheduler-9a061646-4f18-402f-b3ae-c5987d3bf187</p>
            <table style="width: 100%; text-align: left;">
                <tr>
                    <td style="text-align: left;">
                        <strong>Comm:</strong> tcp://127.0.0.1:37575
                    </td>
                    <td style="text-align: left;">
                        <strong>Workers:</strong> 1
                    </td>
                </tr>
                <tr>
                    <td style="text-align: left;">
                        <strong>Dashboard:</strong> <a href="http://127.0.0.1:40393/status" target="_blank">http://127.0.0.1:40393/status</a>
                    </td>
                    <td style="text-align: left;">
                        <strong>Total threads:</strong> 1
                    </td>
                </tr>
                <tr>
                    <td style="text-align: left;">
                        <strong>Started:</strong> Just now
                    </td>
                    <td style="text-align: left;">
                        <strong>Total memory:</strong> 7.68 GiB
                    </td>
                </tr>
            </table>
        </div>
    </div>

    <details style="margin-left: 48px;">
        <summary style="margin-bottom: 20px;">
            <h3 style="display: inline;">Workers</h3>
        </summary>


        <div style="margin-bottom: 20px;">
            <div style="width: 24px; height: 24px; background-color: #DBF5FF; border: 3px solid #4CC9FF; border-radius: 5px; position: absolute;"> </div>
            <div style="margin-left: 48px;">
            <details>
                <summary>
                    <h4 style="margin-bottom: 0px; display: inline;">Worker: 0</h4>
                </summary>
                <table style="width: 100%; text-align: left;">
                    <tr>
                        <td style="text-align: left;">
                            <strong>Comm: </strong> tcp://127.0.0.1:35241
                        </td>
                        <td style="text-align: left;">
                            <strong>Total threads: </strong> 1
                        </td>
                    </tr>
                    <tr>
                        <td style="text-align: left;">
                            <strong>Dashboard: </strong> <a href="http://127.0.0.1:43695/status" target="_blank">http://127.0.0.1:43695/status</a>
                        </td>
                        <td style="text-align: left;">
                            <strong>Memory: </strong> 7.68 GiB
                        </td>
                    </tr>
                    <tr>
                        <td style="text-align: left;">
                            <strong>Nanny: </strong> tcp://127.0.0.1:37061
                        </td>
                        <td style="text-align: left;"></td>
                    </tr>
                    <tr>
                        <td colspan="2" style="text-align: left;">
                            <strong>Local directory: </strong> /tmp/dask-scratch-space/worker-drnl3y_d
                        </td>
                    </tr>





                </table>
            </details>
            </div>
        </div>


    </details>
</div>

        </details>
    </div>
</div>
            </details>


    </div>
</div>



    2024-03-12 00:30:05,011 - distributed.core - INFO - Received 'close-stream' from tcp://127.0.0.1:48720; closing.
    2024-03-12 00:30:05,014 - distributed.scheduler - INFO - Remove worker <WorkerState 'tcp://127.0.0.1:35241', name: 0, status: closing, memory: 3, processing: 0> (stimulus_id='handle-worker-cleanup-1710214205.01484')
    2024-03-12 00:30:05,016 - distributed.scheduler - INFO - Lost all workers
    2024-03-12 00:30:06,132 - distributed.scheduler - INFO - Scheduler closing due to unknown reason...
    2024-03-12 00:30:06,136 - distributed.scheduler - INFO - Scheduler closing all comms


We'll define a function called load_data that will create a cudf.DataFrame with two columns, key and value. The column key will be randomly filled with either a 0 or a 1, with 50% probability of either number being selected. The column value will be randomly filled with numbers sampled from a normal distribution.

Definiremos uma função chamada load_data que criará um cudf.DataFrame com duas colunas, chave e valor. A chave da coluna será preenchida aleatoriamente com 0 ou 1, com 50% de probabilidade de qualquer um dos números ser selecionado. O valor da coluna será preenchido aleatoriamente com números amostrados de uma distribuição normal.


```python
import cudf; print('cuDF Version:', cudf.__version__)
import numpy as np; print('NumPy Version:', np.__version__)


def load_data(n_rows):
    df = cudf.DataFrame()
    random_state = np.random.RandomState(43210)
    df['key'] = random_state.binomial(n=1, p=0.5, size=(n_rows,))
    df['value'] = random_state.normal(size=(n_rows,))
    return df
```

    cuDF Version: 24.04.00a546
    NumPy Version: 1.26.4


We'll also define a function head that takes a cudf.DataFrame and returns the first 5 rows.
Também definiremos um cabeçalho de função que recebe cudf.DataFrame e retorna as 5 primeiras linhas.


```python
def head(dataframe):
    return dataframe.head()
```

We'll define the number of workers as well as the number of rows each dataframe will have.
Definiremos o número de trabalhadores, bem como o número de linhas que cada dataframe terá.



```python
# define the number of workers
n_workers = 1  # feel free to change this depending on how many GPUs you have

# define the number of rows each dataframe will have
n_rows = 125000000  # we'll use 125 million rows in each dataframe
```

We'll create each dataframe using the delayed operator.
Criaremos cada dataframe usando o operador atrasado.


```python
from dask.delayed import delayed


# create each dataframe using a delayed operation
dfs = [delayed(load_data)(n_rows) for i in range(n_workers)]
dfs
```




    [Delayed('load_data-f841e897-3a26-45fb-8278-a9fe8eec0745')]



Vemos que o resultado desta operação é uma lista de objetos atrasados. É importante notar que estas operações estão “atrasadas” – nada foi computado ainda, ou seja, nossos dados ainda não foram criados! Podemos aplicar a função head a cada um de nossos dataframes "atrasados".


```python
head_dfs = [delayed(head)(df) for df in dfs]
head_dfs
```




    [Delayed('head-3beb5e6e-57b2-4736-9bc3-0c4832d33392')]




Como antes, vemos que o resultado é uma lista de objetos Delayed – uma coisa importante a notar é que nossa “chave”, ou identificador exclusivo para cada operação, mudou. Você deverá ver o nome do cabeçalho da função seguido por um sinal de cerquilha. Por exemplo, pode-se ver: [Delayed('head-8e946db2-feaf-4e79-99ab-f732b6e28461') Delayed('head-eb06bc77-9d5c-4a47-8c01-b5b36710b727')] Novamente, nada foi computado - vamos calcular os resultados e execute o fluxo de trabalho usando o método client.compute().


```python
from dask.distributed import wait


# use the client to compute - this means create each dataframe and take the head
futures = client.compute(head_dfs)
wait(futures)  # this will give Dask time to execute the work before moving to any subsequently defined operations
futures
```




    [<Future: finished, type: cudf.core.dataframe.DataFrame, key: head-3beb5e6e-57b2-4736-9bc3-0c4832d33392>]



We see that our results are a list of futures. Each object in this list tells us a bit information about itself: the status (pending, error, finished), the type of the object, and the key (unique identifief).

We can use the client.gather method to collect the results of each of these futures.

Vemos que nossos resultados são uma lista de futuros. Cada objeto nesta lista nos fornece algumas informações sobre si mesmo: o status (pendente, erro, concluído), o tipo do objeto e a chave (identificação única). Podemos usar o método client.gather para coletar os resultados de cada um desses futuros.


```python
# collect the results
results = client.gather(futures)
results
```




    [   key     value
     0    1  0.689155
     1    0  0.999085
     2    0 -0.277850
     3    1 -1.535017
     4    1 -0.028184]



We see that our results are a list of cuDF DataFrames, each having 2 columns and 5 rows. Let's inspect the first dataframe:
Vemos que nossos resultados são uma lista de DataFrames cuDF, cada um com 2 colunas e 5 linhas. Vamos inspecionar o primeiro dataframe:


```python
# let's inspect the head of the first dataframe
print(results[0])
```

       key     value
    0    1  0.689155
    1    0  0.999085
    2    0 -0.277850
    3    1 -1.535017
    4    1 -0.028184


That was a pretty simple example. Let's see how we can use this perform a more complex operation like figuring how many total rows we have across all of our dataframes. We'll define a function called length that will take a cudf.DataFrame and return the first value of the shape attribute i.e. the number of rows for that particular dataframe.

Esse foi um exemplo bem simples. Vamos ver como podemos usar isso para realizar uma operação mais complexa, como descobrir quantas linhas totais temos em todos os nossos dataframes. Definiremos uma função chamada length que pegará um cudf.DataFrame e retornará o primeiro valor do atributo shape, ou seja, o número de linhas para aquele dataframe específico.


```python
def length(dataframe):
    return dataframe.shape[0]
```

We'll define our operation on the dataframes we've created:
Definiremos nossa operação nos dataframes que criamos:


```python
lengths = [delayed(length)(df) for df in dfs]
lengths
```




    [Delayed('length-fff0b6ca-f3eb-4698-bc09-51d97eae936e')]



And then use Python's built-in sum function to sum all of these lengths.
E então use a função sum integrada do Python para somar todos esses comprimentos.


```python
total_number_of_rows = delayed(sum)(lengths)

```

At this point, total_number_of_rows hasn't been computed yet. But we can still visualize the graph of operations we've defined using the visualize() method.
Neste ponto, total_number_of_rows ainda não foi calculado. Mas ainda podemos visualizar o gráfico de operações que definimos usando o método visualize().


```python
# total_number_of_rows.visualize()
```

The graph can be read from bottom to top. We see that for each worker, we will first execute the load_data function to create each dataframe. Then the function length will be applied to each dataframe; the results from these operations on each worker will then be combined into a single result via the sum function.

Let's now execute our workflow and compute a value for the total_number_of_rows variable.

O gráfico pode ser lido de baixo para cima. Vemos que para cada trabalhador, primeiro executaremos a função load_data para criar cada dataframe. Em seguida, o comprimento da função será aplicado a cada dataframe; os resultados dessas operações em cada trabalhador serão então combinados em um único resultado por meio da função soma. Vamos agora executar nosso fluxo de trabalho e calcular um valor para a variável total_number_of_rows.


```python
# use the client to compute the result and wait for it to finish
future = client.compute(total_number_of_rows)
wait(future)
future
```




<strong>Future: sum</strong>
<span style="color: var(--jp-ui-font-color2, gray)"> status: </span>


<span style="color: var(--jp-error-color0, black)">finished</span>,



<span style="color: var(--jp-ui-font-color2, gray)"> type:</span> int,


<span style="color: var(--jp-ui-font-color2, gray)"> key:</span> sum-4786aa41-17e6-4928-b8c2-24aa529014a4



We see that our computation has finished - our result is of type int. We can collect our result using the client.gather() method.
Vemos que nosso cálculo foi concluído – nosso resultado é do tipo int. Podemos coletar nosso resultado usando o método client.gather().


```python
# collect result
result = client.gather(future)
result
```




    125000000



That's all there is to it! We can define even more complex operations and workflows using cuDF DataFrames by using the delayed, wait, client.submit(), and client.gather() workflow.

However, there can sometimes be a drawback from using this pattern. For example, consider a common operation such as a groupby - we might want to group on certain keys and aggregate the values to compute a mean, variance, or even more complex aggregations. Each dataframe is located on a different GPU - and we're not guaranteed that all of the keys necessary for that groupby operation are located on a single GPU i.e. keys may be scattered across multiple GPUs.

To make our problem even more concrete, let's consider the simple operation of grouping on our key column and calculating the mean of the value column. To sovle this problem, we'd have to sort the data and transfer keys and their associated values from one GPU to another - a tricky thing to do using the delayed pattern. In the example below, we'll show an example of this issue with the delayed pattern and motivate why one might consider using the dask_cudf API.

First, let's define a function groupby that takes a cudf.DataFrame, groups by the key column, and calculates the mean of the value column.

Isso é tudo que há para fazer! Podemos definir operações e fluxos de trabalho ainda mais complexos usando cuDF DataFrames usando o fluxo de trabalho atrasado, de espera, client.submit() e client.gather(). No entanto, às vezes pode haver uma desvantagem no uso desse padrão. Por exemplo, considere uma operação comum como groupby - podemos querer agrupar em determinadas chaves e agregar os valores para calcular uma média, variância ou agregações ainda mais complexas. Cada dataframe está localizado em uma GPU diferente - e não temos garantia de que todas as chaves necessárias para essa operação de agrupamento estejam localizadas em uma única GPU, ou seja, as chaves podem estar espalhadas por várias GPUs. Para tornar nosso problema ainda mais concreto, vamos considerar a operação simples de agrupar em nossa coluna-chave e calcular a média da coluna de valor. Para resolver esse problema, teríamos que classificar os dados e transferir chaves e seus valores associados de uma GPU para outra - algo complicado de fazer usando o padrão atrasado. No exemplo abaixo, mostraremos um exemplo desse problema com o padrão atrasado e motivaremos por que alguém pode considerar o uso da API dask_cudf. Primeiro, vamos definir uma função groupby que pega um cudf.DataFrame, agrupa pela coluna-chave e calcula a média da coluna de valor.


```python
def groupby(dataframe):
    return dataframe.groupby('key')['value'].mean()
```

We'll apply the function groupby to each dataframe using the delayed operation.
Aplicaremos a função groupby a cada dataframe usando a operação atrasada.


```python
groupbys = [delayed(groupby)(df) for df in dfs]
```


```python
# use the client to compute the result and wait for it to finish
groupby_dfs = client.compute(groupbys)
wait(groupby_dfs)
groupby_dfs
```




    [<Future: finished, type: cudf.core.series.Series, key: groupby-03b5af48-c53f-424f-bebb-06dc1a521cf8>]




```python
results = client.gather(groupby_dfs)
results
```




    [key
     0   -0.000173
     1   -0.000059
     Name: value, dtype: float64]




```python
for i, result in enumerate(results):
    print('cuDF DataFrame:', i)
    print(result)
```

    cuDF DataFrame: 0
    key
    0   -0.000173
    1   -0.000059
    Name: value, dtype: float64


This isn't exactly what we wanted though - ideally, we'd get one dataframe where for each unique key (0 and 1), we get the mean of the value column.

We can use the dask_cudf API to help up solve this problem. First we'll import the dask_cudf library and then use the dask_cudf.from_delayed function to convert our list of delayed dataframes to an object of type dask_cudf.core.DataFrame. We'll use this object - distributed_df - along with the dask_cudf API to perform that "tricky" groupby operation.

Porém, isso não é exatamente o que queríamos - idealmente, obteríamos um dataframe onde, para cada chave exclusiva (0 e 1), obteríamos a média da coluna de valor. Podemos usar a API dask_cudf para ajudar a resolver este problema. Primeiro importaremos a biblioteca dask_cudf e depois usaremos a função dask_cudf.from_delayed para converter nossa lista de dataframes atrasados ​​em um objeto do tipo dask_cudf.core.DataFrame. Usaremos este objeto - distribuído_df - junto com a API dask_cudf para realizar aquela operação "complicada" de agrupamento.


```python

```


```python
import dask_cudf; print('Dask cuDF Version:', dask_cudf.__version__)


# create a distributed cuDF DataFrame using Dask
distributed_df = dask_cudf.from_delayed(dfs)
print('Type:', type(distributed_df))
distributed_df
```

    Dask cuDF Version: 24.04.00a546
    Type: <class 'dask_cudf.core.DataFrame'>





<div><strong>Dask DataFrame Structure:</strong></div>
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
      <th>key</th>
      <th>value</th>
    </tr>
    <tr>
      <th>npartitions=1</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th></th>
      <td>int64</td>
      <td>float64</td>
    </tr>
    <tr>
      <th></th>
      <td>...</td>
      <td>...</td>
    </tr>
  </tbody>
</table>
</div>
<div>Dask Name: from-delayed, 2 graph layers</div>



The dask_cudf API closely mirrors the cuDF API. We can use a groupby similar to how we would with cuDF - but this time, our operation is distributed across multiple GPUs!
A API dask_cudf reflete de perto a API cuDF. Podemos usar um groupby semelhante ao que faríamos com cuDF - mas desta vez, nossa operação é distribuída por várias GPUs!


```python
result = distributed_df.groupby('key')['value'].mean().compute()
result
```

Lastly, let's examine our result!

Por último, vamos examinar nosso resultado!


```python
print(result)
```

    key
    0   -0.000173
    1   -0.000059
    Name: value, dtype: float64


## Resultados:

#### Segue abaixo o resultado do ranking geral de todos os testes realizados para calcular o min, max e média ordenado pela cidade em um bilhão de linhas.

* **obs:** Vale ressaltar que esse resultado só serve de parâmetro para minha máquina, com base nos scripts gerados aqui, certamente cabem espaços para otimização e em outros cenários os resultados podem ser bem divergentes.
* segue as configurações da minha máquina abaixo:

#### Memória:
Memory block size:       128M
Total online memory:      12G
Total offline memory:      0B

#### CPU:
Architecture:            x86_64
  CPU op-mode(s):        32-bit, 64-bit
  Address sizes:         46 bits physical, 48 bits virtual
  Byte Order:            Little Endian
CPU(s):                  24
  On-line CPU(s) list:   0-23
Vendor ID:               GenuineIntel
  Model name:            Intel(R) Xeon(R) CPU E5-2670 v3 @ 2.30GHz
    CPU family:          6
    Model:               63
    Thread(s) per core:  2
    Core(s) per socket:  12
    Socket(s):           1

#### GPU:
RTX 3060ti 8Gbs


```python
!poetry add matplotlib
```


```python
#script para plotar um grafico do ranking geral.
import csv
import matplotlib.pyplot as plt

# Leitura dos dados do arquivo CSV
dados = []

with open('data/tempos_execucao.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        nome_funcao = row[0]
        tempo = row[1].split()  # Separa minutos e segundos
        if len(tempo) == 2 and tempo[1] == 'segundos':  # Se houver apenas segundos
            tempo_total = float(tempo[0])
        elif len(tempo) == 4:  # Se houver minutos e segundos
            minutos = float(tempo[0])
            segundos = float(tempo[2])
            tempo_total = minutos * 60 + segundos  # Converte minutos para segundos
        else:
            raise ValueError(f'Formato de tempo inválido: {row[1]}')
        dados.append((nome_funcao, tempo_total))

# Ordena os dados pelo tempo de execução
dados_ordenados = sorted(dados, key=lambda x: x[1])

# Extrai os nomes das funções e os tempos de execução ordenados
nomes_funcoes_ordenados = [item[0] for item in dados_ordenados]
tempos_execucao_ordenados = [item[1] for item in dados_ordenados]

# Plotagem do gráfico
plt.figure(figsize=(10, 6))
plt.barh(nomes_funcoes_ordenados, tempos_execucao_ordenados, color='skyblue')
plt.xlabel('Tempo de Execução (segundos)')
plt.ylabel('Função')
plt.title('Tempo de Execução das Funções (Ordenado)')
plt.grid(axis='x')
plt.tight_layout()

# Adicionando os valores nas barras
for i, valor in enumerate(tempos_execucao_ordenados):
    plt.text(valor, i, f'{valor:.2f} s', va='center')

# Exibindo o gráfico
plt.show()

```


    
![png](output_179_0.png)
    



```python

```


```python
<a id="ancora01"></a>
```


```python
<a id="ancora02"></a>
```


```python
<a id="ancora03"></a>
```


```python
<a id="ancora04"></a>
```


```python
<a id="ancora05"></a>
```


```python
<a id="ancora06"></a>
```


```python
<a id="ancora07"></a>
```


```python
<a id="ancora08"></a>
```


```python
<a id="ancora09"></a>
```


```python
<a id="ancora10"></a>
```


```python
<a id="ancora11"></a>
```


```python
<a id="ancora12"></a>
```


```python
<a id="ancora13"></a>
```


```python
<a id="ancora14"></a>
```


```python
<a id="ancora15"></a>
```


```python
<a id="ancora16"></a>
```


```python
<a id="ancora17"></a>
```


```python
<a id="ancora18"></a>
```


```python
<a id="ancora19"></a>
```


```python
<a id="ancora20"></a>
```


```python

```
