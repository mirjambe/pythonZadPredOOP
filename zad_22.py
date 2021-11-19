"""
22. Napišite program za koji traži najveći zajednički djelitelj dvaju brojeva
"""
# 14. Napišite program za koji traži najveći zajednički djelitelj dvaju brojeva

# Funkcija vraća slijedeći prosti broj koji dolazi nakon broja kojeg
# proslijedimo argumentom.
def slijedeciProstiBr (broj):
    broj += 1
    i = 1
    djelitelji = []
    while i <= broj:
        if broj % i == 0:
            djelitelji.append(i)
        i += 1
    if len(djelitelji) > 2:
        return slijedeciProstiBr(broj)
    else:
        return broj

# Test funkcije:
# print (slijedeciProstiBr(5))

# Funkcija broj iz argumenta pretvara u niz koji sadrži broj pretvoren
# u proste faktore.
def brojUProstimFaktorima (broj):
    prostiFaktori = []
    djelitelj = slijedeciProstiBr(1)
    while broj > 1:
        if broj % djelitelj == 0:
            prostiFaktori.append(djelitelj)
            broj /= djelitelj
        else:
            djelitelj = slijedeciProstiBr(djelitelj)
    return prostiFaktori

# Test funkcije:
#print(brojUProstimFaktorima(326))

# Zadana 2 broja:
broj_1 = 140
broj_2 = 220
# 1. Rastaviti brojeve na proste faktore:
broj_1Faktori = brojUProstimFaktorima(broj_1)
broj_2Faktori = brojUProstimFaktorima(broj_2)

print("Broj:", broj_1, "raspisan na proste faktore ->", broj_1Faktori)
print("Broj:", broj_2, "raspisan na proste faktore ->", broj_2Faktori)

zajednDjelitelj_lista = []
i = 0
while i < len(broj_1Faktori):
    #print(broj_1Faktori[i] in broj_2Faktori)
    if broj_1Faktori[i] in broj_2Faktori:
        zajednDjelitelj_lista.append(broj_1Faktori[i])
        broj_2Faktori.remove(broj_1Faktori[i])
        broj_1Faktori.remove(broj_1Faktori[i])
    else:
        i += 1

i = 0
zajednDjelitelj = 1
while i < len(zajednDjelitelj_lista):
    zajednDjelitelj *= zajednDjelitelj_lista[i]
    i += 1
print("Zajednički faktori oba broja ->",zajednDjelitelj_lista, "Zajednički djelitelj je broj:", zajednDjelitelj)


