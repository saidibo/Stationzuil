from datetime import datetime
import random
""""
importeren van de modules
"""

"""
hier haal ik de datum en tijd op
"""
today = datetime.now()
date_time = today.strftime("%m/%d/%Y %H:%M:%S")




""""
een while loop zodat klanten hun gegevens en review kunnen invullen,
hier staat ook de lijst van de 3 steden met random.choice
"""
while True:
    station_lijst = ['Amsterdam', 'Utrecht', 'Rotterdam']
    keuzestation = list(random.choices(station_lijst, k=3))
    msg = str(input("Beste klant, wat is u ervaring: "))
    msg_naam = str(input("Wat is u naam? "))
    if msg_naam == "":
        msg_naam = "anoniem"
    if len(msg) > 140:
        print("u bericht is te lang.")
    elif msg_naam.lower() == 'stop':
        break



    else:
        informatie = (f"{msg_naam},{msg},{str(today)},{keuzestation[0]}\n")
        print(informatie)
        file = open("opmerkingen.csv", 'a')
        file.write(informatie)
        file.close()

