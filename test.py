import os
# use the tkinter filedialog to choose the dir to work on
import tkinter as tk
from tkinter import filedialog


root=tk.Tk()
root.withdraw()
file_path=filedialog.askdirectory()
new_file="ahmad.txt"
make_it=os.path.join(file_path,new_file)
print(file_path)
with open(make_it,"w") as f:
    f.write("Hello World!")
    f.close()

