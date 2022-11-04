from PIL import Image,ImageTk
from tkinter import *
from weer import rek_icon
from tkinter import filedialog
root=Tk()
text = Text(root)
text.pack()
#Insert Image

yourImage=rek_icon()
#imgFile=Image.open(yourImage)
imgToInsert=ImageTk.PhotoImage(file=f'{yourImage}@2x.png)

text.image_create("current",image=imgToInsert)
root.mainloop()