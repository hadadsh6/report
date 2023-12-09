from src.reports_generator import Resource, ReportsGenerator

elta_debts = Resource(
    r"C:\Users\USER\pythonProject\Order_status_report\src\reports_generator\resources\elta_debts_resource.json",
    file_path=r"C:\Users\USER\Documents\Elta_Reports\חובות אלתא.xlsx")
unmatched_transactions = Resource(
    r"C:\Users\USER\pythonProject\Order_status_report\src\reports_generator\resources\unmatched_transactions_resource.json",
    file_path=r"C:\Users\USER\Documents\Elta_Reports\תנועות לא מותאמות-28.xlsx")

reports_gen = ReportsGenerator(
    r"C:\Users\USER\pythonProject\Order_status_report\src\reports_generator\reports\elta_report.json",
    [unmatched_transactions, elta_debts])
reports_gen.create_report_excel()
x = 3
