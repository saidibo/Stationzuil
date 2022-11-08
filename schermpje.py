from tkinter import *
root = Tk()
root['bg'] = '#f7d117'
import psycopg2 as db
from weer import rek_api, rek_icon
from tkinter import ttk
""""
alle modules geimporteerd
"""



"""
connectie met de database
"""
conn = db.connect(
    host = 'localhost',
    user = 'postgres',
    database = 'nszuil',
    password = 'admin'
)

'''
cursur voor de database
'''
cur = conn.cursor()

'''selectie van de laatste 5 berichten in de TABLE opmerkingen door middel van de onderstaande query'''
cur.execute(f'SELECT * FROM opmerkingen '
                    f'WHERE keuring = TRUE '
                    f'ORDER BY id DESC LIMIT 5;')

""""
variabelen voor de fetchall die ik vervolgens in een for-loop zal gebruiken
"""
row = cur.fetchall()


""""
foto's door middel van een variabele die ik in een for-loop zal gebruiken
"""
img_toilet = PhotoImage(file='img_toilet.png')
img_lift = PhotoImage(file='img_lift.png')
img_ovfiets = PhotoImage(file='img_ovfiets.png')
img_pr = PhotoImage(file='img_pr.png')

""""
een functie weer met als city 1 van de 3 steden
"""
def weer(city):

    vb_image = PhotoImage(file=f'weer_icon/{rek_icon(city)}@2x.png')

    """de celcius aanroepen op het scherm"""
    weervoorspelling = Label(root,
                 text=f'{rek_api(city)}',
                 bg='#89CFF0',
                 fg='black',
                 relief = 'raised',
                 width=200,
                 font=('Arial', 30, 'bold italic'),
                 height=150,
                 image=vb_image,
                 compound='bottom'
                 )
    weervoorspelling.img = vb_image

    weervoorspelling.grid(column=0, row=0, columnspan=1, sticky=NE)

""""
knopjes voor de steden, zodat je de temp in celcius kunt zien op de locaties
"""

weer_button_ams = ttk.Button(root, text="Amsterdam", command=lambda: weer('amsterdam'))
weer_button_ams.grid(row=0, column=1, sticky=NE)

weer_button_ams = ttk.Button(root, text="Utrecht", command=lambda: weer("utrecht"))
weer_button_ams.grid(row=0, column=2, sticky=NE)

weer_button_ams = ttk.Button(root, text="Rotterdam", command=lambda: weer('rotterdam'))
weer_button_ams.grid(row=0, column=3, sticky=NE)

""""
een for-loop zodat ik door middel van de bovenstaande query kan selecteren op naam, bericht, locatie
hierdoor krijg ik een for-loop met een maximale lengte van 5 zinnen.
dit doordat de query ORDER BY DESC limit 5 heeft staan
"""

rij = 0
for r in row:
    rij += 1
    cur.execute(f"SELECT * FROM station_service WHERE station_city = '{r[3]}';")
    voorziening = cur.fetchall()
    voorziening = voorziening[0]
    station_city, country, ov_bike, elevator, toilet, park_and_ride = voorziening

    info = (f'{r[1]} schreef: "{r[2]}" op het station in {r[3]}')

    """
    de foto's invoegen in de tkinter met als positie column+=plek en row=rij.
    hierdoor word de column elke keer verschoven met = 1 door elke foto
    """
    plek = 0
    if elevator:
        my_label = Label(root, image=img_lift, relief='sunken', bg='#003082')
        my_label.grid(column=plek, row=rij, columnspan=1, sticky=E)
        plek = plek + 1
    if ov_bike:
        my_label = Label(root, image=img_ovfiets, relief='sunken', bg='#003082')
        my_label.grid(column=plek, row=rij, columnspan=1, sticky=E)
        plek = plek + 1
    if toilet:

        my_label = Label(root, image=img_toilet,relief='sunken', bg='#003082')
        my_label.grid(column=plek, row=rij, columnspan=1, sticky=E)
        plek = plek + 1
    if park_and_ride:
        my_label = Label(root, image=img_pr,relief='sunken' , bg='#003082')
        my_label.grid(column=plek, row=rij, columnspan=1, sticky=E)
        plek = plek + 1

    plek = 0
    """
    hier word de bericht op tkinter laten zien. 
    met naam, bericht en locatie.
    ook word er een seperator gebruikt die de zinnen aan elke einde scheid zodat het een mooiere structuur heeft.
    """
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


"""
NS logo in tkinter
"""
img_NS = PhotoImage(file='NS_logo2.png')
my_label = Label(root, image=img_NS, relief='sunken', bg='#f7d117')
my_label.grid(column=6, row=0, sticky=NW)





"""
eindigen van de container
"""
cur.close()
root.mainloop()

