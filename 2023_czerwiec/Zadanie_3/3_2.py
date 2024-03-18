def ilosc_anagramow(liczba: str) ->int:
    il_1=0
    il_0=0
    for cyfra in liczba:
        if cyfra=='1':
            il_1+=1
        else:
            il_0+=1


    return (sil(il_0+il_1-1))/(sil(il_1-1)*sil(il_0))



def sil(n: int) ->int:
    if n > 1:
        return n*sil(n-1)
    return 1

il={}
with open("anagram.txt") as file:
    for row in file:
        row=row.strip() 
        if len(row)==8:
            il[row]=ilosc_anagramow(row)



najwieksza_wartosc = max(il.values())

nazwa_najwiekszej = [klucz for klucz, wartosc in il.items() if wartosc == najwieksza_wartosc]



print("Największa wartość:", najwieksza_wartosc)
print("Nazwa największej wartości:", nazwa_najwiekszej)
