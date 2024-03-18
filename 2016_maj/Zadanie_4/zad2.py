
wko=0
wkw=0
pi=0
dane=[]
with open("punkty.txt") as plik:
    for row in plik:
        row = row.strip()
        x,y = row.split(" ")
        x,y=int(x), int(y)
        a,b=200,200
        
        if  pow(x-a,2) + pow(y-b,2) < pow(200,2):
            wko+=1
            wkw+=1
        else:
            wkw+=1

    pi=round(((wko*160000)/wkw)/40000,4)
    print(f"Wszystkie punkty pi={pi}")














wko=0
wkw=0
pi=0
with open("punkty.txt") as plik:
    for i in plik:
        dane.append(i)
    
    dane= dane[:1000]
    for row in dane:
        row = row.strip()
        x,y = row.split(" ")
        x,y=int(x), int(y)
        a,b=200,200
        
        if  pow(x-a,2) + pow(y-b,2) <= pow(200,2):
            wko+=1
            wkw+=1
        else:
            wkw+=1

    pi=round(((wko*160000)/wkw)/40000,4)
    print(f"Pierwsze 1000 punktów pi={pi}")
wko=0
wkw=0
pi=0
dane=[]
with open("punkty.txt") as plik:
    for i in plik:
        dane.append(i)
    dane = dane[:5000]
    for row in dane:
        row = row.strip()
        x,y = row.split(" ")
        x,y=int(x), int(y)
        a,b=200,200
        
        if  pow(x-a,2) + pow(y-b,2) < pow(200,2):
            wko+=1
            wkw+=1
        else:
            wkw+=1

    pi=round(((wko*160000)/wkw)/40000,4)
    print(f"Pierwsze 5000 punktów pi={pi}")