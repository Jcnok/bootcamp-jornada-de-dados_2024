import os
import sys
import time
import faker
import random
import cupy as cp
from tqdm import tqdm
from multiprocessing import Pool

# Cria um objeto Faker
fake = faker.Faker()

# Função para gerar dados de teste
def generate_test_data(num_rows, chunk_size, station_names):
  """
  Gera dados de teste e os escreve em um arquivo.

  Argumentos:
    num_rows: Número de linhas a serem geradas.
    chunk_size: Tamanho do bloco de dados a ser gerado por cada thread.
    station_names: Lista de nomes de estações meteorológicas.

  Retorno:
    None.
  """
  with open("data/measurements.txt", "w", encoding="utf-8") as file:
    for i in tqdm(range(0, num_rows, chunk_size)):
      # Gera um bloco de dados
      data_chunk = generate_data_chunk(chunk_size, station_names)
      file.writelines(data_chunk)

# Função para gerar um bloco de dados
def generate_data_chunk(chunk_size, station_names):
  """
  Gera um bloco de dados de tamanho `chunk_size`.

  Argumentos:
    chunk_size: Tamanho do bloco de dados.
    station_names: Lista de nomes de estações meteorológicas.

  Retorno:
    Lista de strings contendo os dados de teste.
  """
  # Aloca memória na GPU
  max_length = 30  # Limite de tamanho da string
  station_names_limited = [name[:max_length] for name in station_names]
  station_names_gpu = cp.asarray(station_names_limited)

  # Gera temperaturas aleatórias na GPU
  temperatures_gpu = cp.random.uniform(-50, 100, (chunk_size, 2))
  temperatures_gpu = cp.around(temperatures_gpu, 1)

  # Seleciona a temperatura final
  temperatures_gpu = cp.where(temperatures_gpu[:, 0] < 50, temperatures_gpu[:, 0], temperatures_gpu[:, 1])

  # Converte os dados para strings
  data_chunk = []
  for i in range(chunk_size):
    station_name = station_names_gpu[i].item()
    temperature = temperatures_gpu[i].item()
    data_chunk.append(f"{station_name};{temperature}\n")

  return data_chunk

# Solicita o número de linhas ao usuário
num_rows = int(input("Digite o número de linhas a serem geradas: "))

# Define o tamanho do bloco de dados
chunk_size = 1_000_000

# Número de threads
num_workers = os.cpu_count()

# Carrega a lista de estações
with open("data/weather_stations.csv", "r", encoding="utf-8") as file:
  station_names = [line.split(";")[0] for line in file.readlines()]

# Gera os dados de teste em paralelo
start_time = time.time()
with Pool(num_workers) as pool:
  pool.starmap(generate_test_data, [(num_rows, chunk_size, station_names)])
end_time = time.time()

# Exibe o tempo real de geração
tempo_em_segundos = end_time - start_time
tempo_em_minutos = tempo_em_segundos / 60
print(f"Tempo real de geração:{tempo_em_minutos:.2f} Minutos")

# Exibe o tamanho real do arquivo
file_size = os.path.getsize("data/measurements.txt")

# Converte o tamanho do arquivo para megabytes
file_size_mb = file_size / (1024 * 1024)

# Exibe o tamanho do arquivo em megabytes
print(f"Tamanho real do arquivo: {file_size_mb:.2f} Megabytes")