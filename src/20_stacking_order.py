"""
 STACKING ORDER
========================

You need to control which widget is on top of the other.
Espacially with the layout grid and place where you can place widgets on to of each other.

Widgets are always placed on top of other widgets when the are created NOT when they are 
placed. The layout method has nothing to with the stacking order.

Example: 'label1 = ttk.Label()'
         'label2 = ttk.Label()'   <-  created
         'label1.grid()'
         'label2.grid()'          <-- placed

         'label2' is going to be on top becasre it was CREATED after 'label1'
         
But it is possible to raise a widget above another widget.

Using
 * 'lift' method, it will raise the widget above the other overlapping widgets
 * 'lower' method, opposite to 'lift' it will place the widget below the oter widgets
 * 'tkraise' method, does the same thing as 'lift', why???

With both 'tkraise' and 'lift' an argument can be added 'aboveThis'. By default the widget
gets put on top of all other widgets. But by using 'aboveThis' ayou specify a particulare
widget to be above and not to be on top.

"""

import tkinter as tk
from tkinter import ttk


# Setup
window = tk.Tk()
window.title("Stacking order")
window.geometry("400x400")

# Widget
label1 = ttk.Label(window, text="Label 1", background="green")
label2 = ttk.Label(window, text="Label 2", background="red")

# Exersise
label3 = ttk.Label(window, text="Label 3", background="blue")

#label1.lift() # Lift 'label1' over the other widgets
#label2.lower() # Lower 'label2' below the other widgets

button1 = ttk.Button(window, text="raise label 1",
                     command=lambda: label1.lift()) # Using command to lift 'label1'
button2 = ttk.Button(window, text="raise label 2",
                     command=lambda: label2.lift()) # Using command to lift 'label2'
# Exersise
button3 = ttk.Button(window, text="raise label 3",
                     command=lambda: label3.lift(aboveThis=label2)) # Be above ''label2'

# Layout
label1.place(x=50, y=100, width=200, height=150)
label2.place(x=150, y=60, width=140, height=100)

# Exersise
label3.place(x=180, y=130, width=90, height=90)

button1.place(rely=1, relx=0.5, anchor="se")
button2.place(rely=1, relx=0.75, anchor="se")

# Exersise
button3.place(rely=1, relx=1, anchor="se")

# Run
window.mainloop()