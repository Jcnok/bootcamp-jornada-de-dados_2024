# Class TxtSource
import os

import pandas as pd
from lib.classes.FilesSources import FilesSources


class TxtSource(FilesSources):
    """
    A class to represent a TXT data source.

    Attributes:
    -----------
    folder_path : str
        The path to the folder containing TXT files.
    previous_files : list
        A list of previously detected TXT files in the folder.

    Methods:
    --------
    create_path():
        Create the folder path to store TXT files if it does not exist.
    check_for_new_files():
        Check for new TXT files in the folder and update the list of previous files.
    get_data():
        Retrieve data from TXT files in the specified folder.
    transform_data_to_df():
        Transform the retrieved data into a DataFrame.
    """

    def create_path(self):
        """
        Create the folder path to store TXT files if it does not exist.
        """
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, "data", "txt_files")
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        """
        Check for new TXT files in the folder and update the list of previous files.
        """
        current_files = os.listdir(self.folder_path)
        new_files = [
            file
            for file in current_files
            if file not in self.previous_files and file.endswith(".txt")
        ]

        if new_files:
            print("New TXT files detected:", new_files)
            # Update the list of previous files
            self.previous_files = current_files
        else:
            print("No new TXT files detected.")
            self.get_data()

    def get_data(self):
        """
        Retrieve data from TXT files in the specified folder.
        """
        # Implement getting data from TXT files in the specified folder
        data_frames = []
        for file_path in self.previous_files:
            try:
                path = os.path.join(self.folder_path, file_path)
                data = pd.read_csv(
                    path, sep="\t"
                )  # Assume that the TXT files are tab-separated
                data_frames.append(data)
            except Exception as e:
                print("An error occurred while reading the TXT file:", e)
        if data_frames:
            self.combined_data = pd.concat(data_frames, ignore_index=True)
            print(self.combined_data)
            return self.combined_data
        else:
            return None
