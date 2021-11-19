"""
17. Napišite program koji sadrži varijablu u kojoj je upisan proizvoljni niz
    znakova. Ispišite koliko velikih slova se nalazi u nizu. Ako je neko od
    unesenih slova u nizu "A", brojanje velikih slova je potrebno prekinuti
    i ispisati informaciju da je veliko slovo "A" pronađeno.
"""

niz = "U ovome Nizu Treba poBROjat VeliKa SLOVo"
brVelikihSl = 0

for i in range(len(niz)):
    if niz[i].isupper():
        brVelikihSl += 1
        if niz[i] == 'A':
            print("Pronađeno slovo 'A', do tada...")
            break
print(f"Broj velikih slova u nizu {niz} je {brVelikihSl}.")