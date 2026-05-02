"""
 PLACE LAYOUT
========================

With the place method for layouts you specify the left, top, width and height of the widget.

You can use the absolute or relative positions.
 * Absolute
   You provide the top, left position and the width and height of the widget. The height and
   width is optional it not provided than the size of the widget will be its content.

 * Relative
   We use a coordinate system for x and y that goes between 0 and 1.
   Top left corner is (o.0, 0.0) and the lower right coner is (1.0, 1.0). Then you specify 
   the height and the width och the widget the same way, 0.1 is 10% of the widgets height.
   
   The best thing about using relative pos is that chnaging the window size everything will
   follow in both size and positioning.
   
The default size of the widget is the space that it takes up.

The .anchor' is the argument that tells which point on the widget should be used for the 
positioning, "center", "n", "s", "e", "w", "nw" (default), "ne","sw" and "se".

"""

import tkinter as tk
from tkinter import ttk


# Setup
window = tk.Tk()
window.title("Place layout")
window.geometry("400x600")

# Widgets
label1 = ttk.Label(window, text="Label 1", background="red")
label2 = ttk.Label(window, text="Label 2", background="blue")
label3 = ttk.Label(window, text="Label 3", background="green")
button1 = ttk.Button(window, text="Button 1")

# Create layout
label1.place(x=0, y=0,        # Absolute pos: top left
            width=200,        # Width of the widget
            height=50         # Height of the widget
            )
label2.place(relx=0.5, rely=0.5, # Relative placement in the middle => pos: 200x300
            relwidth=0.2,        # Realtive width (0.2 * 400) => 80px
            relheight=0.1        # Relative height (0.1 * 600) => 60px
            )
label3.place(x=200, y=300, width=80, height=60, anchor="center") # Use center as the anchor

# Frame
frame = ttk.Frame(window)
frame_label = ttk.Label(frame, text ="Frame label", background="yellow")
frame_button = ttk.Button(frame, text="Frame Button")

# Frame layout
frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)
frame_label.place(relx=0, rely=0, relwidth=1, relheight=0.5)

# Exercise
ttk.Label(window, text="middle of nowhere", background="purple").place(relx=0.5, 
                                                                        rely=0.5,
                                                                        anchor="center",
                                                                        height=200,
                                                                        relwidth=0.5)

# Run
window.mainloop()