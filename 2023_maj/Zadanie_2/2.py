def liczba_blokow(binarna):
    bloki = []
    aktualny_blok = binarna[0]

    for cyfra in binarna[1:]:
        if cyfra == aktualny_blok[-1]:
            aktualny_blok += cyfra
        else:
            bloki.append(aktualny_blok)
            aktualny_blok = cyfra

    bloki.append(aktualny_blok)
    return bloki



with open('bin.txt', 'r') as plik:
    liczby_binarne = plik.read().splitlines()

    liczba_mniejsza_niz_dwa_bloki = 0
    maks=int(liczby_binarne[0], 2)
    for liczba_binarna in liczby_binarne:
        liczba = int(liczba_binarna, 2)
        if liczba>maks:
            maks=liczba
        bloki = liczba_blokow(liczba_binarna)
        if len(bloki) <= 2:
            liczba_mniejsza_niz_dwa_bloki += 1




    print(f"Liczba liczb składających się z co najwyżej dwóch bloków: {liczba_mniejsza_niz_dwa_bloki} \n Największa liczba: {bin(maks)}")


