"""
 MULTIPLE WINDOWS
========================

There are 2 option for extra windows
 * Messagebox for specialised windows (alert, yes no dialog)
   You need to import "messagebox", 'from tkinter import messagebox'
   Then you must choose the specialized message box
    * askquestion
    * askokcancel
    * askyesno
    * ...
    
   The arguments needed is
    * The title of the message box
    * Body of the message box
    
   The return is the awnser of what the user pressed. The MEssage box closes itself when 
   the selection has been done.
   
   https://docs.python.org/3/library/tkinter.messagebox.html
 
 * tk.Toplevel for a completely new window
   You use the toplevel widget just like you do the the ordinary window.

"""
import tkinter as tk
from tkinter import ttk, messagebox


# Setup
window = tk.Tk()
window.title("Multiple windows")
window.geometry("600x400")

# Command functions
def ask_yes_no():
    awnser = messagebox.askyesno(
        title="Create?",
        message="Do you want to create a message box?"
        )

    print(awnser)
    
    
class ExtraWindow(tk.Toplevel):
    
    def __init__(self, title, window_size):
        
        super().__init__()
        
        self.title(title)
        self.geometry(window_size)
        

    def run(self):
        ttk.Label(self, text="A Label CLASS").pack()
        ttk.Button(self, text="A Button CLASS").pack()
        ttk.Label(self, text="Another Label CLASS").pack(expand=True)


def create_window():
    global extra_window
    extra_window = tk.Toplevel()
    extra_window.title("Extra window")
    extra_window.geometry("300x400")
    
    ttk.Label(extra_window, text="A Label").pack()
    ttk.Button(extra_window, text="A Button").pack()
    ttk.Label(extra_window, text="Another Label").pack(expand=True)


def close_window():
    extra_window.destroy()
    
    
def create_window2():
    global ext
    ext = ExtraWindow("Extra window", "300x400")

    ext.run()
    
def close_window2():
    ext.destroy()
    
# Widgets
button1 = ttk.Button(window, text="Open main dialog", command=create_window)
button1.pack(expand=True)

button2 = ttk.Button(window, text="Close main dialog",  command=close_window)
button2.pack(expand=True)




button3 = ttk.Button(window, text="Open class window",  command=create_window2)
button3.pack(expand=True)

button4 = ttk.Button(window, text="Destroy class window",  command=close_window2)
button4.pack(expand=True)

button5 = ttk.Button(
    window, 
    text="create yes no dialog",
    command=ask_yes_no
    )

button5.pack(expand=True)


# Run
window.mainloop()