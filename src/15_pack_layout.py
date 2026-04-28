"""
 PACK LAYOUTS
========================

Stacking widget in order, default from the top (to the bottom). But this can be changed.
 * 'side': The side the widgets is added to ("left", "right", "top" (default) and "bottom")
           It is possibe to combine the different sides, but then the order of the pack
           becomes important. It is better and cleaner to use frames to orgize a more complex
           layout.

A widget can take up all of the horisontal or vertical space.
 * 'expand': Determins the vertical or horizontal space a widget CAN occupy (True or False)
             CAN is the keyworld since it tries to expand not how much it does expand.
             The widget mig only take a small part of the area but CAN use a larger area.
             
             The default is alwasys False.
             
             There are 2 kinds of space
              * The space a widget CAN occupy
              * The space a widget WILL occupy
              
            By default a widget WILL only be as big as its content (a label is only as big as
            its text) but the widget CAN occupy more space by default.
            
            If the side is "top" or "bottom"
             - Widgets CAN be as wide as the container.
             - Expands determin the height
            
            If the side is "left" or "right"
             - Widgets CAN be as heigh as the conytainer
             - Expands determin the width
             
 * 'fill': Sets how much space the widget WILL occupy ("x", "y", "both" or "None". "None" is the
           default and it only will take the space of the widget.
           
 * padding: Adds space for the widget.
            There is two kinds of padding
             * 'padx' or 'pady'
               That creates space AROUND the widget
               
             * 'ipadx' or 'ipady'
               That expands the widget
 
 
 
"""

import tkinter as tk
from tkinter import ttk


# Setup
window = tk.Tk()
window.title("Pack layout")
window.geometry("400x600")

# Widgets
label1 = ttk.Label(window, text="First label", background="red")
label2 = ttk.Label(window, text="Label 2", background="blue")
label3 = ttk.Label(window, text="The last label", background="green")
button = ttk.Button(window, text="Button")

# Layout
# label1.pack(side="top", expand=True, fill = "both")
# label2.pack(side="top")
# label3.pack(side="top")
# button.pack(side="top", expand=True, fill = "y")

# Exercise
# label1.pack(side="top", fill = "x", pady=50) # Added space above and below the label, the label is the same size
# label2.pack(side="top", expand=True)
# label3.pack(side="top", expand=True, fill = "both")
# button.pack(side="top", fill = "x", ipady=50) # The button expanded above and below, text in the middle.

# Different sides
# label1.pack(side="left", expand=True, fill="both")
# label2.pack(side="top", expand=True, fill="both")
# label3.pack(side="top", expand=True, fill="both")
# button.pack(side="top", expand=True, fill="both")

# Exercise
label1.pack(side="top", expand=True, fill="both", padx=10, pady=10)
label2.pack(side="left", expand=True, fill="both")
label3.pack(side="top", expand=True, fill="both")
button.pack(side="top", expand=True, fill="both")



# Run
window.mainloop()