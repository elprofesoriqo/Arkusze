

def znjadz(a,b):
    liczba=b//2
    while liczba>=a:
        if a==liczba:
            return True
        if a-1==liczba:
            return True
        liczba//=2
    return False


pary=[]

with open("pary.txt") as file:
    for row in file:
        row=row.strip()

        a,b = row.split(" ")
        if znjadz(int(a),int(b)):
            pary.append([a,b])
print(pary)