from Report import Report
from config import *

class SoReport(Report):
    needed_columns = [ORDER, PART_NUMBER, PART_DESCRIPTION, PROJECT, PROJECT_DESCRIPTION, AMOUNT, PRICE]
    input_text = 'Please enter orders file path: (Example: C:\\Users\\USER\\Downloads\\orders.xlsx)\n>>'
    def __init__(self, df_to_create_from = None, file_path: str = None):
        super().__init__('SO',df_to_create_from=df_to_create_from, file_path=file_path)

