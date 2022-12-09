from tkinter import *
from tkinter import filedialog
import tkinter as tk

root = Tk()
root.geometry("500x500")
root.title('Price Estimator')
root.config(background = "light blue")
bgimg= tk.PhotoImage(file = r"C:\Users\Josh\Desktop\GitHub Repos\ML_Price_Estimator\images\sky.png")
limg= Label(root, i=bgimg)


w = Label(root, text='ML Price Estimator', font="50")
x = Label(root, text='Authors:')
y = Label(root, text='Joshua Konechy')
z = Label(root, text='Brent Pfefferle')
v = Label(root, text='Arifulla Shaik')


photo1 = PhotoImage(file=r"C:\Users\Josh\Desktop\GitHub Repos\ML_Price_Estimator\images\train.png")
photo2 = PhotoImage(file=r"C:\Users\Josh\Desktop\GitHub Repos\ML_Price_Estimator\images\test.png")
photo3 = PhotoImage(file=r"C:\Users\Josh\Desktop\GitHub Repos\ML_Price_Estimator\images\results.png")
# Resizing image to fit on button
photoimage1 = photo1.subsample(40, 40)
photoimage2 = photo2.subsample(11, 11)
photoimage3 = photo3.subsample(14, 14)


def Train():
    # Toplevel object which will be treated as a new window
    newWindow = Toplevel(root)

    # sets the title of the Toplevel widget
    newWindow.title("Train")

    # sets the geometry of toplevel
    newWindow.geometry("400x450")

    # A Label widget to show in toplevel
    Label(newWindow, text="Please Enter the Independent Variables ").pack()
    Label(newWindow, text="What are your dependent Variables? ").pack()

    x1 = Label(newWindow, text='X 1').pack()
    x1_value = StringVar()
    e1 = Entry(newWindow, textvariable=x1_value).pack()

    x2 = Label(newWindow, text='X 2').pack()
    x2_value = StringVar()
    e2 = Entry(newWindow, textvariable=x2_value).pack()

    x3 = Label(newWindow, text='X 3').pack()
    x3_value = StringVar()
    e3 = Entry(newWindow, textvariable=x3_value).pack()

    x4 = Label(newWindow, text='X 4').pack()
    x4_value = StringVar()
    e4 = Entry(newWindow, textvariable=x4_value).pack()

    x5 = Label(newWindow, text='X 5').pack()
    x5_value = StringVar()
    e5 = Entry(newWindow, textvariable=x5_value).pack()

    x6 = Label(newWindow, text='X 6').pack()
    x6_value = StringVar()
    e6 = Entry(newWindow, textvariable=x6_value).pack()

    x7 = Label(newWindow, text='X 7').pack()
    x7_value = StringVar()
    e7 = Entry(newWindow, textvariable=x7_value).pack()


    submitBtn = Button(newWindow, text="Submit", command=None, image=None, compound=LEFT).pack(pady=10, side=TOP)
    returnBtn = Button(newWindow, text="return", command=newWindow.destroy, image=None, compound=LEFT).pack(pady=10, side=TOP)
def Test():
    # Toplevel object which will be treated as a new window
    newWindow = Toplevel(root)

    # sets the title of the Toplevel widget
    newWindow.title("Test")

    # sets the geometry of toplevel
    newWindow.geometry("400x450")

    Label(newWindow, text="Please Enter the Independent Variables ").pack()
    Label(newWindow, text="What are your dependent Variables? ").pack()

    x1 = Label(newWindow, text='X 1').pack()
    x1_value = StringVar()
    e1 = Entry(newWindow, textvariable=x1_value).pack()

    x2 = Label(newWindow, text='X 2').pack()
    x2_value = StringVar()
    e2 = Entry(newWindow, textvariable=x2_value).pack()

    x3 = Label(newWindow, text='X 3').pack()
    x3_value = StringVar()
    e3 = Entry(newWindow, textvariable=x3_value).pack()

    x4 = Label(newWindow, text='X 4').pack()
    x4_value = StringVar()
    e4 = Entry(newWindow, textvariable=x4_value).pack()

    x5 = Label(newWindow, text='X 5').pack()
    x5_value = StringVar()
    e5 = Entry(newWindow, textvariable=x5_value).pack()

    x6 = Label(newWindow, text='X 6').pack()
    x6_value = StringVar()
    e6 = Entry(newWindow, textvariable=x6_value).pack()

    x7 = Label(newWindow, text='X 7').pack()
    x7_value = StringVar()
    e7 = Entry(newWindow, textvariable=x7_value).pack()

    submitBtn2 = Button(newWindow, text="Submit", command=None, image=None, compound=LEFT).pack(pady=10, side=TOP)
    returnBtn2 = Button(newWindow, text="return", command=newWindow.destroy, image=None, compound=LEFT).pack(pady=10, side=TOP)
def Results():
    # Toplevel object which will be treated as a new window
    newWindow = Toplevel(root)

    # sets the title of the Toplevel widget
    newWindow.title("Results")

    # sets the geometry of toplevel
    newWindow.geometry("400x400")

    # A Label widget to show in toplevel
    Label(newWindow, text="Here are your Results!").pack()
    Label(newWindow, text="----------Display Here----------- ").pack()

    returnBtn = Button(newWindow, text="return", command=newWindow.destroy, image=None, compound=LEFT).pack(pady=10, side=TOP)
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                            title="Select a File",
                                            filetypes=(("Text files",
                                                        "*.txt*"),
                                                        ("all files",
                                                        "*.*")))


#Change the feather icon in the corner
#https://www.geeksforgeeks.org/change-icon-for-tkinter-messagebox/


btnTrain = Button(root, text="Train", command=Train, image=photoimage1, compound=LEFT)
btnTest = Button(root, text="Test", command=Test, image=photoimage2, compound=LEFT)
btnResults = Button(root, text="Results", command=Results, image=photoimage3, compound=LEFT)

label_file_explorer = Label(root, text="Uplaod a .CSV file")
button_explore = Button(root,text="Browse Files", command=browseFiles)


menubar = Menu(root)
# Adding File Menu and commands
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New File', command=None)
file.add_command(label='Open...', command=None)
file.add_command(label='Save', command=None)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Cut', command=None)
edit.add_command(label='Copy', command=None)
edit.add_command(label='Paste', command=None)
edit.add_command(label='Select All', command=None)
edit.add_separator()
edit.add_command(label='Find...', command=None)
edit.add_command(label='Find again', command=None)

# Adding Help Menu
help_ = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help_)
help_.add_command(label='Tk Help', command=None)
help_.add_command(label='Demo', command=None)
help_.add_separator()
help_.add_command(label='About Tk', command=None)


root.config(menu = menubar)
w.pack()
x.pack()
y.pack()
z.pack()
v.pack()

btnTrain.pack(pady=10, side = TOP)
btnTest.pack(pady=10, side = TOP)
btnResults.pack(pady=10, side = TOP)
label_file_explorer.pack(pady=10, side = TOP)
button_explore.pack(pady=10, side = TOP)
limg.pack()
root.mainloop()