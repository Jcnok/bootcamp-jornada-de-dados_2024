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
    df = create_df_with_pandas(filename, total_linhas, chunksize)
    #print(tabulate(df, headers='keys', tablefmt='pretty'))
    print(df)      
    