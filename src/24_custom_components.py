"""
 CUSTOM COMPONENTS WITH CLASSES AND FUNCTIONS
========================
You need to create you own components to be efficient.

Using classes a custom widgets gets created.

There are 2 ways of creating custom components
 * Using classes
   You inherit from a widget and add custom parts.
   You are able to create complex layouts
   But you can end up with a lot of classes
 * Functional
   Create a widget in a function and return it.
   It limits the layouts
   But is is easier to organise when creating smaller components.
   
   

"""

import tkinter as tk
from tkinter import ttk


class Segment(ttk.Frame):
    
    def __init__(self, parent, label_text, button_text, exercise_text):
        
        super().__init__(parent)
        
        # Grid layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1,2), weight=1, uniform="a")
        
        # Widgets
        ttk.Label(self, text=label_text).grid(row=0, column=0, sticky="nswe")
        ttk.Button(self, text=button_text).grid(row=0, column=1, sticky="nswe")
        self.create_exercise_box(exercise_text).grid(row=0, column=2, sticky="nswe")
        
        self.pack(expand=True, fill="both", padx=10, pady=10)
        
        
    def create_exercise_box(self, text):
        frame = ttk.Frame(self)
        
        ttk.Entry(frame).pack(expand=True, fill="both")
        ttk.Button(frame, text=text).pack(expand=True, fill="both")
        
        return frame


def create_segment(parent, label_text, button_text):
    
    frame = ttk.Frame(parent)
    
    # Grid layout
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure((0,1,2), weight=1, uniform="a")
    
    # Widgets
    ttk.Label(frame, text=label_text).grid(row=0, column=0, sticky="nswe")
    ttk.Button(frame, text=button_text).grid(row=0, column=1, sticky="nswe")

    return frame

if __name__ == "__main__":
    
    # Window
    window = tk.Tk()
    window.title("Widgets and return")
    window.geometry("400x600")
    
    # Widgets - class
    Segment(window, "label", "button", "exercise 1")
    Segment(window, "test", "click", "exercise 2")
    Segment(window, "hello", "world", "exercise 3")
    Segment(window, "hi", "goodbye", "exercise 4")
    Segment(window, "final", "last one", "exercise 5")
    
    # Widget - functional
    # create_segment(window, "label", "button").pack(expand=True, fill="both", padx=10, pady=10)
    # create_segment(window, "test", "click").pack(expand=True, fill="both", padx=10, pady=10)
    # create_segment(window, "hello", "world").pack(expand=True, fill="both", padx=10, pady=10)
    # create_segment(window, "hi", "goodbye").pack(expand=True, fill="both", padx=10, pady=10)
    # create_segment(window, "final", "last one").pack(expand=True, fill="both", padx=10, pady=10)
    
    # Run
    window.mainloop()
