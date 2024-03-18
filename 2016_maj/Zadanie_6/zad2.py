def caesar(message: str, key: int) -> str:
    deszyfr = ""

    for letter in message:
        decrypted_letter = ord(chr((ord(letter) - ord('A') - key) % 25 + ord('A')))
        if decrypted_letter > ord("Z"):
            decrypted_letter = ord("A") + decrypted_letter - ord("Z")

        deszyfr += chr(decrypted_letter)

    return deszyfr






with open("dane_6_2.txt") as plik:
    for row in plik:
        row= row.strip()
        slowo, k=row.split(" ")
        k=int(k)
        with open("wyniki_6_2.txt", "a") as wyniki:
            wyniki.write(f"{caesar(slowo,k)}\n")