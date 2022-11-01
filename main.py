from datetime import datetime
import random


today = datetime.now()
date_time = today.strftime("%m/%d/%Y %H:%M:%S")
station_lijst = ['Arnhem', 'Almere', 'Amersfoort', 'Almelo', 'Alkmaar', 'Apeldoorn', 'Assen', 'Amsterdam', 'Boxtel', 'Breda', 'Dordrecht', 'Delft', 'Deventer', 'Enschede','Gouda','Groningen', 'Den Haag', 'Hengelo', 'Haarlem', 'Helmond', 'Hoorn', 'Heerlen', 'Den Bosch', 'Hilversum', 'Leiden', 'Lelystad', 'Leeuwarden', 'Maastricht', 'Nijmegen', 'Oss', 'Roermond', 'Roosendaal', 'Sittard', 'Tilburg', 'Utrecht','Venlo','Vlissingen','Zaandam','Zwolle','Zutphen']
keuzestation = list(random.choices(station_lijst, k=3))


while True:
    msg_naam = str(input("Wat is u naam? "))
    msg = str(input("Beste klant, wat is u ervaring: "))

    if msg_naam == "":
        msg_naam = "anoniem"
    if len(msg) > 140:
        print("u bericht is te lang.")



    else:
        informatie = (f"{msg_naam},{msg},{str(today)},{keuzestation[0]}\n")
        print(informatie)
        file = open("opmerkingen.csv", 'a')
        file.write(informatie)
        file.close()

