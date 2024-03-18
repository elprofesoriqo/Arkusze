przez2=0
przez8 =0

with open("liczby.txt") as plik:
    for row in plik:
        row=row.strip()
        if int(row,2)%2==0:
            przez2+=1
        if int(row,2)%8==0:
            przez8+=1

with open("wynik4.txt", "a") as wyniki:
    wyniki.write(f"Zadanie 2:\nIlość podzielnych przez 2: {str(przez2)}\nilosc podzielnych przez 8: {str(przez8)}\n")

