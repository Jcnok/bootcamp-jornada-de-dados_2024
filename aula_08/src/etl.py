# Desafio ETL
import glob
import os
from typing import List

import pandas as pd
import pandera as pa

from utils.log_decorator import log_decorator
from utils.schema import VendasSchema

# importando os decorators
from utils.timer_decorator import timer


@pa.check_output(VendasSchema)
def ler_arquivos_json(path_origin: str) -> pd.DataFrame:
    caminho_arquivos = os.path.join(path_origin, "*.json")
    arquivos_json = glob.glob(caminho_arquivos)
    if not arquivos_json:
        raise ValueError("Nenhum arquivo JSON encontrado na pasta especificada.")
    dfs = [pd.read_json(arquivo) for arquivo in arquivos_json]
    return pd.concat(dfs, ignore_index=True)


def transformar_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df["Receita"] = df["Quantidade"] * df["Venda"]
    return df


def carregar_dataframe(
    df: pd.DataFrame, path_to_save: str, format_to_save: List[str]
) -> None:
    for formato in format_to_save:
        if formato.lower() == "csv":
            caminho_salvar_csv = path_to_save + ".csv"
            df.to_csv(caminho_salvar_csv, index=False)
            print(f"DataFrame salvo em '{caminho_salvar_csv}'")
        elif formato.lower() == "parquet":
            caminho_salvar_parquet = path_to_save + ".parquet"
            df.to_parquet(caminho_salvar_parquet, index=False)
            print(f"DataFrame salvo em '{caminho_salvar_parquet}'")
        else:
            raise ValueError(
                "Formato especificado não suportado. Use 'csv' ou 'parquet'."
            )


@log_decorator
@timer
def pipeline(path_origin: str, path_to_save: str, format_to_save: List[str]) -> None:
    df = ler_arquivos_json(path_origin)
    df = transformar_dataframe(df)
    carregar_dataframe(df, path_to_save, format_to_save)


if __name__ == "__main__":
    path_to_save = "data/process/dados_processados"
    path_origin = "data/"
    format_to_save = ["csv", "parquet"]  # ou 'parquet'

    pipeline(path_origin, path_to_save, format_to_save)
