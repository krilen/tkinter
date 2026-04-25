"""
A tkinter app is based on 3 major components
 * Widgets: text, button, input field, ...
 * Layout: how to widgets are arranged in the Window
 * Style: size of the text, color of the button, background color, ...
"""
import tkinter as tk        # Logic
#from tkinter import ttk     # Widgets
import ttkbootstrap as ttk

def convert():
    #print(entry.get()) # One of getting the ingo from a widget
    #print(entry_var.get())
    #output_var.set("hello")

    mile_input = entry_var.get()
    km_output =  str(round(mile_input * 1.61, 2)) + " km"
    output_var.set(km_output)

# Window
#window = tk.Tk()
window = ttk.Window(themename="vapor")
window.title("Demo")
window.geometry("300x150")

# Title
title_label = ttk.Label(window, 
                        text="Miles to kilometer", 
                        font="Calibri 24 bold")
title_label.pack(pady=10)

# Input
input_frame = ttk.Frame(window)

entry_var = tk.IntVar()
entry = ttk.Entry(input_frame, 
                  textvariable=entry_var)

button = ttk.Button(input_frame, 
                    text="Convert", 
                    command=convert)

entry.pack(side="left", padx=10)
button.pack(side="left")
input_frame.pack(pady=5)

# Output
output_var = tk.StringVar()
output_label = ttk.Label(window,
                        text="",
                        font="Calibri 20",
                        textvariable=output_var)

output_label.pack(pady=5)


# Run
window.mainloop()