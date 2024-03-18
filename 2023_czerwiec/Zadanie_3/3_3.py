def roznica(a: str,b: str)-> int:
    return abs(int(a,2)-int(b,2))





dane=[]
roznice=[]
with open("anagram.txt") as file:
    for row in file:
        row=row.strip() 
        dane.append(row)


for i in range(len(dane)-1):
    roznice.append(roznica(dane[i], dane[i+1]))

print(bin(max(roznice))[2:])