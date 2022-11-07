# import tkinter as tk
# from tkinter import messagebox as tkmessagebox
#
# top = tk.Tk()
#
# def helloCallBack():
#    tkmessagebox.showinfo( "Hello Python", "Hello World")
#
# B = tk.Button(top, text ="Hello", command = helloCallBack)
#
# B.pack()
# top.mainloop()

from tkinter import *
from tkinter import messagebox

# creating window object
top = Tk()


def Button_1():
    messagebox.showinfo("Status",
                        "Button-1 Pressed")


def Button_2():
    messagebox.showinfo("Status",
                        "Button-2 Pressed")


# size for window
top.geometry("1000x1000")
B1 = Button(top, text=f"Button-1",
            command=Button_1)
B2 = Button(top, text="Button-2",
            command=Button_2)

B1.pack()
B2.pack()
top.mainloop()