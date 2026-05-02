"""
 CustomTkinter
========================

https://customtkinter.tomschimansky.com/

There are external modules that are build onto of tkinter to improve it. Must of it is styling
but some extra functionalities, customtkinter and ttkbootstrap are two of these modules.

Customtkinter uses the same widgets as ttk but give you the ability to east customise them.
There are also some additional widgets and all widgets has a dark or light mode.
Customtkinter has very good documentation.

CustomTkinter needs to be installed since it does not come with Python by default.
'pip install customtkinter'

You need to import customtkinter instaed och the normal tkinter libraries, 
'import customtkinter as ctk'. 

The window creation 'window = ttk.()' inherits from the normal 'TK' ('window = tk.Tk()'). That
makes all of the default arguments are availabe for use.

By default the CustomTkinter uses the default theme of your system. This can be changed by
'command=lambda: ctk.set_appearance_mode("light")' when triggerd the mode will chnage to ligt.

It is possible to get the current system theme by 'ctk.get_appearance_mode()' you would either get
"Dark" or "Light".

When we are able to set or change the color mode in the app we are also able to set different 
colors for the different depending on the color mode. This by specifing a tuple of color,
("white", "black") first argument for the light mode and the second for the dark mode.
This works for any single color.

"""
import customtkinter as ctk

def toggle_theme():
    current = ctk.get_appearance_mode()

    if current == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")



# Setup
window = ctk.CTk()
window.title("CustomTkinter")
window.geometry("600x400")

# Widget
label = ctk.CTkLabel(
    window, 
    text="A CTK Label", 
    fg_color="red", 
    text_color=("white", "black"),  # Different color depending och the color mode
                                    # "white" for light mode and "black" for dark mode
    corner_radius=10,
    )
label.pack()


button = ctk.CTkButton(
    window,
    text="A CTK Button",
    fg_color="#FF0",
    text_color="#000",
    hover_color="#AA0",
    command=lambda: ctk.set_appearance_mode("light"),
    )
button.pack()


button = ctk.CTkButton(
    window,
    text="Toggle Theme",
    command=toggle_theme
)
button.pack()

frame = ctk.CTkFrame(
    window,
    fg_color="transparent",
)

segemented_button = ctk.CTkSegmentedButton(
    frame,
    values=["Value 1", "Value 2", "Value 3"],
    command=print("hello"))

segemented_button.pack()

switch = ctk.CTkSwitch(
    frame,
    text="CTkSwitch", 
    command=print("hello"),
    #variable=switch_var,
    onvalue="on",
    offvalue="off"
    )
switch.pack()

frame.pack(expand=True, fill="both")









# Run
window.mainloop()