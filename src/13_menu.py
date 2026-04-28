"""
 MENUS
========================

Menus are created with 'tk.Menu' (old version).

But you need to know that you use multiple of them and nest them.

If you plase a 'tk.Menu' inside of an 'tk.Menu' this will become ONE option.

Methods that can be used with the menu widget
https://www.tutorialspoint.com/python/tk_menu.htm


A menu button widget uses 'ttk.Menubutton'

"""

import tkinter as tk
from tkinter import ttk


# Setup
window = tk.Tk()
window.title("Menu")
window.geometry("600x400")


# Menu
menu = tk.Menu(window) # The menu bar, first menu is invisible, only see its children

# sub menu
file_menu = tk.Menu(menu, # Start to create an menu option ("File")
                    tearoff=False) # tear off the menu option set defualt to True 
file_menu.add_command(label="New", # Add submeny "New" under "File", an entire
                      command=lambda: print("Menu: 'New'")) # What should happen
file_menu.add_command(label="Open", # Add submeny "New" under "File"
                      command=lambda: print("Menu: 'Open'")) # What should happen
file_menu.add_separator() # seperator
menu.add_cascade(label="File", menu=file_menu) # Add the different submenus to the main main option

            
# help menu
help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label="Support", command=lambda: print("Menu: 'Support':", help_check_str.get())) # What should happe

help_check_str = tk.StringVar(value="on")
help_menu.add_checkbutton(label="Check",
                          onvalue="on",
                          offvalue="off",
                          variable=help_check_str,
                          )

menu.add_cascade(label="Help", menu=help_menu)

# Exercise
exercise_menu = tk.Menu(menu, tearoff=False)
exercise_menu.add_command(label="Exercise 1")
menu.add_cascade(label="Exercise", menu=exercise_menu)

# Exercise sub sub menu
exercise_sub_menu = tk.Menu(menu, tearoff=False)
exercise_sub_menu.add_command(label="Some more stuff")
exercise_menu.add_cascade(label="More stuff", menu=exercise_sub_menu)


window.configure(menu=menu) # Connect the menu to the window


# Menu button
menu_button = ttk.Menubutton(window, text="Menu Button")
menu_button.pack()

menu_button_sub = tk.Menu(menu_button, tearoff=False)
menu_button_sub.add_command(label="entry 1", command=lambda: print("entry 1"))
menu_button_sub.add_command(label="entry 2", command=lambda: print("entry 2"))

#menu_button.configure(menu=menu_button_sub)
menu_button["menu"] = menu_button_sub  # The same thing as above the line

# Run
window.mainloop()