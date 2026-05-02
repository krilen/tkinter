"""
 SIZES
========================

All widgets can have a custom size. But that size can be overwritten by the layout methods.
You have 2 places where you can add the size of the widget but one is prioritized.

Example: 'ttk.Label(parent, text="label", width=10).pack(fill="x")'
          * The label is given the width of 50, not pixels but characters since that 
            is what tkinter uses.
          * Then you have the with oc the pack method, that in this case tellinge the widget
            to fill entire horisontal space.
          * Now tkinter must decide what to do, the default awnser is the layout method'fill="x"'
          
If there are two width you are going to get the one from the layout method.

But in some cases this can cause problem with the layout as shown below.

If you use the metods in the layouts to determin the size you shoul remove any defined size
in the widget.

Also you should always want a flexible layout and any hardcoded size in the widget will cause
problems. Since the window can become very large or very small you should make it flexibale by
using the size methods in the layout.

"""

import tkinter as tk
from tkinter import ttk


# Setup
window = tk.Tk()
window.title("Sizes")
window.geometry("500x300") # The window size is in pixel NOT charachters as the widgets

# Widget
label1 = ttk.Label(window, text="Label 1", background="green") # Used as refrence
label2 = ttk.Label(window, text="Label 2", background="red",
                   width=50) # tkinter character units NOT pixels like the window size.

### Layout - override the defined windget size
## Pack
#label1.pack()
#label2.pack(fill="x") # Actual size since the layout methods overrides the widget custom width

## Grid
#window.columnconfigure((0,1), weight=1, uniform="a")
#window.rowconfigure((0,1), weight=1, uniform="a")
#
#label1.grid(row=0, column=0)
#label2.grid(row=1, column=0, sticky="nswe") # Again the layout method for size overrides
                                            # the widget custom width

## Place
label1.place(relx=0.5, rely=0.2, anchor="center")
label2.place(relx=0.5, rely=0.7, anchor="center",
                  relwidth=0.5, relheight=0.5) # Again the layout size overrides the widget size
# Run
window.mainloop()