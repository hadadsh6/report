# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd

def read_invoice_excel(file_path: str ):
    invoice = pd.read_excel(r"C:\Users\USER\Downloads\שורות חשבוניות מכירה.xlsx")
    return invoice

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    invoices = read_invoice_excel('')
    x=3

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
