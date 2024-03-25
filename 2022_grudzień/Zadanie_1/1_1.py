


ilosc_roznych=0


with open("mecz.txt") as file:
    for row in file:
        row=row.strip()

        for i in range(1,len(row)):
            if row[i] != row[i-1]:
                ilosc_roznych+=1

print(ilosc_roznych)