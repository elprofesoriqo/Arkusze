


ilosci_wygranych={
    "A": 0,
    "B": 0
}

with open("mecz.txt") as file:
    for row in file:
        row=row.strip()

        for i in row:
            ilosci_wygranych[i]+=1
            if abs(ilosci_wygranych["A"]-ilosci_wygranych["B"])>=3 and (ilosci_wygranych["A"]>=1000 or ilosci_wygranych["B"]>=1000):
                if ilosci_wygranych["A"]>ilosci_wygranych["B"]:
                    print("A")
                print("B")
                break                
            
print(ilosci_wygranych)
