"""
 COLORS
========================

The Tkinter default calors are red, white, blue, pink, green, ...

Yuu could use hexadecimal colors (<red>,<green>, <blue>).

The lenght of the hexcode is either 3 or 6 digits long.

You need to put a hash infront of the colorcode and Tkinter will recognize the string
as a color code, example '...background="#0AF"...' or '...background="#00AAFF"...'

"""
import tkinter as tk
from tkinter import ttk


# Setup
window = tk.Tk()
window.title("Colors")
window.geometry("400x300")

# Widgets
ttk.Label(window, background="#C50").pack(expand=True, fill="both") # Exercise: brown color
ttk.Label(window, background="#00AAFF").pack(expand=True, fill="both")
ttk.Label(window, background="#4FC296").pack(expand=True, fill="both")


# Run
window.mainloop()