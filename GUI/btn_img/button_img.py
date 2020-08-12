from tkinter import *
from tkinter import ttk        
    
window = Tk()

button = ttk.Button(window, text = "Click Me")
button.pack()

def callback():
    print('Clicked')

button.config(command = callback)



logo = PhotoImage(file = 'python tkinter.gif')
button.config(image = logo, compound = LEFT)
small_logo = logo.subsample(5, 5)
button.config(image = small_logo)

window.mainloop()
