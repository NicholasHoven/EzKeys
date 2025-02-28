#Nicholas Hoven 2025
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from key_manager import *
from pathlib import Path

root = tk.Tk()
data_path = str(Path(__file__).parent).replace("\\src", "//data//main_path.txt") #This is the folder the program exists in.


def clear_menu(): #this will completely clear the GUI menu
    for widget in root.winfo_children():
        widget.destroy()


def import_key_folder():
    folder_path = filedialog.askdirectory(title="Select Key Folder")
    if folder_path != "":
        data_path = Path(__file__).parent
        data_path = str(data_path).replace("\\src", "//data//main_path.txt")
        with open(data_path, 'w') as file:
            file.write(folder_path)
        global imported_directory_path
        imported_directory_path = folder_path
        display_main_menu(folder_path)
        return folder_path
    

def display_main_menu(data_path):
    clear_menu()
    root.title("EzKey Key Management")
    root.geometry("345x200")
    label = tk.Label(root, text="Select Key:")
    label.place(x = 70)
    combobox = ttk.Combobox(root, values = list_files(data_path))
    combobox.place(x = 135)
    copy_button = tk.Button(root, text = "Copy", command=lambda: copy_key(data_path, str(combobox.get()) + ".txt"))
    copy_button.place(x = 300)
    import_button = tk.Button(root, text = "Import", command=lambda: import_key_folder())
    import_button.place(x=5)


def run_gui():
    display_main_menu(get_file_contents(data_path))
    root.mainloop()