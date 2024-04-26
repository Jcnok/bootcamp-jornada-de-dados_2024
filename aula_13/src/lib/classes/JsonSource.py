import os

import pandas as pd
from lib.classes.FilesSources import FilesSources


class JsonSource(FilesSources):
    """
    Classe para lidar com fontes de dados em formato JSON.

    Attributes:
    -----------
    folder_path : str
        O caminho para a pasta que contém os arquivos JSON.
    previous_files : list
        Uma lista dos arquivos JSON previamente detectados na pasta.
    """

    def create_path(self):
        """
        Cria o caminho da pasta para armazenar os arquivos JSON, se não existir.
        """
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, "data", "json_files")
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        """
        Verifica se há novos arquivos JSON na pasta e atualiza a lista de arquivos anteriores.
        """
        current_files = os.listdir(self.folder_path)
        new_files = [
            file
            for file in current_files
            if file not in self.previous_files and file.endswith(".json")
        ]

        if new_files:
            print("Novos arquivos JSON detectados:", new_files)
            # Atualiza a lista de arquivos anteriores
            self.previous_files = current_files
        else:
            print("Nenhum novo arquivo JSON detectado.")
            self.get_data()

    def read_json_file(self, file_path):
        """
        Lê um arquivo JSON e retorna os dados.

        Parameters:
        -----------
        file_path : str
            O caminho para o arquivo JSON.

        Returns:
        --------
        dict or None
            Os dados do arquivo JSON ou None se ocorrer um erro ao acessar o arquivo.
        """
        try:
            with open(file_path, "r") as f:
                data = pd.read_json(f)
            return data
        except Exception as e:
            print("Erro ao acessar o JSON:", e)
            return None

    def get_data(self):
        """
        Obtém os dados dos arquivos JSON na pasta especificada.

        Returns:
        --------
        pandas.DataFrame
            Um DataFrame contendo os dados de todos os arquivos JSON.
        """
        data_frames = []
        for file_path in self.previous_files:
            if file_path.endswith(".json"):
                path = os.path.join(self.folder_path, file_path)
                json_data = self.read_json_file(path)
                if json_data is not None:
                    data_frames.append(json_data)
        if data_frames:
            combined_data = pd.concat(data_frames, ignore_index=True)
            print(combined_data)
            return combined_data
        else:
            return None
