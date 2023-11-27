from Report import Report
from config import *
class SiReport(Report):

    needed_columns = [INVOICE, ORDER, ROW_ON_ORDER, AMOUNT]
    def __init__(self, df_to_create_from = None, file_path: str = None):
        if df_to_create_from is None and file_path is None:
            file_path = input('Please enter invoices file path: (Example: C:\\Users\\USER\\Downloads\\invoices.xlsx)\n>>')
        super().__init__('SI',df_to_create_from=df_to_create_from, file_path=file_path)

    def get_order_info(self, order_num: str):
        if order_num not in list(self[ORDER]):
            print(f"Order number doesn't exist on {self.source} table")
        return SiReport(df_to_create_from=self[self[ORDER] == order_num], file_path=self.source)