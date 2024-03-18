liczby = {}

nr = 0
with open("liczby.txt") as plik:
    for row in plik:
        nr += 1
        row = row.strip()
        liczby[nr] = int(row, 2)

max_value_key = max(liczby, key=liczby.get)
min_value_key = min(liczby, key=liczby.get)

with open("wynik4.txt", "a") as wyniki:
    wyniki.write("Zadanie 3:\n")

    wyniki.write(f"Największa liczba: {max(liczby.values())}, Numer: {max_value_key}\n")
    wyniki.write(f"Najmniejsza liczba: {min(liczby.values())}, Numer: {min_value_key}\n")
