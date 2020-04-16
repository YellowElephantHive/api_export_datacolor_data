from abc import ABC, abstractmethod

from pandas import DataFrame


class BaseDatabaseExporter(ABC):
    @abstractmethod
    def isConnect(self):
        pass

    @abstractmethod
    def query(self):
        pass

    @abstractmethod
    def commit(self):
        pass

    @staticmethod
    def export(
            df: DataFrame,
            file_name: str,
            file_path: str,
            file_type: str
    ):

        if file_type == 'csv':
            df.to_csv(file_path, file_name)

        elif file_type == 'excel':
            df.to_excel(file_path, file_name)

        else:
            print('Data types are not supported')
