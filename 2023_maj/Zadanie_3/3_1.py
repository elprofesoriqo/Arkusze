ilosc=0
dane=[]
liczby =[]
with open("pi.txt") as plik:
    for row in plik:
        row= row.strip()
        dane.append(row)

    for i in range(0,len(dane)-1):
        liczby.append(int(f"{dane[i]}{dane[i+1]}"))


    for i in liczby:
        if str(i)[0]=='0':
            # ilosc+=1
            pass
        elif i>90:
            ilosc+=1
        

print(ilosc)