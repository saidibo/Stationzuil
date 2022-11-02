#tkinter scherm importeren
from tkinter import *
root = Tk()

#DB zuil inporteren voor zo nodig....
import psycopg2 as db

#rek_api functie aanroepen
from weer import rek_api

#for de foto's
from PIL import ImageTk, Image


#connectie met de database
conn = db.connect(
    host = 'localhost',
    user = 'postgres',
    database = 'nszuil',
    password = 'admin'
)

#cursur voor de database
cur = conn.cursor()

#selectie van de laatste 5 berichten in de database
tekst = cur.execute(f'SELECT * FROM opmerkingen WHERE keuring = TRUE order by ID DESC LIMIT 3;')
rij = cur.fetchall()

conn.commit()
cur.close()

#een for loop voor de laatste 5 berichten met tkinter erin
for r in rij:
    print(r)
    info = (f'de heer {r[1]} zei: {r[2]}. in de plaats {r[3]}')
    label = Label(master=root,
                  text=info,
                  background='yellow',
                  foreground='blue',
                  font=('Arial', 30, 'bold italic'),
                  width=80,
                  height=3
                  )

    label.pack()

#hier probeer ik een foto te importeren in tkinter
my_img = ImageTk.PhotoImage(Image(open('')))
my_label = label(image=my_img)
my_label.pack()


#de celcius aanroepen in tkinter
test = Label(root,
                text=rek_api(),
                bg = 'yellow',
                fg='black',
                width=80,
                font=('Arial', 30, 'bold italic'),
                height=10
                )
test.pack(ipadx=6, ipady=12)

#eindigen van tkinter.
root.mainloop()

