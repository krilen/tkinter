"""
 COMBOBOX and SPINBOX WIDGETS
========================
Combobox is a dropdown
Spinbox is a selection / menu where you scroll predefined value (numbers or strings)

Both need a list of values and they both can be connected to a Tkinter variable

With Combobox there is an unique event that can be used everytime a selection is made

A spinbox works simulare like a combobox.

Sepcial events for the spinbox when going up or down through the spinbox
<spinbox>.bind("<<Increment>>", ...) - Going up
<spinbox>.bind("<<Decrement>>", ...) - Going down

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

combo1_label = ttk.Label(window, text="Animal")             # Other way by using lambda
combo1_label.pack()

# Spinbox   
spin_int = tk.IntVar(value=12)              # Start value

spin1 = ttk.Spinbox(window, 
                    from_= 3, to=20,        # Another way of defing values 3 to 20
                    increment=3,            # step size
                    #command=lambda: print("spin was pressed"),
                    command=lambda: print(spin_int.get()),
                    textvariable=spin_int
                    )     
#spin1["value"] = (1,2,3,4,5)               # One way of defining values

# Spinbox event
spin1.bind("<<Increment>>", lambda event: print("up"))      # Up
spin1.bind("<<Decrement>>", lambda event: print("down"))    # Down
spin1.pack()

# Exercise

spin2_letters = ("A", "B", "C", "D", "E")
spin2_str = tk.StringVar(value=spin2_letters[-1])

spin2 = ttk.Spinbox(window,
                    textvariable=spin2_str,
                    values=spin2_letters,
                    )

spin2.bind("<<Decrement>>", lambda event: print("Down to:", spin2_str.get()))
spin2.pack()


window.mainloop()