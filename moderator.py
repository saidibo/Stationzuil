import psycopg2 as db

conn = db.connect(
    host = 'localhost',
    user = 'postgres',
    database = 'nszuil',
    password = 'admin'
)

point = conn.cursor()



mod_name = str(input('Voer u naam in: '))

bestand = open("opmerkingen.csv", "r")


for lines in bestand.readlines():
    lines = lines.strip('\n')
    print(lines)
    lines = lines.split(',')

    opmerking = input("wilt u het bericht goedkeuren? ")
    if opmerking in ['ja', "JA", 'Ja', 'jA']:
        keur = 'TRUE'
    else:
        keur = "FALSE"



    point.execute(f"INSERT INTO opmerkingen(naam, bericht, datetime, station, mod_naam, keuring) VALUES ('{lines[0]}', '{lines[1]}', '{lines[2]}', '{lines[3]}', '{mod_name}', {keur});")

    conn.commit()

point.close()
bestand.close()
