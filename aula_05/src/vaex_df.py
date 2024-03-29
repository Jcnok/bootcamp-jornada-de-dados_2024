# Vaex => script para caluclar min, max e mean.
from utils.decorators import timer_to_csv
from utils.config import PATH
import vaex
@timer_to_csv
def vaex_df(filename):
    # Leitura do arquivo CSV utilizando Vaex
    df = vaex.from_csv(filename, sep=';', header=None, names=['city', 'temp'])

    # Cálculo das estatísticas
    combined_results = df.groupby(df['city']).agg({'temp': ['max', 'min', 'mean']})

    # Ordenar por 'city'
    combined_results = combined_results.sort(by='city')
    
    # Exibição dos resultados
    return print(combined_results)
   
if __name__ == "__main__":
    filename = PATH
    vaex_df(filename)
