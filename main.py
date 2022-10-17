from datetime import datetime


msg_naam = str(input("Wat is u naam? "))
msg = str(input("Beste klant, wat is u ervaring: "))
today = datetime.now()
date_time = today.strftime("%m/%d/%Y %H:%M:%S")


if msg_naam == "":
    msg_naam = "anoniem"
if len(msg) > 140:
    print("u bericht is te lang.")



else:
    informatie = (f"{msg_naam}|'{msg}'|{str(today)}\n")
    file = open("review.txt", 'a')
    file.write(informatie)
    file.close()
    print(informatie)

