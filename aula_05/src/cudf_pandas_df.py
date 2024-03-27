# Script usando cudf == pandas mas rápido pq usa a GPU, porém a mem não suport procesar 1bilhão.
import cudf
from utils.decorators import timer_to_csv
@timer_to_csv
def cudf_pandas(filename):
    
    # Carregar o arquivo CSV e criar os cabeçalhos 'city' e 'temp'
    df = cudf.read_csv(filename, header=None, sep=';', names=['city', 'temp'])
    
    # Agrupar por 'city' e calcular o 'min', 'max' e 'mean' da coluna 'temp'
    grouped_df = df.groupby('city').agg({'temp': ['min', 'max', 'mean']})
    
    # Ordenar o DataFrame pelo índice (city)
    result = grouped_df.sort_index()     
    
    # retorna o resultado
    return print(result)

if __name__ == "__main__":
    filename = "data/measurements_pandas.txt"
    cudf_pandas(filename)
