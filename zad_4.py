"""
4. Kreiraj listu brojeva i pretvori svaki element u listi u njegov kvadrat
"""

listaBrojeva = [2, 15, 12, 7, 5]
print("Lista brojeva:", listaBrojeva)
kvadrati = [x*x for x in listaBrojeva]
print("lista kvadrata:", kvadrati)

# drugi način
for i in range(len(listaBrojeva)):
    listaBrojeva[i] *= listaBrojeva[i]
print("Lista brojeva:", listaBrojeva)
