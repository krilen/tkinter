"""
 STYLING OPTIONS
========================

There are several ways of styling in Tkinter
 * Built-in styling options (widget options and styling object)
 * External themes that are applied to all widgets
 * External modules (sutomtkinter and ttkbootstrap). Theay are built onto of tkinter

Some widgets like "Label" can be styled with color, text, font, ...
Other widgets like "Button" can not be styled in the same way.
But there is a solution you need to create a styling object from Tkinter, using 'ttk.Style'

You can either use a style_theme or create something,
<style>.configure("T<widget>, <keyword>="<value>"), see in the example below.

The style is added automatically you do not need to specify that the widget should use it.

But you can also specify a specific style by adding a keyword infront ot the widget name,
<style>.configure("<keyword>.T<widget>, <keyword>="<value>"), see in the example below.
Then you need to specify the style argument for the widget.

Perhaps the best solution is to ONLY define specific styles for widgets and let the default
be as default.

It is even possible to define different states for a button using '<style>.map(....)'

"""
import tkinter as tk
from tkinter import ttk, font


# Setup
window = tk.Tk()
window.title("Styling")
window.geometry("400x300")

#print(font.families()) # get all fonts avaible

# Widgets
label = ttk.Label(
    window,
    text="A Label\n and a new line is...", # When lines are skrewd the 'justify' acts.
    background="lightgreen", # Background color
    foreground="white",      # Text color
    font=("Montserrat", 20), # Font to use and its size (in a tuple)
    justify="center",        # Where the text is placed in the widget, option "left, "center" or "right" 
                         )   # But not with the pack method

label.pack()

# The Button widget does not have any of the styling methods
# But we can create a style object that can be use on all widgets.
style = ttk.Style()
# print(style.theme_names()) # Get current styling themes that can be used
# style.theme_use("classic")

# Create a default style for all button, "green"
style.configure(
    "TButton",
    background="green",
    foreground="white",
    font=("Montserrat", 20),
    )

# Create a specific style for a widget
style.configure(
    "blue.TButton",
    background="blue",
    foreground="white",
    font=("Montserrat", 20),
    )

# Define the style during different states
style.map("blue.TButton", background = [("pressed", "red"),     # Press the button
                                        ("disabled", "yellow"), # argument needed: 'state="disabled" 
                                        ("hover", "pink"),      # hover over the button
                                        ])

# Use the default "green" button
button = ttk.Button(window, text="A Button")
button.pack()

# Used the defined "blue" button
button = ttk.Button(window, text="A Button", style="blue.TButton")
button.pack()


# Run
window.mainloop()