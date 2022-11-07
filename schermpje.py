from tkinter import *
root = Tk()
root['bg'] = '#f7d117'
import psycopg2 as db
from weer import rek_api, rek_icon
from tkinter import ttk

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
row = cur.fetchall()



'''sluiten van de database'''
# conn.commit()

img_toilet = PhotoImage(file='img_toilet.png')
img_lift = PhotoImage(file='img_lift.png')
img_ovfiets = PhotoImage(file='img_ovfiets.png')
img_pr = PhotoImage(file='img_pr.png')



rij = 0
for r in row:
    rij += 1
    cur.execute(f"SELECT * FROM station_service WHERE station_city = '{r[3]}';")
    voorziening = cur.fetchall()
    voorziening = voorziening[0]
    station_city, country, ov_bike, elevator, toilet, park_and_ride = voorziening

    info = (f'{r[1]} schreef: "{r[2]}" op het station in {r[3]}')


    plek = 0
    if elevator:
        my_label = Label(root, image=img_lift, bg='#003082')
        my_label.grid(column=plek, row=rij, columnspan=1, sticky=E)
        plek = plek + 1
    if ov_bike:
        my_label = Label(root, image=img_ovfiets, bg='#003082')
        my_label.grid(column=plek, row=rij, columnspan=1, sticky=E)
        plek = plek + 1
    if toilet:

        my_label = Label(root, image=img_toilet, bg='#003082')
        my_label.grid(column=plek, row=rij, columnspan=1, sticky=E)
        plek = plek + 1
    if park_and_ride:
        my_label = Label(root, image=img_pr, bg='#003082')
        my_label.grid(column=plek, row=rij, columnspan=1, sticky=E)
        plek = plek + 1

    plek = 0

    label = Label(root,
                  text=info,
                  bg = '#f7d117',
                  foreground='blue',
                  font=('Arial', 14, 'bold italic'),
                  width=70,
                  height=1,
                  )
    label.grid(column=4, row=rij, columnspan=1, sticky=W)
    separator = ttk.Separator(
        master=root,
        orient='horizontal',
    )
    separator.grid(row=rij, column=4, ipadx=430, pady=10, sticky=S)


"""hier importeer ik de png bestanden in de tkinter scherm"""
img_NS = PhotoImage(file='NS_logo2.png')
my_label = Label(root, image=img_NS, bg='#f7d117')
my_label.grid(column=6, row=0, sticky=NW)

cur.close()



vb_image = PhotoImage(file=f'weer_icon/{rek_icon()}@2x.png')
"""de celcius aanroepen op het scherm"""
test = Label(root,
                text= f'{rek_api()}',
                bg = '#89CFF0',
                fg='black',
                width=200,
                font=('Arial', 30, 'bold italic'),
                height=150,
                image= vb_image,
                compound='bottom'
                )
test.grid(column=0, row=0, columnspan=1, sticky=NE)

"""eindigen van de container"""
root.mainloop()

