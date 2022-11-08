import psycopg2 as db
from datetime import datetime as dt
conn = db.connect(
    host = 'localhost',
    user = 'postgres',
    database = 'nszuil',
    password = 'admin'
)
"""
connectie met de database, en alle modules geimporteerd die ik nodig heb.
"""
point = conn.cursor()


"""
mod naam, mod email en mod tijd.
"""
mod_name = str(input('Voer u naam in:\n'))
mod_email = str(input('Voer u mail adres in:\n'))
mod_time = dt.now()
date_time = mod_time.strftime("%m/%d/%Y %H:%M:%S")


bestand = open("opmerkingen.csv", "r")

"""
for-loop die de database leest, en door middel van een goedkeuring [ja, JA, Ja].
"""

for lines in bestand.readlines():
    lines = lines.strip('\n')
    print(lines)
    lines = lines.split(',')

    opmerking = input("wilt u het bericht goedkeuren? ")
    if opmerking in ['ja', "JA", 'Ja', 'jA']:
        keuring = 'TRUE'
    else:
        keuring = "FALSE"


    "query die de values toevoegd aan de database"
    point.execute(f"INSERT INTO opmerkingen(naam, bericht, datetime, station, keuring) VALUES "
                  f"('{lines[0]}', '{lines[1]}', '{lines[2]}', '{lines[3]}', {keuring});")

    point.execute(f"INSERT INTO moderator(mod_name, mod_email, mod_time) VALUES ('{mod_name}', '{mod_email}', '{mod_time}')")

    conn.commit()

"""
bestand sluiten en pointer afsluiten.
"""
print(f'bedankt en tot ziens {mod_name}!')
point.close()
bestand.close()



"""

deze code is gemaakt door de heer Said Ebrahimin
© 
"""