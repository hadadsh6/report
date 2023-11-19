import pandas as pd
from Report import Report
from SiReport import SiReport
from config import *



class ShReport(Report):
    def __init__(self, df_to_create_from = None, file_path: str = None):
        super().__init__('SH',df_to_create_from=df_to_create_from, file_path=file_path)

    def get_order_info(self, order_num: str):
        if not order_num in self[ORDER]:
            print(f"Order number doesn't exist on {self.source} table")
        return ShReport(df_to_create_from=self[self[ORDER] == order_num], file_path=self.source)

    def create_ship_status_report(self, invoices: SiReport):
        raise NotImplementedError

    def get_unique_shipments(self, order_num: str):
        ships_of_order = self[self[ORDER] == order_num]
        return set(ships_of_order[SHIPMENT_CERTIFICATE])