"""
 SLIDERS
========================

In Tkinter there are two types
 * sliders
 * progress bar
 
Both shows progress in one dimension (horisontal or vertical)

The slider can be moved by the user or set independently.

While the progress bar can only be set independently, nothing to useas input.

The a slider is move it provides an output value where it is. By defualt the values are 0 to 1
But this can be changed using 'from_' and 'to'.

By defult a slider is horisontal but can be chnage using the arugemnt 'orient="vertical"'.

By default a progress bar have a maximum value of 100 but this can be changed by 'maximum'

It is also possible to set the mode of the progress bar, how the progress is displayed.
 * A progrss that extends from 0 till whatever, 'mode="determinate"', the default.
 * Or a vlock that moves acorss the progress bar, 'mode="indeterminate"'
 
A progrss bar have a couple of special methods called start and stop.
 * <widget>.start() - will start the progress bar and affect anything connected to it
    The ms can be set as a value
 * <widget>.stop() - will stop the progress bar  


There is also something called scrolled test that needs to be imported,
'from tkinter import scrolledtext'. It is not a widget but it contains other widgets, combined 
widget. It contains a text field and a slider but can be used as a widget.
 * 'scrolledtext.ScrolledText(window)' - it is a text field with an scroll




"""

import tkinter as tk
from tkinter import ttk

# For scolled text
from tkinter import scrolledtext

# Setup
window = tk.Tk()
window.title("Sliders")
window.geometry("600x800")

# Slider
scale_var = tk.DoubleVar(value=15.0)

scale = ttk.Scale(window,
                  #command=lambda value: print(value)   # When the slider is moved an value output 
                                                        # from 0 to 1, ex: 0.7789955...
                  from_=0,
                  to=25,
                  #command=lambda value: print(value),
                  command=lambda _: print(scale_var.get()),
                  length=80,                           # Lenght of the slider
                  orient="vertical",                    # Change from the default horizontal orient
                  variable=scale_var,
                )
scale.pack()

# Progress bar
progress = ttk.Progressbar(window,
                           variable=scale_var,      # What to "follow"
                           maximum=25,              # Change the max in the progress bar
                           orient="vertical",       # Change the default orient to vertical
                           mode="indeterminate",
                           length=80
                           )
progress.pack()

progress.start(100)

button = ttk.Button(window,
                    command= lambda: progress.stop(),
                    text="Stop progress bar",
                    )
button.pack()

# Scrolled text
scrolled_text = scrolledtext.ScrolledText(window,
                                          width=60,
                                          height=10)
scrolled_text.pack()

# Exercise

progress2_var = tk.IntVar()

progress2 = ttk.Progressbar(window,
                            variable=progress2_var,
                            maximum=20,
                            orient="vertical",
                            )

label = ttk.Label(window,
                  textvariable=progress2_var,
                  )

slider = ttk.Scale(window,
                   variable=progress2_var,
                   from_=0,
                   to=20,
                   ) 

progress2.pack()
label.pack()
slider.pack()

progress2.start()


# Run
window.mainloop()