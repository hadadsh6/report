from Report import Report
from ShReport import ShReport
from SiReport import SiReport
from config import *


class SoReport(Report):
    def __init__(self, df_to_create_from = None, file_path: str = None):
        super().__init__('SO',df_to_create_from=df_to_create_from, file_path=file_path)

    def get_order_info(self, order_num: str):
        if not order_num in self[ORDER]:
            print(f"Order number doesn't exist on {self.source} table")
        return SoReport(df_to_create_from=self[self[ORDER] == order_num], file_path=self.source)

    def create_summary_report(self, order_number, shipments: ShReport, invoices: SiReport):
        order = self.get_order_info(order_number)
        shipments_of_order = shipments.get_order_info(order_number)
        invoices_of_order = invoices.get_order_info(order_number)
        for row_i, row in enumerate(order.iter_over_rows()):
            shipments_of_row = shipments_of_order[shipments_of_order[ROW_NUMBER] == row_i + 1]
            invoices_of_row = invoices_of_order[invoices_of_order[ROW_ON_ORDER] == row_i + 1]

            print(f"ORDER: {order_number} row: {row_i + 1} מקט: {row[PART_NUMBER].array[0]} sent: {shipments_of_row[AMOUNT].sum()}"
                  f" billed: {invoices_of_row[AMOUNT].sum()}")