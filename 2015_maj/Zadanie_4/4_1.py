ilosc=0


with open("liczby.txt") as plik:
    for row in plik:
        zera=0
        jedynki=0
        row = row.strip()
        for i in row:
            if i == '0':
                zera+=1
            else:
                jedynki+=1
        if zera>jedynki:
            ilosc+=1


with open("wynik4.txt", "a") as wyniki:
    wyniki.write(f"Zadanie 1:\nIlość: {str(ilosc)}\n")

