"""alle modules die nodig zijn importeren"""
from tkinter import *
root = Tk()
root['bg'] = 'yellow'
import psycopg2 as db
from weer import rek_api, rek_icon
from PIL import ImageTk, Image
#resize

"""connectie met de database"""
conn = db.connect(
    host = 'localhost',
    user = 'postgres',
    database = 'nszuil',
    password = 'admin'
)

'''cursur voor de database'''
cur = conn.cursor()

'''selectie van de laatste 5 berichten in de database'''
cur.execute(f'SELECT * FROM opmerkingen '
                    f'WHERE keuring = TRUE '
                    f'ORDER BY id DESC LIMIT 5;')
rij = cur.fetchall()



'''sluiten van de database'''
conn.commit()
cur.close()

for r in rij:
    info = (f'{r[1]} schreef: "{r[2]}" op het station in {r[3]}')
    label = Label(root,
                  text=info,
                  bg = 'yellow',
                  foreground='blue',
                  font=('Arial', 15, 'bold italic'),
                  width=70,
                  height=1
                  )
    label.pack(ipady=20, ipadx=20)

"""hier importeer ik de png bestanden in de tkinter scherm"""




my_img = PhotoImage(file=f'img_ovfiets.png')
my_label = Label(root, image=my_img)
my_label.pack()
#
# my_img2 = PhotoImage(file='img_lift.png')
# my_label2 = Label(root, image=my_img2)
# my_label2.grid(row=1, column=0)
#
# my_img3 = PhotoImage(file='img_toilet.png')
# my_label3 = Label(root, image=my_img3)
# my_label3.grid(row=2, column=0)
vb_image = PhotoImage(file=f'weer_icon/{rek_icon()}@2x.png')
"""de celcius aanroepen op het scherm"""
test = Label(root,
                text= f'{rek_api()}',
                bg = '#89CFF0',
                fg='black',
                width=200,
                font=('Arial', 30, 'bold italic'),
                height=190,
                image= vb_image,
                compound= 'bottom'
                )
test.pack()

"""eindigen van de container"""
root.mainloop()

