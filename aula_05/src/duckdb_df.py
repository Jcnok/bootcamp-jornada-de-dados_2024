# Duckdb => script para caluclar min, max e mean em um bilhão de linhas.
from utils.decorators import timer_to_csv
import duckdb
@timer_to_csv
def create_duckdb(): 
    conn = duckdb.connect(':memory:')    
    print(conn.execute("""
            SELECT city,
                MAX(temp) AS max_temp,
                MIN(temp) AS min_temp,
                CAST(AVG(temp) AS DECIMAL()) AS mean_temp                
            FROM read_csv("data/measurements.txt", AUTO_DETECT=FALSE, sep=';', columns={'city':VARCHAR, 'temp': 'DECIMAL'})
            GROUP BY city
            ORDER BY city
        """).df())
    
if __name__ == "__main__":
    create_duckdb()   
