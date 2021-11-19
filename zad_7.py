"""
7.  Učitajte s tipkovnice 2 niza znakova, svaki od tih nizova znakova
    spremite u zasebnu varijablu. Ispišite indekse na kojima se pojavljuju
    ista slova neovisno o veličini ('a' i 'A' tretirati jednako).
"""

print("Unesite dva niza znakova.")
prviNiz = input("Unesi prvi niz: ")
drugiNiz = input("Unesi drugi niz: ")

interval = len(prviNiz)
if interval > len(drugiNiz):
    interval = len(drugiNiz)

print(f"Uneseni nizovi:\n{prviNiz}\n{drugiNiz}")
print("Pozicije gdje su isti znakovi:")
for i in range(interval):
    if(prviNiz[i].lower() == drugiNiz[i].lower()):
        print(i+1, end=" \\")