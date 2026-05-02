"""
 EVENTS
========================

Different kinds of events
 * Keyboards inputs
 * Widget getting changed
 * Widgets gets selected / unselected
 * Mouse click / motion / wheel

Events can be observed and used, ex: run a function on button press.

You need to bind an event to a widget, '<widget>.bind(<event>, <function)'

The format for an event is: <<modifier>-<type>-<detail>>, ex: '<Alt-Keypress-a>'
 
https://www.pythontutorial.net/tkinter/tkinter-event-binding/

ONLY when the widget is selected does the modifier become valid.
When an event is triggered the event itself is forwared to the function.

Tkinter only checks the event on the current selected widget, but the window is 
always selected.


"""

import tkinter as tk
from tkinter import ttk


def get_pos(event):
    print(f"Position: x{event.x}, y{event.y}")




# Setup
window = tk.Tk()
window.title("Event bindings")
window.geometry("600x500")

text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text = "A button")
button.pack()

# Events
# Applies to th whole window
window.bind("<Alt-KeyPress-a>", lambda event: print("An event:", event))
# Only works when the button is selected and ALT+b
button.bind("<Alt-KeyPress-b>", lambda event: print("An button event:", event))
# Motion
#window.bind("<Motion>", get_pos)
# Text windget
#text.bind("<Motion>", get_pos)
# Only a keypress not a specific combination
window.bind("<KeyPress>", lambda event: print(f"Key '{event.char}' was pressed!"))

# Verify if a windget has been selected, in Focus.
entry.bind("<FocusIn>", lambda event: print("Entry was selected (in Focus)"))
# Widget as been un-selected
entry.bind("<FocusOut>", lambda event: print("Entry was deselected (in Focus)"))

# Exercise
text.bind("<Shift-MouseWheel>", lambda event: print("Mousewheel"))

window.mainloop()