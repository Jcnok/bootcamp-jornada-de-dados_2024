# Class FilesSources
import os

# from AbstractDataSource import AbstractDataSource
from lib.classes.AbstractDataSource import AbstractDataSource


class FilesSources(AbstractDataSource):
    """
    A class to represent a data source for files.

    Attributes
    ----------
    previous_files : list
        A list to store the names of the previously processed files.
    folder_path : str
        The path to the folder containing the files.

    Methods
    -------
    create_path()
        Creates the folder path if it does not exist.
    check_for_new_files()
        Checks for new files in the folder.
    get_data()
        Placeholder method to get data from files.
    transform_data_to_df()
        Placeholder method to transform data to DataFrame.
    save_data()
        Placeholder method to save data.
    show_files()
        Prints the list of previously processed files.
    start()
        Initializes the data source.
    """

    def __init__(self):
        """Initialize the FilesSources class."""
        self.previous_files = []
        self.start()

    def create_path(self):
        """Create the folder path if it does not exist."""
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, "data", "extension_files")
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        """Check for new files in the folder."""
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previous_files]

        if new_files:
            print("New files detected:", new_files)
            # Update the list of previous files
            self.previous_files = current_files
        else:
            print("No new files detected.")

    def get_data(self):
        """Placeholder method to get data from files."""
        pass

    def transform_data_to_df(self):
        """Placeholder method to transform data to DataFrame."""
        pass

    def save_data(self):
        """Placeholder method to save data."""
        pass

    def show_files(self):
        """Print the list of previously processed files."""
        print(self.previous_files)

    def start(self):
        """Initialize the data source."""
        self.create_path()
