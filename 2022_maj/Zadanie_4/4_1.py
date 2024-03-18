

dane=[]
with open("ips.txt") as file:
    for row in file:
        row=row.strip()
        dane.append(row.split(";")[0])
        # print(dane)
dane.pop(0)
waga=[1,3,7,9,1,3,7,9,1,3]

k={}
for row in dane:
    sk=0
    for i in range(9):
        sk+=int(row[i])*waga[i]
    if sk%10==0:
        k[row]=0
    else:
        k[row]=abs((sk%10)-10)

ilosc=0
for klucz, wartosc in k.items():
    ostatnia_cyfra_klucza = int(klucz[-1])  # Pobieranie ostatniej cyfry z klucza
    if ostatnia_cyfra_klucza != wartosc:
        ilosc+=1


print(ilosc)