def brak_0(liczba: str) ->int:
    if not '0' in str(int(liczba,2)):
        return 1
    return 0



def suma_roznych_cyfr(liczba: str):
    s=0
    liczba= int(liczba,2)
    cyfry=[]
    while liczba>0:
        if not (liczba % 10) in cyfry: 
            cyfry.append(liczba % 10)
            s+=(liczba % 10)
        liczba//=10
    return s


ilosc_bez_0=0
zadb={}
with open("anagram.txt") as file:
    for row in file:
        row=row.strip() 
        ilosc_bez_0+=brak_0(row)  
        zadb[int(row,2)]=suma_roznych_cyfr(row)



najwieksza_wartosc = max(zadb.values())

nazwa_najwiekszej = [klucz for klucz, wartosc in zadb.items() if wartosc == najwieksza_wartosc][0]


print(f"Ilość bez 0: {ilosc_bez_0}")
print("Największa wartość:", najwieksza_wartosc)
print("Nazwa największej wartości:", nazwa_najwiekszej)

