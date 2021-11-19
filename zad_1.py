"""
1.  Napiši program koji učitava listu i briše sve duplikate iz te liste
    te ispisuje novu listu s obrisanim duplikatima.
"""

lista = input("Unesi elemente liste.\nElemente razdvajaš praznim mjestom: ")
lista = lista.split(" ")

listElemenata = []
listaDuplikata = []

for element in lista:
    if element not in listElemenata:
        listElemenata.append(element)
    else:
        listaDuplikata.append(element)
print(f"Originalna, unešena lista: {lista}")
print(f"Lista različitih elemenata: {listElemenata}")
print(f"Lista elementa koji se ponavljaju: {listaDuplikata}")

