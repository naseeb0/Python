from tkinter import *
# behaviour 1
t1 = Tk()
t1.b = Button(t1, text = "push me",
    command = lambda:t1.b.destroy())
t1.geometry('500x500')
t1.b.pack()
t1.mainloop()
# behaviour 2
t2 = Tk()
t2.b = Button(t2, text = "me too!",
    command = lambda:t2.b.quit())
t2.geometry('500x500')
t2.b.pack()
t2.mainloop()
