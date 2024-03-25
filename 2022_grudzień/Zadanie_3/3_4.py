znaki={
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0
}



liczba=0
with open("liczby.txt") as file:
    for row in file:
        row=row.strip()

        liczba = str(hex(int(row))[2:])



        for i in liczba:
            if i in znaki:
                znaki[i]+=1





print(znaki)