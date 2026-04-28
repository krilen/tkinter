"""
 TABS
========================

'ttk.Notebook' is a weidget that creates tabs in the window.

The 'ttk.Notebook' will have a couple of children (frames) and each fram will be a tab.

And in each frame you can add widgets, the notebook itself will be invisable the only thing you
will see is the tabs.



"""

import tkinter as tk
from tkinter import ttk


# Setup
window = tk.Tk()
window.title("Tabs")
window.geometry("600x400")

# Notebook (tab)
notebook = ttk.Notebook(window)

# tab 1
tab1 = ttk.Frame(notebook)


label1 = ttk.Label(tab1, text ="Text in tab 1")
label1.pack()
button1 = ttk.Button(tab1, text="Button in tab 1")
button1.pack()

# Tab 2
tab2 = ttk.Frame(notebook)

label2 = ttk.Label(tab2, text ="Text in tab 2")
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()

# Exercise
tab3 = ttk.Frame(notebook)

ttk.Label(tab3, text ="Exercise text").pack()
ttk.Button(tab3, text="Button 1 in exercise").pack()
ttk.Button(tab3, text="Button 2 in exercise").pack()

# Add tabs och pack
notebook.add(tab1, text="Tab 1")        # packing the frame
notebook.add(tab2, text="Tab 2")        # packing the frame
notebook.add(tab3, text="Exercise")     # packing the frame

notebook.pack()


# Run
window.mainloop()