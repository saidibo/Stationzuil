go_bericht = open("goedkeuring.txt", "a")
bericht = open("review.txt", "r")
afgekeurd = open("afgekeurd.txt", 'a')


for lines in bericht.readlines():

    go_bericht = open("goedkeuring.txt", 'a')
    bericht = open("review.txt", 'r')
    afgekeurd = open("afgekeurd.txt", 'a')
    print(lines)
    opmerking = input("wilt u het bericht goedkeuren?")

    if opmerking == 'ja' or opmerking == 'Ja' or opmerking == 'JA':
        print("oke het bericht is goedgekeurd")
        go_bericht.write(lines)
        bericht = open("review.txt", 'w')

    else:
        afgekeurd = open("afgekeurd.txt", 'a')
        afgekeurd.write(lines)

        print('bericht is afgekeurd en verwijderd.')

go_bericht.close()
bericht.close()
afgekeurd.close()