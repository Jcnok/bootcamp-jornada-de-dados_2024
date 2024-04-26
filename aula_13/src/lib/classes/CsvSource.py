import os

import pandas as pd
from lib.classes.FilesSources import FilesSources


class CsvSource(FilesSources):
    """
    Classe para lidar com fontes de dados em formato CSV.

    Attributes:
    -----------
    folder_path : str
        O caminho para a pasta que contém os arquivos CSV.
    previous_files : list
        Uma lista dos arquivos CSV previamente detectados na pasta.
    """

    def create_path(self):
        """
        Cria o caminho da pasta para armazenar os arquivos CSV, se não existir.
        """
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, "data", "csv_files")
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        """
        Verifica se há novos arquivos CSV na pasta e atualiza a lista de arquivos anteriores.
        """
        current_files = os.listdir(self.folder_path)
        # Ignora os diretórios ao verificar os novos arquivos
        new_files = [
            file
            for file in current_files
            if file not in self.previous_files
            and file.endswith(".csv")
            and not os.path.isdir(os.path.join(self.folder_path, file))
        ]

        if new_files:
            print("Novos arquivos CSV detectados:", new_files)
            # Atualiza a lista de arquivos anteriores
            self.previous_files = current_files
        else:
            print("Nenhum novo arquivo CSV detectado.")
            self.get_data()

    def read_csv_file(self, file_path):
        """
        Lê um arquivo CSV e retorna os dados.

        Parameters:
        -----------
        file_path : str
            O caminho para o arquivo CSV.

        Returns:
        --------
        pandas.DataFrame or None
            Os dados do arquivo CSV ou None se ocorrer um erro ao acessar o arquivo.
        """
        try:
            data = pd.read_csv(file_path)
            return data
        except Exception as e:
            print("Erro ao acessar o CSV:", e)
            return None

    def get_data(self):
        """
        Obtém os dados dos arquivos CSV na pasta especificada.

        Returns:
        --------
        pandas.DataFrame
            Um DataFrame contendo os dados de todos os arquivos CSV.
        """
        data_frames = []
        for file_path in self.previous_files:
            if file_path.endswith(".csv"):
                path = os.path.join(self.folder_path, file_path)
                # Verifica se o caminho é um arquivo antes de tentar ler
                if os.path.isfile(path):
                    csv_data = self.read_csv_file(path)
                    if csv_data is not None:
                        data_frames.append(csv_data)
        if data_frames:
            combined_data = pd.concat(data_frames, ignore_index=True)
            print(combined_data)
            return combined_data
        else:
            return None
