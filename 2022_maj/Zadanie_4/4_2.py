def sito(n):
    pierwsze=[]
    tab = []
    for i in range(n+1):
       tab.append(0) 
    tab[0] = tab[1] = 1
    i = 2 
    while i*i <= n: 
        if tab[i] == 0:
            for j in range(i*i, n+1, i):
                tab[j] = 1 
        i += 1 

    for i in range(n + 1):
        if tab[i] == 0:
            pierwsze.append(int(i))
    return pierwsze


with open("liczby.txt") as file:
    for row in file:
        row=row.strip()
        pierwsze=[]
        pierwsze=sito(int(row))
     
        il=0
        for i in pierwsze:
            reszta = 0
            reszta= row - i
            if reszta in pierwsze:
                il+=1
print(il/2)
