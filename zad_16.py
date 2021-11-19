"""
16. Napišite program koji sadrži varijablu u kojoj je upisan proizvoljni
    niz znakova i brojčanu varijablu n. Provjerite je li vrijednost varijable
    n manja od broja znakova u nizu. Ako je vrijednost varijable n veća
    ispišite informaciju o grešci. Ispišite iz niza znakova svako n-to
    slovo. Na primjer, ulazni niz je "ABCDEFGH", n je 2, tada je izlaz
    "ACEG".
"""
niz = "Pustim problem da prenoći. Ko zna, možda se i ne probudi."
n = 2


noviNiz = ""
if n < len(niz):
    for i in range(0, len(niz), n):
        noviNiz += niz[i]
print(f"Zadani niz:", niz)
print(f"Svaki {n}-i član je", noviNiz)