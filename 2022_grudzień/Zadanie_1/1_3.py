
passy={}

with open("mecz.txt") as file:
    for row in file:
        row=row.strip()
        passa=1
        j=1
        for i in range(1,len(row)):
            if row[i] != row[i-1]:
                if passa>=10:
                    passy[f"{j}_{row[i-1]}"]=passa
                    j+=1
                passa=1
            else:
                passa+=1



print(f"Ilość pass: {len(passy)}\n{max(passy.values()), max(passy, key=passy.get)[-1]}")