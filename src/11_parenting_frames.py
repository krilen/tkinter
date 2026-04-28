"""
 PARENTING and FRAMES
========================

Frames is just another widget but they are not used by themself. They are used to create a better
layout. And for a better layout you are going to need parenting.

In Python with Tkinter, the “master” (or “parent”) is simply the widget that contains another 
widget.

Think of it like a hierarchy (a tree):
 * The master/parent is the container
 * The child widget lives inside that container

In the beging the 'window' has been the the "parent" (or "master"). But this is something that you
might not want. A menu item would have the menu as the "parent" or a tab entry would have the tab
as its "parent".

What “parentr” means in practice
 * It controls where the widget appears
 * It determines lifetime (destroying the parent destroys its children)
 * It affects layout and grouping

For complex layout you create a container widget to organinse the oter widgets. This container
widget becomes the frame.

'ttk.Frame' is empty widget that other widgets can be placed in then the frame is placed.

Frames are invisible, and by default has no size, you can specify the height and width if needed.

The size of a frame is set by its children (widgets in the frame), this will override the width
and height specified for the frame. But it can be overwritten by setting
'<frame>.pack_propagate(False)', the default is 'True' and the frame changes it size for its
children.

If you set the size of the frame all of the widgets in it will comply with the size even if they
must change their size.

"""

import tkinter as tk
from tkinter import ttk


# Setup
window = tk.Tk()
window.title("Parenting and Frames")
window.geometry("600x400")

# Frame
frame = ttk.Frame(window,
                  width=200,        # Frames width
                  height=200,       # Frame height
                  borderwidth=10,   # Border for the frame
                  relief=tk.GROOVE # Make border visible
                                    #  - tk.FLAT is the default and you do not see anything.
                                    #  - tk.GROOVE - ???
                                    #  - tk.SOLID - A line around the frame
                                    #  - tk.RIDGE -  a raised frame around the frame
                                    #  - tk.RAISED - the frame get raised out of sunked into the window
                                    #  - tk.SUNKEN - the frame get sunked into the window
                  
                  )
frame.pack_propagate(False) # False - keep the frame height and width but 
                            # True (defualt) - let the children of the frame set the size of the frame
frame.pack(side="left")

# Parenting - master settings

label = ttk.Label(frame, text = "Label in frame")
label.pack()

button = ttk.Button(frame, text="A button in the frame")
button.pack()

# Example of why it is good
label2 = ttk.Label(window, text = "Label outside frame")
label2.pack()

# Exercise

frame2 = ttk.Frame(window, height=80, width=140, borderwidth=2, relief=tk.GROOVE)
frame2.pack_propagate(False)
frame2.pack(side="right")

ttk.Label(frame2, text="Frame2").pack()
ttk.Entry(frame2).pack()
ttk.Button(frame2, text="Button in frame").pack()
frame2.pack(side="right")

# Run
window.mainloop()