"""
 GRID LAYOUT
========================
When using the 'grid' layout you set the number of rows and columns.
The height and width of each colomn and row can be set.

With the grid layout it will always scale along when the window change.. 

After that you place the widget in a column and row.
A widget can occupy multiple cells (row and columns) and can have padding.

Overlapping widgets is possible and the last one that is placed on the grid that is on top.

Like with 'pack' the grid only determind how much space a widget CAN occupy but not how much it
WILL occupy.

In the 'pack' we have the 'fill' argument but in 'grid' we have the 'sticky' argument. The
'sticky' argument tells on which border of the space the widget should "connect" to. By default
the widget is in the center of the space but by setting 'sticky' for n (north), s (south), w (west)
and e (east) the widget can fill out the space.

Examples
 * sticky="n": Widget will retain its size but stick to the top.
 * sticky="ns": Widget will retain width but height is the height of the cell.
 * sticky="nsew": Widget will expand to the size of the cell.
 * sticky="nw": Widget will retian its size but stick to the upper left corner.
 * sticky="new": Widget will expand only it witdh and stick to the top.

There are two types of padding
 * 'padx' and 'pady'
    Expands the space around the widget to give space between the current widget and its neighbour

 * 'ipadx' and 'ipady'
    Expands to current border of the widget, makes it larger.
    But is also shrinks other cells.

There is one thing that is weird with grid and it has to do with empty cells, uniformity, and
their width might not be what you expect. Cells with widgets may become wider next to empty cells.
To fix this you add the argument 'uniform="a"' to the rows and columns that you define.



"""

import tkinter as tk
from tkinter import ttk


# Setup
window = tk.Tk()
window.title("Grid layout")
window.geometry("600x400")

# Widgets
label1 = ttk.Label(window, text="Label 1", background="red")
label2 = ttk.Label(window, text="Label 2", background="blue")
label3 = ttk.Label(window, text="Label 3", background="green")
label4 = ttk.Label(window, text="Label 4", background="yellow")
button1 = ttk.Button(window, text="Button 1")
button2 = ttk.Button(window, text="Button 2")
entry = ttk.Entry(window)

# Define grid
window.columnconfigure((0,1,2), weight=1, uniform="a")
window.columnconfigure(3, weight=2, uniform="a")
window.rowconfigure((0,1,2), weight=1, uniform="a")
window.rowconfigure(3, weight=3, uniform="a")


# Place a widget
label1.grid(row=0, column=0,
            sticky="nswe",          # sticky for full witdh and height
            ipady=50)               # pushes the other cells down to make the widget bigger
label2.grid(row=1, column=1, 
            rowspan=3,              # span 2 rows from the cell
            sticky="nsew") 
label3.grid(row=1, column=0, 
            columnspan=3,           # span 3 columns from the cell                       
            sticky="nsew",
            padx=20,                # created a space around the widget
            pady=10)
label4.grid(row=3, column=3, sticky="se")

# Exercise
button1.grid(row=0, column=3, sticky="nswe")
button2.grid(row=2, column=2, sticky="nswe")
entry.grid(row=2, column=3, rowspan=2)

# Run
window.mainloop()

