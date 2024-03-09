import time
import dask
dask.config.set({'dataframe.query-planning': True})
import dask.dataframe as dd
start_time = time.time()
# Ler o arquivo txt diretamente em um DataFrame Dask
df = dd.read_csv('data/measurements.txt', delimiter=';', header=None, names=['City', 'Temperature'])
# min, max, e mean pela cidade ordenado pelo index
print(df.groupby('City').
agg({'Temperature': ['max','min','mean']}).
compute().
sort_index())
end_time = time.time() - start_time
print(f"tempo de processamento com Dask:{end_time:.2f} segundos")