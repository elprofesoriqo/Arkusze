
def suma_np(n):
    snp=0
    for i in range(len(n)):
        if i%2==1:
            snp+=int(n[i])
        
    return snp



def suma_p(n):
    sp=0
    for i in range(len(n)):
        if i%2==0:
            sp+=int(n[i])
        
    return sp




kody={
    "0":	10101110111010,
    "1":	11101010101110,
    "2":	10111010101110,
    "3":	11101110101010,
    "4":	10101110101110,
    "5":	11101011101010,
    "6":	10111011101010,
    "7":	10101011101110,
    "8":	11101010111010,
    "9":	10111010111010
}



with open("kody.txt") as plik:
    for row in plik:
        row = row.strip() 
        sp=0
        snp=0
        sp=suma_p(row[::-1])
        snp=suma_np(row[::-1])

        kontrolna=0
        kontrolna=(10-(3*sp+snp)%10)%10

        kod=kody[f"{kontrolna}"]

        with open("kody2.txt", "a") as wynik:
            wynik.write(f"{str(kontrolna)} {kod}\n")