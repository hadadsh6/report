from config import *
from pathlib import Path
import time
import pandas as pd
from pandas import DataFrame
from SoReport import SoReport
from ShReport import ShReport
from SiReport import SiReport

from typing import Tuple
class SummaryDict(dict):
    def __init__(self):
        """
        Initializes the summary dictionary
        """
        super().__init__()
        for key in SUMMARY_DICT_FIELDS_BY_ORDER:
            self.setdefault(key, [])
        self.order = None
    def append_row(self, row_i: int, row: DataFrame, shipments_of_row: DataFrame, invoices_of_row: DataFrame) -> None:
        """
        append the information of to the dictionary
        :param row_i:
        :param row:
        :param shipments_of_row:
        :param invoices_of_row:
        :return:
        """
        self[ORDER].append(row[ORDER].array[0])
        self[ROW_ON_ORDER].append(row_i + 1)
        self[AMOUNT].append(row[AMOUNT].sum())
        self[PART_NUMBER].append(row[PART_NUMBER].array[0])
        self[PART_DESCRIPTION].append(row[PART_DESCRIPTION].array[0])
        self[PROJECT].append(row[PROJECT].array[0])
        self[PROJECT_DESCRIPTION].append(row[PROJECT_DESCRIPTION].array[0])
        self[PRICE].append(row[PRICE].array[0])
        self[SHIPMENT_CERTIFICATE].append(list(shipments_of_row[SHIPMENT_CERTIFICATE]))
        self[SENT].append(shipments_of_row[AMOUNT].sum())
        self[INVOICES].append(list(invoices_of_row[INVOICE]))
        self[BILLED].append(invoices_of_row[AMOUNT].sum())
        self[AMOUNT_LEFT_ON_ORDER].append(max(0, row[AMOUNT].sum() - invoices_of_row[AMOUNT].sum()))
        self[AMOUNT_LEFT_ON_ORDER_PRICE].append(
            max(0, row[AMOUNT].sum() - invoices_of_row[AMOUNT].sum()) * row[PRICE].array[0])
        self[SENT_BUT_NOT_BILLED].append(
            max(0, shipments_of_row[AMOUNT].sum() - invoices_of_row[AMOUNT].sum()))
        self[SENT_BUT_NOT_BILLED_PRICE].append(
            max(0, shipments_of_row[AMOUNT].sum() - invoices_of_row[AMOUNT].sum()) * row[PRICE].array[0])

    def get_orders_dataframes(self, orders: SoReport, shipments: ShReport, invoices: SiReport) ->\
            Tuple[SoReport, ShReport, SiReport]:
        """

        :param orders:
        :param shipments:
        :param invoices:
        :return:
        """
        self.order = input("Please enter an order number: \n(Example: SO20000218)")
        if self.order not in list(orders[ORDER]):
            raise IOError(f"Order {self.order} isn't on your orders excel")
        order = orders.get_order_info(self.order)
        shipments_of_order = shipments.get_order_info(self.order)
        invoices_of_order = invoices.get_order_info(self.order)
        return order, shipments_of_order, invoices_of_order
    def create_summary_report(self) -> None:
        """

        """
        orders = SoReport()
        shipments = ShReport()
        invoices = SiReport()
        order, shipments_of_order, invoices_of_order = self.get_orders_dataframes(orders, shipments, invoices)
        for row_i, row in enumerate(order.iter_over_rows()):
            shipments_of_row = shipments_of_order[shipments_of_order[ROW_NUMBER] == row_i + 1]
            invoices_of_row = invoices_of_order[invoices_of_order[ROW_ON_ORDER] == row_i + 1]
            self.append_row(row_i, row, shipments_of_row, invoices_of_row)
        self.create_excel_of_summary_dict()
    def create_excel_of_summary_dict(self) -> None:
        """

        :return:
        """
        order_df = pd.DataFrame(self)
        order_df.to_excel(SummaryDict.get_path_to_put_results_in())

    @staticmethod
    def get_path_to_put_results_in() -> None:
        folder_path = input(
            "Please enter path to put summary excel on:\n (Example: C:\\Users\\USER\\Documents)")
        folder_path = Path(folder_path)
        if not folder_path.exists():
            raise IOError("Folder doesn't exist!")
        if not folder_path.is_dir():
            raise IOError("Path isn't a folder!!")
        return folder_path.joinpath(Path(f"summary{time.asctime().replace(':', '_').replace(' ', '_')}.xlsx"))
