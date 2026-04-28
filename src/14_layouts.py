"""
 LAYOUTS
========================

There are 3 methods for layouts
 * pack
   Takes a window and lets you stack widgets in a certain direction.
   By default you go from the top to the bottom, placing widgets below each other.
   You can tell a widget to take the enre vertical space , horisontal spce or both.
   It is also possible to stack widgets in different directions, left to right, right to left
   or bottom to top.
   
 * place
   You place widgets at a certain position and chnage the size. By defining the x and y position
   you place the widget.
   
   The 'x' and 'y' are absolute numbers regarding pixels.
   
   While 'relx' and 'rely' are relative numbers where the top left corner is (relx=0.0, rely=0.0)
   and the bottom right corner is (relx=1.0, rely=1.0)
   When working with 'place' you should use relavive position since the widget move is the window
   get bigger or smaller, wile the widget with absolute dont move and can be outside the window.
   
   By default the 'anchor', the point on the widget that the position uses it the top left corner,
   the nw point,but this can be changed. n (north), w (west), e (east), s (south), 
   nw (north west, default), sw, se (south east), nw and center.
 
 * grid
   You place a grid over the window and it used to pace widget in a certain position and take a
   number of rows or columns. Even place widgets over each oter using an overlap.
   The height of a row or the width of a column can be changed.
   To creating complex layouts 'grid' is the system to use.

You are able to combine the different layout method easily,  normally this is what you need to
do to create any complex layout.

You need to be aware of that you will heavily rely on parenting and frames to keep them orginized.

You place a layout in a frame then you place that frame to keep it all modulare and much easier
to maintain.



"""

import tkinter as tk
from tkinter import ttk


# Setup
window = tk.Tk()
window.title("Layout intro")
window.geometry("600x400")

# Widgets
label1 = ttk.Label(window, text="Label 1", background="red")
label2 = ttk.Label(window, text="Label 2", background="blue")
label3 = ttk.Label(window, text="Label 3", background="green")


# LAYOUT PACK
# label1.pack(side="left", # Side is where to place the widget, "top" default
#             expand=True, # Expand will take up all space it can, default is False.
#             fill="both", # Tells the widget to fill x, y both or none (default)
#             )
# label2.pack(side="right", expand=True, fill="y")


# LAYOUT GRID
# Grid setup needs to be done first
# window.columnconfigure(0,           # The index of the column, start with 0 and goes up 
#                        weight=1     # The size of the column
#                        )
# window.columnconfigure(1, weight=1) # Second column also the weight of 1
# window.columnconfigure(2, weight=2) # Third column the weight of 2, twice as wide as the other

# window.rowconfigure(0, weight=1)    # Setup and create 1 row
# window.rowconfigure(1, weight=1)    # Setup and create an additional row1 row

# As setup above we have u row with 3 column where the last column is the same size
# as the other columns
#  +-----+-----+-----------+
#  |     |     |           |   Row 0, Column 0, 1 and 2
#  |     |     |           |
#  +-----+-----+-----------+
#  |     |     |           |   Row 1, Column 0, 1 and 2
#  |     |     |           | 
#  +-----+-----+-----------+

# Place the widget in the grid

# label1.grid(row=0,              # row 0
#             column=0,           # column 0
#             sticky="nswe",      # By default the widget takes up as much space it needs.
#                                 # By using sticky we can expand the widget in the requested direction
#             )
# label2.grid(row=0, column=1, sticky="ns")
# label3.grid(row=0, column=2, sticky="we")

# # Using columnspan and rowspan to span the wiget into other columns or rows
# # You start with the defined column and row then expand to the right and down.
# label1.grid(row=0, column=0, rowspan=2, sticky="nswe")
# label2.grid(row=0, column=1, sticky="nswe")
# label3.grid(row=1, column=1, columnspan=2, sticky="nswe")


# LAYOUT PLACE
label1.place(x=0, y=0,                  # Top left corner, absolute pos
             width=200, height=100      # Width and the height, absolute
             )
label2.place(relx=0.42, rely=0.33,      # Somewhere in the middle, relative pos
             relwidth=1, relheight=0.5  # Relative size, grown and shrink
             )
label3.place(relx=0.6, rely=0.10,       # Somewhere in the middle, relative pos
             relwidth=0.25,             # Relative size, growns and shrinks
             relheight=0.25,           
             anchor="ne",           # Anchor in the center
             )

# Run
window.mainloop()