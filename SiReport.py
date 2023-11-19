from Report import Report
from config import *
class SiReport(Report):
    def __init__(self, df_to_create_from = None, file_path: str = None):
        super().__init__('SI',df_to_create_from=df_to_create_from, file_path=file_path)

    def get_order_info(self, order_num: str):
        if order_num not in list(self[ORDER]):
            print(f"Order number doesn't exist on {self.source} table")
        return SiReport(df_to_create_from=self[self[ORDER] == order_num], file_path=self.source)