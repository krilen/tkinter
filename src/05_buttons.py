"""
 BUTTONS
========================

There are different types of buttons
 * Normal button

 * Checkbox button
   Each checkbox is or should be by itself but they can be connected.
   By default when a checkbox button start it is in a neutral state not enabled or disabled.
   We need the tkinter variable to get or set its state
   The button can have different tkinter variable types
   The button also have two specific arguments 'onvalue' / 'offvalue' that can be used to set
   the value when the button is checked or not checked.

 * Radio button (normally many at the same time)
   Each radiobutton should be connected to each other by the tkinter variable.
   Each of the radio button needs a value.
   Through the tkinter variable the buttons are connected



"""
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Buttons")
window.geometry("600x400")

# Button
def button_func():
    print("A basic button")

button_var = tk.StringVar(value="Button") # Value will override the 'text' of the button

button = ttk.Button(window, text="Button", command=button_func, textvariable=button_var)
button.pack()

# Checkbutton
check1_var = tk.IntVar(value=0)

check1 = ttk.Checkbutton(window, 
                         text="checkbox 1",
                         command=lambda: print("Check button 1:", check1_var.get()),
                         variable=check1_var,
                         onvalue=1,
                         offvalue=0)
check2 = ttk.Checkbutton(window, 
                         text="checkbox 1",
                         command=lambda: print("Check button 2:", check1_var.get()))

check1.pack()
check2.pack()


# Radiobutton
radio_var = tk.StringVar()

radio1 = ttk.Radiobutton(window,
                         text="Radiobutton 1",
                         value="radio 1",
                         variable=radio_var,
                         command=lambda: print(radio_var.get()))
radio2 = ttk.Radiobutton(window,
                         text="Radiobutton 2",
                         value=2,
                         variable=radio_var,
                         command=lambda: print(radio_var.get()))

radio1.pack()
radio2.pack()

# Exercise

check_var2 = tk.BooleanVar()
radio_var2 = tk.StringVar()

def radio_func():
    print("Value of checkbutton: ", check_var2.get())
    check_var2.set(False)

def check_func():
    print("Value of radiobutton: ", radio_var2.get())

radioA = ttk.Radiobutton(window,
                         text="Radio A",
                         value="A",
                         variable=radio_var2,
                         command=radio_func,
                         )
radioB = ttk.Radiobutton(window,
                         text="Radio B",
                         value="B",
                         variable=radio_var2,
                         command=radio_func,
                         )
checkC = ttk.Checkbutton(window, 
                         text="Check C",
                         command=check_func,
                         variable=check_var2,
                         onvalue=True,
                         offvalue=False
                         )

radioA.pack()
radioB.pack()
checkC.pack()


window.mainloop()