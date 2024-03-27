from utils.decorators import timer_to_csv
import duckdb

def get_total_lines(num_rows_path):
    with open(num_rows_path, 'r') as f:
        total_lines = f.read()
    return int(total_lines)

@timer_to_csv
def create_duckdb(filename,num_rows_path):
    total_linhas = get_total_lines(num_rows_path)
    chunksize = total_linhas // 10 + (1 if total_linhas % 10 else 0)  # Define o tamanho do chunk
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
    filename = "data/measurements_pandas.txt" 
    num_rows_path= "data/num_rows.txt"
    create_duckdb(filename,num_rows_path)
  
