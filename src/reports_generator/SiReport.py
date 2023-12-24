from src.reports_generator import Report, config

class SiReport(Report):

    needed_columns = [config.INVOICE, config.ORDER, config.ROW_ON_ORDER, config.AMOUNT]
    input_text = 'Please enter invoices.json file path: (Example: C:\\Users\\USER\\Downloads\\invoices.json.xlsx)\n>>'
    def __init__(self, df_to_create_from = None, file_path: str = None):
        super().__init__('SI',df_to_create_from=df_to_create_from, file_path=file_path)

