"""
 DATA
========================
Two ways to get data from a widget
 * Tkinter variables this should be used.
 * get method

The get method is the easiest mothod to get data but many widgets do 
not have a get method. Label is such a widget an error would occur.

Every widget in tkinter have a config method that can update the widget
ex: <widget>.configure(text="<new_text>")
    <widget>["text"] = "<new_text>"
    
Both method gives the same result.

The "state" tells you is the widget is enabled or disabled.

To get ALL of the options for a widget you can work with
for the widget 'print(<widget>.configure()

"""

import tkinter as tk
from tkinter import ttk

def button_func():
    # Contenet of the entry
    entry_data = entry.get()    # Entry widget has the get method
    #print(entry_data)
    
    # get method
    #print(label.get())          # Label widget do not have the get method
                                # 'Label' object has no attribute 'get'
    # configure method - update
    # way 1
    #label.configure(text = "other text")
    
    # way 2
    #label["text"] = "newer text"
    
    label["text"] = entry_data
    
    print(entry["state"]) # => Normal
    entry["state"] = "disabled"
    print(entry["state"]) # => "disabled"
    
    print(entry.configure())
    
def button_func2():
    
    label["text"] = "some text"
    entry["state"] = "normal"

window = tk.Tk()
window.title("Getting and Setting widgets")
window.geometry("200x120")




# Widgets
label = ttk.Label(window, text="Hello")
entry = ttk.Entry(window)
button = ttk.Button(window, text="Change", command=button_func)
button2 = ttk.Button(window, text="Restore", command=button_func2)

label.pack()
entry.pack()
button.pack()
button2.pack()


window.mainloop()




