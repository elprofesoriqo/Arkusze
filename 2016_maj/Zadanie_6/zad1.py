def caesar(message: str, key: int) -> str:
    szyfr = ""
    

    for znak in message:
        pozycja = ord(znak) 
        pozycja+= key
        while pozycja>90:
            pozycja-=25

        szyfr+=chr(pozycja)
    return szyfr



nr=1
with open("dane_6_1.txt") as plik:

    for row in plik:
        row = row.strip()
        print(f"{nr} {caesar(row,103)}")            
        nr+=1
