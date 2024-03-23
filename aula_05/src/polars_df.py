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
   
