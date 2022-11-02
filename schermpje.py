import tkinter as tk
#tkinter scherm importeren
import psycopg2 as db
#DB zuil inporteren voor zo nodig....
from weer import rek_api
import json


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


#
#
# label = Label(master=root,
#               text= lst,
#               background='yellow',
#               foreground='blue',
#               font=('Arial', 16, 'bold italic'),
#               width=60,
#               height=20
#               )
#
# label.pack()
#
# root.mainloop()


conn.commit()
cur.close()

root = tk.Tk()
test = tk.Label(root,
                text=info,
                bg = 'yellow',
                fg = 'black',
                width=50,
                height=10
                )
test.pack(ipadx=30, ipady=6)
test = tk.Label(root,
                text=rek_api(),
                bg = 'yellow',
                fg='black',
                width=50,
                height=10
                )
test.pack(ipadx=6, ipady=12)
tk.mainloop()

