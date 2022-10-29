from tkinter import *

root = Tk()
root.geometry("300x200")

w = Label(root, text='ALERT', font="50")
w.pack()

msg = Message(root, text="Your Item's value has been calculated!")

msg.pack()

root.mainloop()