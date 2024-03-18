def licz(liczba: str) ->list:
    il_1=0
    il_0=0
    for cyfra in liczba:
        if cyfra=='1':
            il_1+=1
        else:
            il_0+=1
    return {"jedynki": il_1, "zera": il_0}


zrownowazone=0
prawie=0
with open("anagram.txt") as file:
    for row in file:
        ilosc=licz(row.strip())
        if ilosc["jedynki"] == ilosc["zera"]:
            zrownowazone+=1
        elif abs(ilosc["jedynki"] - ilosc["zera"])==1:
            prawie+=1
print(f"Ilość liczb zrównowazonych: {zrownowazone}\n Ilość liczb prawiezrównoważonych: {prawie}")