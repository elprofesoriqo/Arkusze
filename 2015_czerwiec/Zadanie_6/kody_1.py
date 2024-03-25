
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


with open("kody.txt") as plik:
    for row in plik:
        row = row.strip() 
        sp=0
        snp=0
        sp=suma_p(row)
        snp=suma_np(row)

        with open("kody1.txt", "a") as wynik:
            wynik.write(f"{str(sp)} {str(snp)}\n")