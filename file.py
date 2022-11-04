#import tkinter as tk
# root = tk.Tk()
# test = tk.Label(root,
#                 text=info,
#                 bg = 'yellow',
#                 fg = 'black',
#                 width=50,
#                 height=10
#                 )
# test.pack(ipadx=30, ipady=6)
# test = tk.Label(root,
#                 text=rek_api(),
#                 bg = 'yellow',
#                 fg='black',
#                 width=50,
#                 height=10
#                 )
# test.pack(ipadx=6, ipady=12)
# tk.mainloop()




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




import psycopg2 as db

conn = db.connect(
    host = 'localhost',
    user = 'postgres',
    database = 'nszuil',
    password = 'admin'
)


cur = conn.cursor()

info = cur.execute(f'SELECT * FROM station_service '
                    f'WHERE ov_bike = TRUE '
                   f'AND elevator = TRUE '
                   f'AND toilet = TRUE '
                   f'AND park_and_ride = TRUE'
                   f';')
rij = cur.fetchall()

for r in rij:
    print()

print(rij)
conn.commit()
cur.close()