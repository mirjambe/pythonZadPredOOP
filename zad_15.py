"""
15. Napišite program koji ispisuje koliko ima prostih brojeva između
    dva proizvoljna broja
    (prost broj je broj koji je djeljiv samo sa 1 i sa samim sobom).
"""

pocetak = 1
kraj = 10

def fprostBroj (broj):
    djelitelji = []
    for i in range(1, broj+1):
        if broj % i == 0:
            djelitelji.append(i)
    if len(djelitelji) <= 2:
        return broj
    else:
        return -1

listaProstih = []

for i in range(pocetak, kraj+1):
    prostBr = fprostBroj(i)
    if prostBr != -1:
        listaProstih.append(prostBr)
print(f"U intervalu [{pocetak} - {kraj}] ima {len(listaProstih)} prostih brojeva.\nTo su brojevi: {listaProstih}")