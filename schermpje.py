from tkinter import *
root = Tk()
#tkinter scherm importeren
import psycopg2 as db
#DB zuil inporteren voor zo nodig....
# import requests
# # import request
# resource_uri = "http://api.openweathermap.org/geo/1.0/zip?zip={3085},{14}&appid={623674843eb5b413c214a36bad8eefdc}"
# response = requests.get(resource_uri)
# response_data = response.json()
# for key in response_data.keys():
#     print(f"{key}: {response_data[key]}")




conn = db.connect(
    host = 'localhost',
    user = 'postgres',
    database = 'nszuil',
    password = 'admin'
)

cur = conn.cursor()

tekst = cur.execute(f'select * from opmerkingen WHERE keuring = TRUE order by random() limit 10;')

rij = cur.fetchall()

for r in rij:
    print(r)
    info = (f'de heer {r[1]} zei: {r[2]}. in de plaats {r[3]}')



label = Label(master=root,
              text= info,
              background='yellow',
              foreground='blue',
              font=('Arial', 16, 'bold italic'),
              width=60,
              height=20
              )

label.pack()

root.mainloop()


conn.commit()
cur.close()
