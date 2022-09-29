import datetime

print("dit is de Station zuil project")



msg_naam = str(input("Wat is u naam? "))
msg = str(input("Beste klant, wat is u ervaring: "))
today = datetime.datetime.now()
date_time = today.strftime("%m/%d/%Y, %H:%M:%S ")

info = msg_naam, msg, date_time

if msg_naam == "":
    msg_naam = "anoniem"
elif msg_naam:
    msg_naam == msg_naam

if len(msg) > 140:
    print("u bericht is te lang.")



else:
    None


print(info)


