
brzeg=[]
wnetrze=0

with open("punkty.txt") as plik:
    for row in plik:
        row = row.strip()
        x,y = row.split(" ")
        x,y=int(x), int(y)
        a,b=200,200
        if pow(x-a,2) + pow(y-b,2) == pow(200,2):
            brzeg.append({x,y})
        elif  pow(x-a,2) + pow(y-b,2) < pow(200,2):
            wnetrze+=1

print(f"Brzeg {brzeg} \n Wnętrze: {wnetrze}")