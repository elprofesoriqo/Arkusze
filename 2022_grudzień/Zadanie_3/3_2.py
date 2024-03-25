def pierwsza(n):

    for i in range(2,round(n**(1/2))+1):
        if n%i==0:
            return False
    return True


il_pier=0
with open("liczby.txt") as file:
    for row in file:
        row=row.strip()

        if pierwsza(int(row)-1):
            il_pier+=1

print(il_pier)