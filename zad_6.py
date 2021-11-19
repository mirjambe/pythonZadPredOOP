"""
6.  S tipkovnice učitavajte cijele brojeve. Prvi upisani broj može biti bilo
    koji cijeli broj.
    Učitavanje ponavljati dok god je upisani broj strogo veći od prethodno upisanog broja.
    Ispisati sumu svih učitanih brojeva osim broja zbog kojeg je prekinuto učitavanje.
"""
listaBrojeva = []
uvjet = True
broj = int(input("Unesi neki cijeli broj: "))
suma = 0
while uvjet:
    suma += broj
    slBr = int(input("Unesi neki cijeli broj: "))
    listaBrojeva.append(broj)
    uvjet = slBr > broj
    broj = slBr
print("Lista brojeva: ",listaBrojeva)
print("Suma brojeva liste:", sum(listaBrojeva), f"ili na drugi nacin {suma}")
