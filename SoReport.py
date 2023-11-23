from Report import Report
from config import *

class SoReport(Report):
    needed_columns = [ORDER, PART_NUMBER, PART_DESCRIPTION, PROJECT, PROJECT_DESCRIPTION, AMOUNT, PRICE]
    def __init__(self, df_to_create_from = None, file_path: str = None):
        if df_to_create_from is None and file_path is None:
            file_path = input('Please enter orders file path: \n(Example: C:\\Users\\USER\\Downloads\\orders.xlsx)')
        super().__init__('SO',df_to_create_from=df_to_create_from, file_path=file_path)

    def get_order_info(self, order_num: str):
        if not order_num in self[ORDER]:
            print(f"Order number doesn't exist on {self.source} table")
        return SoReport(df_to_create_from=self[self[ORDER] == order_num], file_path=self.source)