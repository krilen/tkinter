"""
 TABLES (TREEVIEW)
========================

If canvas is paint, treeview is excel.

The entries in the table can be "worked" with.

There is a special event for tables when a row is selected
<table>.bind("<<TreviewSelect>>", <func>)

When setting up like below 'ambda event: print(table.selection())'
The output will be a tuple that contains ID , one ID for one row but multiple ID when 
choosing multiple rows. The simplest way to work with the ID is using a for loop.

"""

import tkinter as tk
from tkinter import ttk

from random import choice

# Setup
window = tk.Tk()
window.title("Tables")
window.geometry("600x800")

first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']
domains = ["gmail.com", "hotmail.com", "email.com", "yahoo.com"]

# Treeview

table = ttk.Treeview(window, 
                     columns=("first", "last", "email"), # Name of the columns, define them
                     show="headings",                    # Placement of headings
                     )

# Show headings
table.heading("first", text="First name")
table.heading("last", text="Surname")
table.heading("email", text="Email")

table.pack(fill="both", expand=True)

# Insert values into the table by row single row
#table.insert(parent="", index=0, values=("John", "Doe", "john.doe@email.com"))

for i in range(100):
    
    fname = choice(first_names).title()
    lname = choice(last_names).title()
    email = f"{fname.lower()}.{lname.lower()}@{choice(domains).lower()}"
    
    row = (fname, lname, email.lower())
    
    table.insert(parent="",
                 index=0,       # the index where to place it, 0 meaning the first row
                 values=row,
                )

# Insert values into the last row
table.insert(parent="", index=tk.END, values=("X","Y","Z"))

def item_select(_):
    print(table.selection()) # => ('I063',)

    for id in table.selection():
        print(id)                       # The row ID
        print(table.item(id))           # => {'text': '', 'image': '', 
                                        #'values': ['Lisa', 'Walker', 'lisa.walker@hotmail.com'], 
                                        # 'open': 0, 'tags': ''}
        print(table.item(id)["values"]) # => "['Lisa', 'Walker', 'lisa.walker@hotmail.com']"

# Special event when selecting a row in the table
#table.bind("<<TreeviewSelect>>", lambda event: print(table.selection())) # => ('I063',)
table.bind("<<TreeviewSelect>>", item_select)

def delete_items(_):
    for id in table.selection():
        table.delete(id)
    
# Using event "delete"
table.bind("<Delete>", delete_items)

# Run
window.mainloop()