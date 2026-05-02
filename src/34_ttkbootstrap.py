"""
 TTKBOOTSTRAP
========================

https://ttkbootstrap.readthedocs.io/en/latest/

Another useful tool to customize Tkinter is "ttkbootstrap", are also an exteranl moduel
that needs to be installed, 'pip install ttkbootstrap'

While for customtikinter we customize widgets individually, ttkbootstrap applies thems to
every windget.

It makes it easier to style widgets but gives us less control.

Simply by importing ttkbootstrap we are applying a new theme. But normally you 'import
ttkboostrap as ttk'. On thing that you must be aware of is that we do NOT want to use "tk.TK()"
for the window but instead use "ttk.Window()". Because with the new window we can add theme
name.



"""

import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
#from ttkbootstrap.constants import *

def on_theme_change():
    print("Theme is now:", style.theme.name)


def toggle_action():
    
    if toggle_var.get() == "journal":
        print("light")
        style.theme_use("journal")
    else:
        print("dark")
        style.theme_use("darkly")
    
    #print("Toggle state:", toggle_var.get())



# Setup
#window = tk.Tk()
window = ttk.Window() # darkly, journal, 
window.title("TTK Bootstrap intro")
window.geometry("400x300")

# Style
style = ttk.Style()
style.theme_use("journal")
#style.theme_use("darkly")

# Widgets
label = ttk.Label(window, text="Label")
label.pack(pady=10)

button1 = ttk.Button(window, text="Button 1", bootstyle="primary-outline")
button1.pack(pady=10)

button2 = ttk.Button(window, text="Button 2", bootstyle="info-link")
button2.pack(pady=10)

button3 = ttk.Button(window, text="Button 3", command=on_theme_change)
button3.pack(pady=10)

toggle_var = ttk.StringVar(value="journal")

toggle = ttk.Checkbutton(
    window,
    text="Light mode",
    bootstyle="info-squared-toggle",
    variable=toggle_var,
    onvalue="journal",
    offvalue="darkly",
    command=toggle_action
)

toggle.pack(pady=20)


# Run
window.mainloop()