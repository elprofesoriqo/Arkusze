dane=[]
licznik = {}
liczby =[]
with open("pi.txt") as plik:
    for row in plik:
        row= row.strip()
        dane.append(row)

    for i in range(0,len(dane)-1):
        liczby.append(int(f"{dane[i]}{dane[i+1]}"))



    for element in set(liczby):
        licznik[element] = liczby.count(element)

    

print(licznik)
najmniejsza_wartosc = min(licznik.values())
najwieksza_wartosc = max(licznik.values())

nazwa_najmniejszej = [klucz for klucz, wartosc in licznik.items() if wartosc == najmniejsza_wartosc][0]
nazwa_najwiekszej = [klucz for klucz, wartosc in licznik.items() if wartosc == najwieksza_wartosc][0]

print("Najmniejsza wartość:", najmniejsza_wartosc)
print("Nazwa najmniejszej wartości:", nazwa_najmniejszej)

print("Największa wartość:", najwieksza_wartosc)
print("Nazwa największej wartości:", nazwa_najwiekszej)
