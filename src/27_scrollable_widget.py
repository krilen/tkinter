"""
 SCROLLABLE WIDGET
========================

There is no built-in tool in Tkinter for scrolling but you can add scroll on a canvas and the
add widgets to the canvas.

To add a widget to the canvas you must use the method, 
'<canvas>.create_window((posX,posY), window=<widget>)'

After the widget has been added it is possible to add scrolling mechanic to the canvas.

This can get complex that is why to use a class to simplify.

The major thing is that you are not using the layout method on the canvas instead you could say
that you are drawing the windget in the canvas.

But because of this the size can not be set using the frame widget (width=200) or the pack mehhod
(expand=True). To set the height we need to set in on the widget that get added to the frame
(by using the a layout method)

The 'create_window' method ONLY tries to create a create a space so large to fit the content
(in the example below the frame) so we can set the space needed in it.



"""
import tkinter as tk
from tkinter import ttk


# # Setup
# window = tk.Tk()
# window.title("Scrollable widget")
# window.geometry("500x400")

# # Canvas
# canvas = tk.Canvas(window, background="white")
# canvas.create_window((30, 20),                              # position posX, posY on the canvas
#                      window = ttk.Label(canvas,             # "master" (parent) does not matter
#                                         text="A Label", 
#                                         background="white"))
# canvas.create_window((30, 60),
#                      window = ttk.Button(canvas,            # This widget does not be used by a
#                                          text="A Label",    # layout method
#                                          command=lambda: print("Hello")))
# canvas.pack(expand=True, fill="both")
# 
# # Run
# window.mainloop()

class ListFrame(ttk.Frame):
    
    def __init__(self,  parent, text_data, item_height):
        super().__init__(parent)
        self.pack(expand=True, fill="both")     # Simplest layout method
        
        # Widget data
        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height
    
    
    def run(self):
        self.create_canvas()
        self.create_frame()
        self.add_events()
        
    
    def create_canvas(self):
        self.canvas = tk.Canvas(
            self, 
            background="red", 
            scrollregion=(0,0,self.winfo_width(),self.list_height)
        )
        
        self.canvas.pack(expand=True, fill="both")


    def create_frame(self):
        # SIZE INFO
        # Using 'create_window' we draw the attaching widget in the case blow the frame
        # It is NOT possible to specify the frame or its layout method with a size / expand / ...
        # The canvas size is only as big as it is needed.
        # But we can set the size either
        #  * on the "label" that gets attached to the frame
        #  * or we can set the size of the canvas specifically
        #
        # But sice the "label" only has a 'width' argument and not a 'height' the easiest 
        # is to set the size on the canvas.
        
        self.frame = ttk.Frame(self)                    # Frame size DOES NOT matter
        #ttk.Label(self.frame, text="A label").pack()
        
        for i, item in enumerate(self.text_data, start=1):
            self.create_item(i, item).pack(
                expand=True, 
                fill="both", 
                pady=4, 
                padx=10,
                )

        # scrollbars
        #self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        #self.canvas.configure(yscrollcommand=self.scrollbar.set)
        #self.scrollbar.place(relx=1, rely=0, anchor="ne", relheight=1)

    def add_events(self):
        self.canvas.bind_all( # instead of just 'bind' we use 'bind_all' for all widgets
            "<MouseWheel>", # Windows Mousewheel
            lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units")
            )
        
        self.canvas.bind_all(
            "<Button-4>",   # Linux MouseWheel UP
            lambda event: self.canvas.yview_scroll(-2, "units")
            )
        
        self.canvas.bind_all(
            "<Button-5>",   # Linux MouseWheel Down
            lambda event: self.canvas.yview_scroll(2, "units")
            )
        
        self.bind("<Configure>", self.update_size)


    def remove_events(self):
        self.canvas.unbind_all("<MouseWheel>")
        self.canvas.unbind_all("<Button-4>")
        self.canvas.unbind_all("<Button-5>")


    def create_item(self, index, item):
        frame = ttk.Frame(self.frame)
 
        # Grid layout
        frame.rowconfigure(0, weight=1, uniform="a")
        frame.columnconfigure((0,1,2,3,4), weight=1, uniform="a")
                              
        # Widget
        ttk.Label(frame, text=f"#{index}").grid(row=0, column=0)
        ttk.Label(frame, text=f"{item[0]}").grid(row=0, column=1)
        ttk.Button(frame, text=f"{item[1]}").grid(row=0, column=2, columnspan=3, sticky="nswe")
        
        return frame


    def update_size(self, _):
        if self.list_height >= self.winfo_height():
            height = self.list_height
            self.add_events()
            self.add_scrollbars()
            
        else:
            height = self.winfo_height()
            self.remove_events()
            self.scrollbar.place_forget()
        
        self.canvas.create_window(
            (0,0),                      # Pos to place the frame
            window = self.frame,        # Where placement
            anchor="nw",                # Position
            width=self.winfo_width(),   # Get the width from the window itself
            height=height,
            )
    

    def add_scrollbars(self):
        
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(relx=1, rely=0, anchor="ne", relheight=1)

    
    
    





class App(tk.Tk):
    
    def __init__(self, title, window_size, test_list):
        # Setup
        super().__init__()
               
        self.title(title)
        self.geometry(window_size)

        self.text_list = test_list


    def run(self):
        
        list_frame = ListFrame(self, self.text_list, 100)
        list_frame.run()
        
        # Run
        self.mainloop()




if __name__ == "__main__":
    
    text_list = [("label", "button"),
                 ("thing", "click"),
                 ("label 2", "button 2"),
                 ("label three", "button three"),
                 ("Label 4", "B4"),
                 ("Last button", "Button Last")]
    
    app = App("Scrollable widget", "500x400", text_list)
    app.run()