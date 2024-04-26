# script para utilizar classes abstratas.
from abc import ABC, abstractmethod


class AbstractDataSource(ABC):
    """Abstract class for defining data source operations."""

    @abstractmethod
    def start(self):
        """Method to start the data source."""
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_data(self):
        """Method to retrieve data from the source."""
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def transform_data_to_df(self):
        """Method to transform data to a DataFrame."""
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def save_data(self):
        """Method to save data."""
        raise NotImplementedError("Method not implemented")

    def hello_world(self):
        """Simple method to print 'Hello World'."""
        print("Hello World")
