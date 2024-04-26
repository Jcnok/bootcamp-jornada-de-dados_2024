import os

import pandas as pd
from lib.classes.FilesSources import FilesSources


class TxtSource(FilesSources):
    """
    Classe para lidar com fontes de dados em formato TXT.

    Attributes:
    -----------
    folder_path : str
        O caminho para a pasta que contém os arquivos TXT.
    previous_files : list
        Uma lista dos arquivos TXT previamente detectados na pasta.
    """

    def create_path(self):
        """
        Cria o caminho da pasta para armazenar os arquivos TXT, se não existir.
        """
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, "data", "txt_files")
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        """
        Verifica se há novos arquivos TXT na pasta e atualiza a lista de arquivos anteriores.
        """
        current_files = os.listdir(self.folder_path)
        # Ignora os diretórios ao verificar os novos arquivos
        new_files = [
            file
            for file in current_files
            if file not in self.previous_files
            and file.endswith(".txt")
            and not os.path.isdir(os.path.join(self.folder_path, file))
        ]

        if new_files:
            print("Novos arquivos TXT detectados:", new_files)
            # Atualiza a lista de arquivos anteriores
            self.previous_files = current_files
        else:
            print("Nenhum novo arquivo TXT detectado.")
            self.get_data()

    def read_txt_file(self, file_path):
        """
        Lê um arquivo TXT e retorna os dados.

        Parameters:
        -----------
        file_path : str
            O caminho para o arquivo TXT.

        Returns:
        --------
        list or None
            Os dados do arquivo TXT ou None se ocorrer um erro ao acessar o arquivo.
        """
        try:
            with open(file_path, "r") as f:
                data = f.readlines()
            return data
        except Exception as e:
            print("Erro ao acessar o TXT:", e)
            return None

    def get_data(self):
        """
        Obtém os dados dos arquivos TXT na pasta especificada.

        Returns:
        --------
        pandas.DataFrame
            Um DataFrame contendo os dados de todos os arquivos TXT.
        """
        data_frames = []
        for file_path in self.previous_files:
            if file_path.endswith(".txt"):
                path = os.path.join(self.folder_path, file_path)
                # Verifica se o caminho é um arquivo antes de tentar ler
                if os.path.isfile(path):
                    txt_data = self.read_txt_file(path)
                    if txt_data is not None:
                        # Cria um DataFrame a partir dos dados do arquivo TXT
                        df = pd.DataFrame(txt_data, columns=["data"])
                        # Adiciona o DataFrame à lista de DataFrames
                        data_frames.append(df)
        if data_frames:
            # Concatena todos os DataFrames em um único DataFrame
            combined_df = pd.concat(data_frames, ignore_index=True)
            return combined_df
        else:
            return None
