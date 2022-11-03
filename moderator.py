import psycopg2 as db
from datetime import datetime as dt
conn = db.connect(
    host = 'localhost',
    user = 'postgres',
    database = 'nszuil',
    password = 'admin'
)

point = conn.cursor()



mod_name = str(input('Voer u naam in:\n'))
mod_email = str(input('Voer u mail adres in:\n'))
mod_time = dt.now()


bestand = open("opmerkingen.csv", "r")

for lines in bestand.readlines():
    lines = lines.strip('\n')
    print(lines)
    lines = lines.split(',')

    opmerking = input("wilt u het bericht goedkeuren? ")
    if opmerking in ['ja', "JA", 'Ja', 'jA']:
        keuring = 'TRUE'
    else:
        keuring = "FALSE"



    point.execute(f"INSERT INTO opmerkingen(naam, bericht, datetime, station,"
                  f" mod_naam, keuring, mod_email, mod_time) VALUES "
                  f"('{lines[0]}', '{lines[1]}', '{lines[2]}', '{lines[3]}', '{mod_name}', {keuring}, '{mod_email}', '{mod_time}');")

    conn.commit()
print(f'bedankt en tot ziens {mod_name}!')
point.close()
bestand.close()
