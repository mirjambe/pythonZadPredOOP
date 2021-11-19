"""
5.  Kreiraj listu koja se sastoji od stringova i brojeva,
    te odvoji brojeve i stringove u zasebne liste
"""

lista = [378, 'ovo je lista', 2.25, 15, 'od', "brojeva", 15, 1.22, 'i', "stringova"]
listaBrojeva = []
listaStringova = []
for element in lista:
    if str (type(element)).find('str') > 0:
        listaStringova.append(element)
    else:
        listaBrojeva.append(element)
print("Originalna lista:", lista)
print("Lista brojeva:", listaBrojeva)
print("Lista stringova:", listaStringova)
