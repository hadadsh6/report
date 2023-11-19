# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from config import *
from ShReport import ShReport
from SiReport import SiReport
from SoReport import SoReport
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    shipment_certificates = ShReport(file_path=pathes[0])
    invoices = SiReport(file_path=pathes[1])
    orders = SoReport(file_path=pathes[2])
    order = orders.get_order_info('SO20000218')
    order.create_summary_report('SO20000218', shipment_certificates, invoices)
    x=3


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
