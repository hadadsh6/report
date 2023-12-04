# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import Tk, Label, Button, Text
# import filedialog module
from tkinter import filedialog


# Function for opening the
# file explorer window
def browseFiles(title: str="choose a file"):
    filename = askopenfilename(initialdir="/",
                                          title=title,
                                          filetypes=(("Text files",
                                                      "*.xlsx*"),
                                                     ("all files",
                                                      "*.*")))
    return filename




def create_dialog(text_to_show):
    # Create the root window
    window = Tk()

    # Set window title
    window.title('מחולל הדוחות')

    # Set window size
    window.geometry("500x500")

    # Set window background color
    window.config(background="grey")

    # Create a File Explorer label
    label_file_explorer = Label(window,
                                text=file_name_var,
                                width=100, height=4,
                                fg="blue", background="grey")



    button_explore = Button(window,
                            text="Browse Files",
                            command=browseFiles)

    button_exit = Button(window,
                         text="Exit",
                         command=exit)

    # Grid method is chosen for placing
    # the widgets at respective positions
    # in a table like structure by
    # specifying rows and columns
    label_file_explorer.grid(column=1, row=1)
    label_file_explorer.grid(column=1, row=2)
    label_file_explorer.grid(column=1, row=3)


    button_explore.grid(column=1, row=2)

    button_exit.grid(column=1, row=3)

    # Let the window wait for any events
    window.mainloop()