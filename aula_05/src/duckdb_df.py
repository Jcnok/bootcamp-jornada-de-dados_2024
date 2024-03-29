# Duckdb => script para caluclar min, max e mean.
from utils.decorators import timer_to_csv
from utils.config import PATH
import duckdb

@timer_to_csv
def duckdb_df(filename):
    conn = duckdb.connect(':memory:')
    query = f"""
            SELECT city,
                MAX(temp) AS max_temp,
                MIN(temp) AS min_temp,
                CAST(AVG(temp) AS DECIMAL()) AS mean_temp                
            FROM read_csv("{filename}", AUTO_DETECT=FALSE, sep=';', columns={{'city':VARCHAR, 'temp': 'DECIMAL'}})
            GROUP BY city
            ORDER BY city
        """
    print(conn.execute(query).df())

if __name__ == "__main__":
    filename = PATH 
    duckdb_df(filename) 
