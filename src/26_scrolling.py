"""
 RESPONSIVE LAYOUTS
========================

In Tkinter there are 3 widgets that can be scrolled
 * Canvas
   Is useful since it can display widgets.
 * Text
 * Treeview

A scrollbar is just another widget


"""
import tkinter as tk
from tkinter import ttk
from random import randint, choice

# Setup
window = tk.Tk()
window.title("Scrolling")
window.geometry("600x400")

# ### Canvas
# canvas = tk.Canvas(window, bg="white", scrollregion=(0,0,2000,5000)) # Scrollregion: left, top, right, bottom

# # Line
# canvas.create_line(0,0,2000,5000, fill="green", width=10)

# # Rectangles
# for i in range(100):
#     l = randint(0, 2000)
#     t = randint(0, 5000)
#     r = l +randint(10, 500)
#     b = t +randint(10, 500)
#     color = choice(("red", "black", "green", "orange", "blue", "purple", "yellow", "pink", "brown"))
    
#     canvas.create_rectangle(l, t, r, b, fill=color)

# canvas.pack(expand=True, fill="both")

# ## Mousewheel Vertical
# canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(-int(event.delta / 60), "units"))
# canvas.bind("<Button-4>", lambda event: canvas.yview_scroll(-2, "units")) # Linux up
# canvas.bind("<Button-5>", lambda event: canvas.yview_scroll(2, "units")) # Linux down

# ### Mousewheel Horisontal
# canvas.bind("<Control-MouseWheel>", lambda event: canvas.xview_scroll(-int(event.delta / 60), "units"))
# canvas.bind("<Control-Button-4>", lambda event: canvas.xview_scroll(-2, "units")) # Linux right
# canvas.bind("<Control-Button-5>", lambda event: canvas.xview_scroll(2, "units")) # Linux left

# # Scrollbar
# scrollbar_v = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
# canvas.configure(yscrollcommand=scrollbar_v.set)
# scrollbar_v.place(relx=1, rely=0, anchor="ne", relheight=1)

# scrollbar_h = ttk.Scrollbar(window, orient="horizontal", command=canvas.xview)
# canvas.configure(xscrollcommand=scrollbar_h.set)
# scrollbar_h.place(relx=0, rely=1, anchor="sw", relwidth=0.98)


# ### Text
# text = tk.Text(window)

# for i in range(1, 200):
#     text.insert(f"{i}.0", f"text: {i}\n")

# text.pack(expand=True, fill="both")

# ## Scrollbar
# scrollbar_text = ttk.Scrollbar(window, orient="vertical", command=text.yview)
# text.configure(yscrollcommand=scrollbar_text.set)
# scrollbar_text.place(relx=1, rely=0, anchor="ne", relheight=1)


### Treeview
table = ttk.Treeview(window, columns=(1,2), show="headings")
table.heading(1, text="First name")
table.heading(2, text="Surname")

first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

for i in range(100):
    
    fname = choice(first_names).title()
    lname = choice(last_names).title()
    
    row = (fname, lname)
    
    table.insert(parent="", index=tk.END, values=row)

table.pack(fill="both", expand=True)

## Scrollbar
scrollbar_table= ttk.Scrollbar(window, orient="vertical", command=table.yview)
table.configure(yscrollcommand=scrollbar_table.set)
scrollbar_table.place(relx=1, rely=0, anchor="ne", relheight=1)

# Run
window.mainloop()