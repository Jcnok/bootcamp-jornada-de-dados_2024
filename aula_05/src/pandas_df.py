#pandas => script para caluclar min, max e mean em um bilhão de linhas.
import pandas as pd 
from multiprocessing import Pool, cpu_count
from config import PATH, NUM_ROWS
from utils.decorators import timer_to_csv  

CONCURRENCY = cpu_count()

def get_total_lines(num_rows_path):
    with open(num_rows_path, 'r') as f:
        total_lines = f.read()
    return int(total_lines)

def process_chunk(chunk):
    # Agrega os dados dentro do chunk usando Pandas
    aggregated = chunk.groupby('city')['temp'].agg(['max','min','mean']).reset_index()
    return aggregated

@timer_to_csv  # Aplica o decorador
def create_df_with_pandas(filename, num_rows_path):
    total_linhas = get_total_lines(num_rows_path)
    chunksize = total_linhas // 200 + (1 if total_linhas % 10 else 0)  # Define o tamanho do chunk
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
    num_rows_path= NUM_ROWS
    filename = PATH     
    df = create_df_with_pandas(filename, num_rows_path)
    #print(tabulate(df, headers='keys', tablefmt='pretty'))
    print(df)
 
    