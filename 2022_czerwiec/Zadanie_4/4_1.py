

with open("liczby.txt") as file:
    for row in file:
        row=row.strip()

        if int(row[::-1]) %17==0:
            print(row[::-1])