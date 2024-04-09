from etl import pipeline

path_to_save = "data/process/dados_processados"
path_origin = "data/"
format_to_save = ["csv", "parquet"]  # ou 'parquet'

pipeline(path_origin, path_to_save, format_to_save)
