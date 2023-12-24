from src.reports_generator import ReportsGenerator

reports_gen = ReportsGenerator(
    r"C:\Users\USER\pythonProject\Order_status_report\src\reports_generator\reports\billing_status.json")
reports_gen.create_report_excel()
