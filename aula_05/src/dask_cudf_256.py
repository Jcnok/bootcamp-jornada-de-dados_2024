# dask_cudf com blocksize 256mb => script para caluclar min, max e mean em um bilhão de linhas usando a gpu rtx 3060ti.
from dask.distributed import Client
from dask_cuda import LocalCUDACluster
from utils.decorators import timer_to_csv
import dask_cudf as dc

@timer_to_csv
def dask_cudf_256(filename):
    # Definindo o cluster para usar gpu
    with LocalCUDACluster() as cluster, Client(cluster) as client:
        # Carregar o arquivo csv em um dataframe dask_cudf
        df = dc.read_csv(filename,
                         sep=';', header=None,
                         names=['city', 'temp'], 
                         dtype={'city': 'str', 'temp': 'float32'},
                         blocksize='256 MiB')
        
        # Agrupar pela coluna 'city' e calcular min, max e mean da coluna 'temp'
        result = df.groupby('city').agg({'temp': ['max','min','mean']}).compute().sort_index()
        print(result)
if __name__ == "__main__":
    filename= 'data/measurements_pandas.txt'
    dask_cudf_256(filename)
