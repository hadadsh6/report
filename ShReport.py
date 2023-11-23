from Report import Report
from config import *

class ShReport(Report):
    needed_columns = [SHIPMENT_CERTIFICATE, ORDER, ROW_NUMBER, AMOUNT]
    def __init__(self, df_to_create_from = None, file_path: str = None):
        if df_to_create_from is None and file_path is None:
            file_path = input('Please enter shipment certificates (תעודות משלוח) file path: \n(Example: C:\\Users\\USER\\shipment_certificates.xlsx)')
        super().__init__('SH',df_to_create_from=df_to_create_from, file_path=file_path)

    def get_order_info(self, order_num: str):
        if not order_num in self[ORDER]:
            print(f"Order number doesn't exist on {self.source} table")
        return ShReport(df_to_create_from=self[self[ORDER] == order_num], file_path=self.source)

