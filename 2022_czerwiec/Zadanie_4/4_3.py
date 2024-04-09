
def primary(n):
    n=int(n)
    for i in range(2,round(n**(1/2))+1):
        if n%i==0:
            return False
    return True




with open("liczby.txt") as file:
    for row in file:
        row=row.strip()
        if primary(int(row)) and primary(int(row[::-1])):
            print(row)