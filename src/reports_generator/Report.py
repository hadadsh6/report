import pandas as pd
from pandas import DataFrame
from pathlib import Path
from src.reports_generator import config


class Report:
    needed_columns = []
    prompt = ''
    KEY = config.ORDER

    def __init__(self, report_type, df_to_create_from: DataFrame = None, file_path=None):

        if report_type not in config.SUPPORTED_REPORT_TYPES:
            raise f"{report_type} is not supported, try one of {config.SUPPORTED_REPORT_TYPES}"
        if file_path is None and df_to_create_from is None:
            file_path = input(self.prompt)
            file_path = file_path.strip('"')
            file_path = Path(file_path)
            if not file_path.exists():
                raise FileNotFoundError("couldn't find the specified path!")
            if file_path.suffix == '.csv':
                reader = pd.read_csv
            elif file_path.suffix in ['.xlsx','.xls']:
                reader = pd.read_excel
            else:
                raise IOError(f"{file_path.suffix} is not a valid file type")
            self.df = reader(file_path)
            self.source = file_path
            self.report_type = report_type
        elif df_to_create_from is not None:
            self.df = df_to_create_from
            self.source = file_path
            self.report_type = report_type
        elif file_path is not None:
            file_path = file_path.strip('"')
            file_path = Path(file_path)
            if file_path.suffix == '.csv':
                reader = pd.read_csv
            elif file_path.suffix == '.xlsx':
                reader = pd.read_excel
            elif file_path.suffix == '.xls':
                reader = pd.read_excel
            else:
                raise IOError(f"{file_path.suffix} is not a valid file type")
            self.df = reader(file_path)
            self.source = file_path
            self.report_type = report_type

        if not self.is_report_valid():
            raise IOError(f"The given report didn't include {self.needed_columns} columns")

    def iter_over_rows(self):
        for i in range(len(self.df)):
            yield self.df[i: i + 1]

    def is_report_valid(self):
        for col in self.needed_columns:
            if col not in self.df.columns:
                return False
        return True

    def get_order_info(self, key_str: str):
        if not key_str in list(self.df[config.ORDER]):
            print(f"Order number doesn't exist on {self.source} table")
        return self.__class__(df_to_create_from=self.df[self.df[config.ORDER] == key_str], file_path=self.source)
