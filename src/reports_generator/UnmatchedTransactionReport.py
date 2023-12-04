from Report import Report


class UnmatchedTransactionReport(Report):
    needed_columns = []
    KEY = 'אסמכתא1'
    input_text = 'Please enter תנועות לא מתואמות file path: (Example: C:\\Users\\USER\\Downloads\\UnmatchedTransactions.xlsx)\n>>'
    def __init__(self, df_to_create_from = None, file_path: str = None):
        super().__init__('UT',df_to_create_from=df_to_create_from, file_path=file_path)

