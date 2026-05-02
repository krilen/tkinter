"""
 PACK and FRAMES
========================

Pack with frame to create a complicated layout.


"""

import tkinter as tk
from tkinter import ttk


# Setup
window = tk.Tk()
window.title("Pack and Frame complex layout")
window.geometry("400x600")

### Widgets
# Top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text="First label", background="red")
label2 = ttk.Label(top_frame, text="Label 2", background="blue")

# Middle widget
label3 = ttk.Label(window, text="Another label", background="green")

# Bottom frame
bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text="Last of labels", background="orange")
button1 = ttk.Button(bottom_frame, text="A Button")
button2 = ttk.Button(bottom_frame, text="Another Button")

# Exercise frame
exercise_frame = ttk.Frame(bottom_frame)
button3 = ttk.Button(exercise_frame, text="Button 3")
button4 = ttk.Button(exercise_frame, text="Button 4")
button5 = ttk.Button(exercise_frame, text="Button 5")

### Layout
# Top layout
label1.pack(side="left", fill="both", expand=True)
label2.pack(side="left", fill="both", expand=True)
top_frame.pack(fill="both", expand=True)

# Middle layout
label3.pack(expand=True)

# Botton layout
button1.pack(side="left", expand=True, fill="both")
label4.pack(side="left", expand=True, fill="both")
button2.pack(side="left", expand=True, fill="both")

# Exercise layout
button3.pack(expand=True, fill="both")
button4.pack(expand=True, fill="both")
button5.pack(expand=True, fill="both")
exercise_frame.pack(side="left",expand=True, fill="both")

# Botton layout frame
bottom_frame.pack(expand=True, fill="both", padx=20, pady=20)

# Run
window.mainloop()