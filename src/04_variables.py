"""
 TKINTER VARIABLES
========================

Tkinter has built in variable that are desinged to work with widgets.
They are automatically updated by a widget and they update a widget.
But they are basic data types are like, string, int and bool

They are used to get data and connect different windgets to each other
The connection is done using argument 'textvariable'

 * 'StringVar' stores strings it automatically gets the value
   Arguments
    - 'value'
 * 'IntVar'
 * 'DoubleVar'
 * 'BooleanVar'

The different variables have methods that can be used
 - 'get': get the value
 - 'set': set the value
"""

import tkinter as tk
from tkinter import ttk

def button_func():
    
    print(string_var.get())
    string_var.set(string_var.get()[::-1]) # reverse (hello -> olleh)


window = tk.Tk()
window.title("Tkinter variables")
window.geometry("200x200")

# Tkinter variable
string_var = tk.StringVar(value="start value") # with a default value

# Widget
label = ttk.Label(window, text="label", textvariable=string_var)
entry = ttk.Entry(window, textvariable=string_var)
entry2 = ttk.Entry(window, textvariable=string_var)
button = ttk.Button(window, text="Submit", command=button_func)

label.pack()
entry.pack()
entry2.pack()
button.pack()

# Exercise

str_var = tk.StringVar(value="test")

entry3 = ttk.Entry(window, textvariable=str_var)
entry4 = ttk.Entry(window, textvariable=str_var)
label2 = ttk.Label(window, textvariable=str_var)

label2.pack()
entry3.pack()
entry4.pack()

window.mainloop()
