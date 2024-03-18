import math

wkw = 0
wko = 0
error = []
dane = []
pi=[]
def calculate_pi(dane, n):
    wko = 0
    wkw = 0
    for row in dane[:n]:
        x, y = map(int, row.strip().split(" "))
        a, b = 200, 200
        wkw += 1
        if (x - a) ** 2 + (y - b) ** 2 <= 200 ** 2:
            wko += 1
    return round((wko * 4) / wkw, 4)

with open("punkty.txt") as plik:
    for line in plik:
        dane.append(line)

for n in range(1, 1701):
    przewid_pi = calculate_pi(dane, n)
    true_pi = math.pi # True value of pi
    absolute_error = abs(true_pi - przewid_pi)
    pi.append(przewid_pi)
    error.append(absolute_error)

with open("punkciki.txt", "w") as pliczek:
    for i in range(len(error)):
        pliczek.write(f"{str(pi[i])};{str(error[i])} \n")
    
print(f"Odpowiedź: {error[1000], error[1699]}")