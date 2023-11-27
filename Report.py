import pandas as pd
from pandas import DataFrame
from pathlib import Path
from config import *
class Report(DataFrame):
    needed_columns = []

    def __init__(self, report_type,df_to_create_from: DataFrame = None, file_path = None):

        if report_type not in SUPPORTED_REPORT_TYPES:
            raise f"{report_type} is not supported, try one of {SUPPORTED_REPORT_TYPES}"
        if df_to_create_from is not None:
            super().__init__(df_to_create_from)
            self.source = file_path
            self.report_type = report_type
        elif file_path is not None:
            file_path = file_path.strip('"')
            file_path = Path(file_path)
            if not file_path.exists():
                raise FileNotFoundError("couldn't find the specified path!")
            super().__init__(pd.read_excel(file_path))
            self.source = file_path
            self.report_type = report_type
        else:
            raise "please specify source to create report from!"
        if not self.is_report_valid():
            raise IOError(f"The given report didn't include {self.needed_columns} columns")

    def iter_over_rows(self):
        for i in range(len(self)):
            yield self[i: i+1]


    def is_report_valid(self):
        for col in self.needed_columns:
            if col not in self.columns:
                return False
        return True

