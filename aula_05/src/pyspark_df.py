# Pyspark => script para caluclar min, max e mean em um bilhão de linhas.
from utils.decorators import timer_to_csv
from pyspark.sql import SparkSession
from config import PATH
from pyspark.sql.functions import col, min as spark_min, max as spark_max, avg as spark_avg, round as spark_round

@timer_to_csv
def pyspark_df(filename):     
    # Inicializar uma sessão Spark
    spark = SparkSession.builder \
        .appName("Temperature Analysis") \
        .getOrCreate()
    
    # Ler o arquivo CSV diretamente em um DataFrame Spark
    df = spark.read.option("header", "false").option("delimiter", ";").csv(filename) \
        .toDF("City", "Temperature")
    
    # Converter a coluna 'Temperature' para tipo numérico
    df = df.withColumn("Temperature", col("Temperature").cast("float"))
    
    # Calcular estatísticas usando Spark SQL
    statistics = df.groupBy("City") \
        .agg(spark_max("Temperature").alias("Max Temperature"),
             spark_min("Temperature").alias("Min Temperature"),             
             spark_round(spark_avg("Temperature"),2).alias("Avg Temperature"))
    
    # Ordenar as estatísticas pela cidade
    statistics_sorted = statistics.orderBy("City")
    
    # Mostrar as estatísticas
    return statistics_sorted.show()
    
    # Encerrar a sessão Spark
    spark.stop()

if __name__ == "__main__":
    filename = PATH
    pyspark_df(filename)  
