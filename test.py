import os
# use the tkinter filedialog to choose the dir to work on
import tkinter as tk
from tkinter import filedialog


root=tk.Tk()
root.withdraw()
file_path=filedialog.askdirectory()
with open("file_list.log","a") as flist:
    with os.scandir(file_path) as entries:
        for entry in entries:
            print(entry.name)
            flist.write(entry.name)
            flist.write("\n")
    flist.close()
