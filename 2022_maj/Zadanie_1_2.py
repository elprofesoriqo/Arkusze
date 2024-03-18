def permutacje(a:list, n:int )->int:
    liczby=[]
    k=0
    ilosc_za_duzych=0
    duplikaty=0
    for i in range(0,n+1):
        liczby+=[0]
        if a[i-2]>n:
            ilosc_za_duzych+=1


    for i in range(1,n):
        for j in a:
            if i==j:
                liczby[i]+=1


    for i in liczby:
        while i>1:
            duplikaty+=1
            i-=1

    k+=ilosc_za_duzych
    k+=duplikaty

    return k

a=[8,4,9,6,5,7]
n=6

print(permutacje(a,n))