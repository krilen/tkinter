"""
 COMBOBOX and SPINBOX WIDGETS
========================
Combobox is a dropdown
Spinbox is a selection / menu where you scroll predefined value (numbers or strings)

Both need a list of values and they both can be connected to a Tkinter variable

With Combobox there is an unique event that can be used everytime a selection is made

A spinbox works simulare like a combobox.

@7:52s

"""

import tkinter as tk
from tkinter import ttk

# Setup
window = tk.Tk()
window.title("Combo and Spin")
window.geometry("600x500")

# Combobox
items1 = ["dog", "cat", "bird", "horse"]
animal_var = tk.StringVar()
combo1 = ttk.Combobox(window, textvariable=animal_var)
combo1["values"] = items1           # One way of defining the values
combo1.pack()

items2 = ["car", "bike", "truck"]
veichle_var = tk.StringVar(value=items2[0]) # set a default value in the list
combo2 = ttk.Combobox(window, textvariable=veichle_var)
combo2.configure(values = items2)   # The other way of defining the values
combo2.pack()

# Events for combobox, it has one special event that is unique to it
combo2.bind("<<ComboboxSelected>>", lambda event: print(veichle_var.get()))

combo2_label = ttk.Label(window, textvariable=veichle_var) # One way of setting the label
combo2_label.pack()

combo1.bind("<<ComboboxSelected>>", lambda event: print(combo1_label.configure(text=animal_var.get())))

combo1_label = ttk.Label(window, text="Animal")             # Other way using lambda
combo1_label.pack()

# Spinbox


window.mainloop()