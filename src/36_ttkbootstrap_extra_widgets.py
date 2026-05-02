"""
 TTKBOOTSTRAP EXTRA WIDGETS
========================

 ScrollFrame
------------------------
A frame that is scrollable but it has limitations, if something more than basic is needed a
custom scrollable frame should be created.

The graphics is a bit woobly when scrolling.

This import is needed: 'from ttkbootstrap.widgets.scrolled import ScrolledFrame'


 Toast
------------------------
Is a extra window that opens up with a message.

This import is needed: 'from ttkbootstrap.widgets.toast import ToastNotification'

There is a warning: if triggered by itself, '<toast>.show_toast()' it can affect the application,
is should be triggered seperat (by a button or something like that).


 Tooltip
------------------------
This is a way to give information about the different widgets, especailly button when you hover
over them. You create the widget then specify in the 'ToolTip' the specific widget and a text.
The text can be styled using ttkbootstrap.

This import is needed: 'from ttkbootstrap.widgets.tooltip import ToolTip'


 Calender
------------------------
Add a calender to simpyfy dates. Instead of wrintein a date you can get a calander and scroll to
a specific date. Then you can extract the date.

This import is needed: 'from ttkbootstrap.widgets.dateentry import DateEntry'


 Floodgauge / Progressbar
------------------------
This is a progressbar.

??? This import is needed: 'from ttkbootstrap.widgets.floodgauge import Floodgauge'


 Meter
------------------------

"""

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.widgets.scrolled import ScrolledFrame
from ttkbootstrap.widgets.toast import ToastNotification
from ttkbootstrap.widgets.tooltip import ToolTip
from ttkbootstrap.widgets.dateentry import DateEntry
#from ttkbootstrap.widgets.floodgauge import Floodgauge
from ttkbootstrap.widgets.meter import Meter



window = ttk.Window(themename="darkly")
window.title("TTK Bootstrap extra widgets")
window.geometry("500x900")

# Scrollable Frame
scroll_frame = ScrolledFrame(window, autohide=True)
scroll_frame.pack(expand=True, fill="both")

for i in range(1, 20):
    ttk.Label(scroll_frame, text=f"Label: #{i}").pack()
    ttk.Button(scroll_frame, text=f"Button: #{i}").pack()


# Toast
def warning_toast():
    toast.show_toast()

toast = ToastNotification(
    title="The title message", 
    message="The real message",
    duration=2000, # 2 sec
    bootstyle="warning",
    position=(10, 10, "ne"), # The padding x and y, then the place on the screen
    alert="True", # Sound then triggered
    )

ttk.Button(scroll_frame, text="Toast", command=warning_toast).pack(padx=5, pady=5)


# Tooltip
button = ttk.Button(window, text="Tooltip button", bootstyle="warning")
button.pack(pady=10)
ToolTip(button, text="This does something", bootstyle="danger-inverse")


# Calender
calender = DateEntry(window, firstweekday=0, dateformat="%Y%b%d")
calender.pack(pady=10)

ttk.Button(window, text="Get calander date", command=lambda: print(calender.entry.get())).pack(pady=10)


# Progressbar / Floodgauge
progress_int = tk.IntVar(value=10)
progress = ttk.Floodgauge(
    window, 
    text="progress", 
    variable=progress_int,
    bootstyle="danger",
    mask="{}%"
    )
progress.pack(pady=10, fill="x")

ttk.Scale(window, from_=0, to=100, variable=progress_int).pack()


# Meter
meter = ttk.Meter(
    window,
    bootstyle="danger",
    amounttotal=180,
    amountused=0,
    interactive=True,
    subtext="KPH",
    metertype="semi",
    ).pack()

# Run
window.mainloop()