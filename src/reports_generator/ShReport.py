from src.reports_generator import config, Report


class ShReport(Report):

    needed_columns = [config.SHIPMENT_CERTIFICATE, config.ORDER, config.ROW_NUMBER, config.AMOUNT]
    input_text = 'Please enter shipment certificates (תעודות משלוח) file path: (Example: C:\\Users\\USER\\shipment_certificates.xlsx)\n>>'
    def __init__(self, df_to_create_from = None, file_path: str = None):
        super().__init__('SH',df_to_create_from=df_to_create_from, file_path=file_path)


