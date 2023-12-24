# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from pathlib import Path
from os import listdir, path
import tkinter
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import Tk, Label, Button, Text
# import filedialog module
from tkinter import filedialog
from tkinter import Tk, Listbox, Button, Scrollbar
import json
from src.reports_generator import ReportsGenerator, Resource

report_gen_folder = Path(path.dirname(__file__))
resources = {}
report_base_folder = []



def reload_folder(path_text):

    def browseFiles(title: str = "choose a file"):
        new_path = askdirectory(initialdir="/",
                                   title=title)
        path_text.delete("1.0", "end")
        path_text.insert(tkinter.END, Path(new_path).name)
        report_base_folder.append(Path(new_path))
    return browseFiles
def reload_file(resource_json, path_text):

    def browseFiles(title: str = "choose a file"):
        new_path = askopenfilename(initialdir="/",
                                   title=title,
                                   filetypes=(("Text files",
                                               "*.xlsx*"),
                                              ("all files",
                                               "*.*")))
        resources[resource_json] = new_path
        path_text.delete("1.0", "end")

        path_text.insert(tkinter.END, Path(new_path).name)
    return browseFiles



def create_report(report_type: str):
    n_rows = 0
    report_json_path = report_gen_folder.joinpath("reports", report_type + ".json")
    with report_json_path.open('r', encoding='utf-8') as f:
        report_json = json.loads(f.read())
    window = Tk()
    # Set window title

    window.title(report_type)

    # Set window size
    window.geometry("500x500")

    # Set window background color
    window.config(background="grey")
    headers = ["סוג הקובץ:", "שם הקובץ:"]
    for i, header in enumerate(headers):
        header_label = Label(window, text=header)
        header_label.grid(column=i+1, row=0)

    for resource_json, resource_excel_path in report_json["Resources"].items():
        resources[resource_json] = resource_excel_path
        row_text = Label(window, text=f"{resource_json}:")
        path_text = Text(window, height=1, width=20)
        reload_button = Button(window, text="טען מחדש", command=reload_file(resource_json, path_text))

        path_text.insert(tkinter.END, Path(resource_excel_path).name)
        n_rows += 1
        row_text.grid(column=1, row=n_rows)
        path_text.grid(column=2, row=n_rows)
        reload_button.grid(column=3, row=n_rows)

    row_text = Label(window, text="איפה ליצור את הדו\"ח?")
    path_text = Text(window, height=1, width=20)
    reload_button = Button(window, text="בחר מיקום", command=reload_folder(path_text))

    path_text.insert(tkinter.END, "לא מוגדר")
    n_rows += 1
    row_text.grid(column=1, row=n_rows)
    path_text.grid(column=2, row=n_rows)
    reload_button.grid(column=3, row=n_rows)


    button_exit = Button(window,
                         text="Exit",
                         command=exit)
    button_run = Button(window,
                         text="צור דו\"ח",
                         command=run_generator(report_type, window))

    button_exit.grid(column=1, row=n_rows + 1)
    button_run.grid(column=2, row=n_rows + 1)
    window.mainloop()
def choose_report_type_wrapper(window):
    def choose_report_type():
        report_type = report_type_selector.get('active')
        window.destroy()
        create_report(report_type)

    return choose_report_type

def run_generator(report_type, window):
    def run_report_generator():
        window.destroy()
        reports_gen = ReportsGenerator(
            report_json_path=report_gen_folder.joinpath("reports", f"{report_type}.json"),
            resources=[Resource(resource_path=report_gen_folder.joinpath("resources", f"{resource_type}.json"),
                                file_path=resource_path) for resource_type, resource_path in resources.items()])
        reports_gen.create_report_excel(report_base_folder[0])

    return run_report_generator



def create_dialog():
    global report_type_selector
    # Create the root window
    window = Tk()

    # Set window title
    window.title('מחולל הדוחות')

    # Set window size
    window.geometry("500x500")

    # Set window background color
    window.config(background="grey")

    scroll = Scrollbar(window)

    report_type_selector = Listbox(window, yscrollcommand=scroll.set)

    report_type_selector.grid(column=1, row=1)
    for line in listdir(report_gen_folder.joinpath("reports")):
        report_type_selector.insert('end', line[:-5])
    scroll.config(command=report_type_selector.yview)

    selectbutton = Button(window, text="Choose report type:", command=choose_report_type_wrapper(window))
    selectbutton.grid(column=1, row=0)

    button_exit = Button(window,
                         text="Exit",
                         command=exit)

    button_exit.grid(column=1, row=2)

    window.mainloop()


create_dialog()
