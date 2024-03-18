def klucz(wyr1, wyr2):
    for i in range(len(wyr1)):
        if ord(wyr2[i]) - ord(wyr1[i]) != ord(wyr2[0]) - ord(wyr1[0]):
            return True
    return False




with open("dane_6_3.txt") as plik:
    for row in plik:
        wyr1, wyr2= map(str, row.strip().split(" "))
        with open("wyniki_6_3.txt", "a") as wyniki:
            if klucz(wyr1, wyr2):
                wyniki.write(f"{wyr1}\n")
