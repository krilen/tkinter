"""
 TOOGLE
========================
Toogle = on / off or visable / invisable

In tkinter you dont hide / reveal widgets you remove and add widgets to the layout.

'pack', 'grid' and 'place' are the methods used to add widgets.

While 'pack_forget', 'grid_forget' and 'place_forget' are methods used to remove widgets.

Both place and grid method works without any problem with their layout forget method.

The problem is pack since it depends on removing widgets then the stacking is changed and the
widgets move. When placing the widget again it lands on top. The solution is add a replacement
frame that is visisble for the widget that is removed. But when placing this widget you must
use the argument 'before' and define before which widget. This way the widget is not added on
top of the stacking but in the stack at the appropriate place.

"""

import tkinter as tk
from tkinter import ttk



# Setup
window = tk.Tk()
window.title("Hide widgets")
window.geometry("400x400")


# ### Place
# ## Func to toogle
# def toggle_label_place():
#     global label_visable
    
#     if label_visable:
#         label.place_forget()    # Removes the placement for the label
#         label_visable = False
        
#     else:
#         label.place(relx=0.5, rely=0.5, anchor="center") # Places the label
#         label_visable = True

# # Toggle button
# button = ttk.Button(window, text="Toogle Label", command=toggle_label_place)
# button.place(relx=0.5, rely=1, anchor="s")

# # Toggle variable
# label_visable = True

# # Widget
# label = ttk.Label(window, text="A label", background="yellow", padding=80)
# label.place(relx=0.5, rely=0.5, anchor="center")




# ### Grid
# window.columnconfigure((0,1), weight=1, uniform="a")
# window.rowconfigure(0, weight=1, uniform="a")

# ## Func to toogle
# def toggel_label_grid():
    
#     global label_visable
    
#     if label_visable:
#         label.grid_forget()
#         label_visable = False
        
#     else:
#         label.grid(row=0, column=1, sticky="nswe", padx=10, pady=20)
#         label_visable = True

# # Toggle button
# button = ttk.Button(window, text="Toogle Label", command=toggel_label_grid)
# button.grid(row=0, column=0, sticky="nswe", padx=40, pady=160)

# # Toggle variable
# label_visable = True

# # Widget
# label = ttk.Label(window, text="A label", background="orange")
# label.grid(row=0, column=1, sticky="nswe", padx=10, pady=20)


### Pack
## Func
def toggel_label_pack():
    
    global label_visable
    

    
    if label_visable:
        label.pack_forget()
        label_visable = False
        frame.pack(expand=True, before=button)
        
    else:
        frame.pack_forget()
        label.pack(expand=True, fill="both", padx=20, pady=20, before=button)
        label_visable = True

# Toggle variable
label_visable = True

# Widget
label = ttk.Label(window, text="A label", background="lightgreen")
label.pack(expand=True, fill="both", padx=20, pady=20)

# Toggle button
button = ttk.Button(window, text="Toogle Label", command=toggel_label_pack)
button.pack()

# Frame
frame = ttk.Frame(window)

# Run
window.mainloop()