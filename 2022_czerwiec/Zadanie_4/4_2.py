
roznice={}


with open("liczby.txt") as file:
    for row in file:
        row=row.strip()

        roznice[row]=abs(int(row)- int(row[::-1]))


print(max(roznice.values()))
for key, value in roznice.items():
    if value == max(roznice.values()):
        print(key)