"""
 WINDOW
========================
Widgets are the building blocks of tkinter
Widgets: text, buttons, checkboxes, menus, frames, ...

Understanding the widgets and controlling them is key to mastering
the tkinter gui framework (or any oter framework and lanhuage).

There are 2 types of widgets
 * tk widgets that are the original ones
 * ttk widgets where added later on (more modern)
 
tk widgets looks outdated, you should primarily use ttk widgets.

tkk widgets works like the old ones but the look better and have
some extra functionality.

'window = tk.Tk()' - Create the window

'mainloop' - Runs until the 'window' is closed.
 * Updates the GUI, text, color, ... and you see the results
 * Checks for events (button clicks, mouse movements, closing a window, ...)

"""

import tkinter as tk
from tkinter import ttk

# A function called by the Event of a button pressed
def button_func():
    print("A button was pressed!")      # Print out in the CLI

def button_hello():
    print("hello 1")      # Print out in the CLI

window = tk.Tk()                        # Create the window
window.title("Window and Widgets")      # Title of the window
window.geometry("500x650")              # Size of the window at start, (width height)

# TKK widget
from tkinter import ttk

label = ttk.Label(window, text="This is a test")
label.pack()

# TK widget
#tk.Text(window).pack()                 # Tk Textbox (old) using the pack layout method
text = tk.Text(window)                  # Sqme as the above but with 2 rows of code
text.pack()

# TTK entry
entry = ttk.Entry(window)
entry.pack()

# exercise label
ttk.Label(window, text="my label").pack()

# TTK button
button = ttk.Button(window, text="A button", command=button_func) # Call function 'button_func'
button.pack()

# exercise button
ttk.Button(window, text="Hello 1", command=button_hello).pack()
ttk.Button(window, text="Hello 2", command=lambda: print("hello 2")).pack()

# Run
window.mainloop()                       # Runs until the window is closed, updates the 
                                        # GUI and looks for Events

print("hello") # Will ONLY be processed when the mainloop ends (window is closed)
