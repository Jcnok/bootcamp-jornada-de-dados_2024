# Polars => script para caluclar min, max e mean em um bilhão de linhas.
from utils.decorators import timer_to_csv
import polars as pl

def get_total_lines(num_rows_path):
    with open(num_rows_path, 'r') as f:
        total_lines = f.read()
    return int(total_lines)

@timer_to_csv
def polars_df(filename, num_rows_path):
    total_linhas = get_total_lines(num_rows_path)
    chunksize = total_linhas // 10 + (1 if total_linhas % 10 else 0)  # Define o tamanho do chunk

    pl.Config.set_streaming_chunk_size(chunksize)

    # Leitura do arquivo CSV e definição do schema
    return (pl.scan_csv(filename, separator=";", has_header=False,
                        schema={"city": pl.String, "temp": pl.Float64})
                        .group_by("city").agg(
                                                 max_temp=pl.col("temp").max(),
                                                 min_temp=pl.col("temp").min(),
                                                 mean_temp=pl.col("temp").mean()
                                                ).sort("city").collect(streaming=True)
           )

if __name__ == "__main__":  
    num_rows_path= "data/num_rows.txt"
    filename = "data/measurements_pandas.txt" 
    df = polars_df(filename, num_rows_path)
    print(df)

   
