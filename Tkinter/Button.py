from tkinter import *


root = Tk()


root.geometry('100x100')


btn = Button(root, text='Click me !', bd='5',
             command=root.destroy)

# Set the position of button on the top of window.
btn.pack(side='top')

root.mainloop()