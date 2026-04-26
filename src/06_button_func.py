"""
 BUTTON FUCTIONS
========================

When using function you can use lambda function to call functions with
arguments.

Or you could create a function that returns another function. At page
load the uter_func' is automatically executed but it ONLY returns
the 'inner_func' and this is what gets executed at the first and all
presses after.




"""
import tkinter as tk
from tkinter import ttk

# Function using lambda to wrap
def button_func(entry_string):
    print("Button was pressed. Entry value:", entry_string.get())

# Function using inner function
def outer_func(parameter):
    def inner_func():
        print("Button was pressed. Entry value:", parameter.get())
    return inner_func

# Setup
window = tk.Tk()
window.title("Button functions with arguments")
window.geometry("600x400")

# Widgets
entry_str = tk.StringVar(value="test")

entry = ttk.Entry(window,
                  textvariable=entry_str
                  )
entry.pack()

button = ttk.Button(window,
                    text="Button",
                    #command=button_func(entry_str)         # Automatically at start without pressed
                    #command=lambda: button_func(entry_str) # Using 'lambda' to wrap the function 
                                                            # fixes the problem
                    command=outer_func(entry_str)           # Using an outer function with return and 
                    )                                       # and inner func to execute
button.pack()

window.mainloop()