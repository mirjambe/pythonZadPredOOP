"""
11. Napišite program koji s tipkovnice učitava cijeli broj n iz intervala [3, 20].
    U slučaju da je unesena vrijednost neispravna, ispisati prikladnu poruku
    na ekran te zatražiti ponovni unos cijelog broja.
    Nakon učitane vrijednosti n, učitajte n parova cijelih brojeva. Nakon što je n
    parova brojeva učitano, ispišite parove brojeva koji imaju najveću sumu.
"""
n = int(input("Unesi broj n iz itervala [3, 20]: "))
while n<3 or n>20:
    print("Broj nije OK. Ponovi unos.")
    n = int(input("Unesi broj n iz itervala [3, 20]: "))
dictParovi = {}
print(f"Unesite {n} parova:")
for i in range(1, n+1):
    print(f"Unos {i}. para:")
    kljuc = int(input(f"1. član {i}. para -> "))
    vrijednost = int(input(f"2. član {i}. para -> "))
    dictParovi.update({kljuc: vrijednost})
print(f"Uneseni parovi: {dictParovi}")
najvecaSuma = 0
key = 0
for x in dictParovi:
    if x + dictParovi[x] > najvecaSuma:
        najvecaSuma = x + dictParovi[x]
        key = x
print(f"Par s najvećeom sumom {najvecaSuma} je {key}: {dictParovi[key]}")