# Dask => script para caluclar min, max e mean em um bilhão de linhas.
from utils.decorators import timer_to_csv
import dask
dask.config.set({'dataframe.query-planning': True})
import dask.dataframe as dd
@timer_to_csv
def dask_df(filename):    
    # Ler o arquivo txt diretamente em um DataFrame Dask
    df = dd.read_csv(filename, delimiter=';', 
                     header=None, names=['city', 'temp'])
    # min, max, e mean pela cidade ordenado pelo index
    return print(df.groupby('city').
                   agg({'temp': ['max','min','mean']}).
                   compute().round(2).sort_index())

if __name__ == "__main__":
    filename = "data/measurements_pandas.txt"
    dask_df(filename)
