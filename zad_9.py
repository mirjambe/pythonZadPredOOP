"""
9.  Napišite program koji učitava cijele brojeve sve dok je unesena
    vrijednost veća od 0. Pronađite koji od učitanih brojeva ima najmanju
    sumu znamenki te ispišite taj broj i sumu.
"""

listaBrojeva = []
broj = int(input("Unesi broj veći od 0: "))

while broj > 0:
    listaBrojeva.append(str(broj))
    broj = int(input("Unesi broj veći od 0: "))

print("Lista unesenih brojeva:", listaBrojeva)
dictBrojevi = {}
for x in listaBrojeva:
    x = list(x)
    suma = 0
    for n in x:
        suma += int(n)
    dictBrojevi.update({"".join(x): suma})
print(dictBrojevi)
najmanjaSuma = min (dictBrojevi.values())
print("Najmanja suma je:",najmanjaSuma)
for x in dictBrojevi:
    if dictBrojevi[x] == najmanjaSuma:
        print(f"Broj {x} ima najmanju sumu znamenaka {dictBrojevi[x]}")