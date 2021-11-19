"""
10. S tipkovnice učitajte proizvoljni niz znakova. Kreirajte novi niz
    znakova koji će sadržavati naizmjence velika i mala slova iz ulaznog
    niza, redom kako se pojavljuju u ulaznom nizu: prvo veliko slovo u
    ulaznom nizu, prvo sljedeće malo slovo u nastavku ulaznog niza,
    prvo sljedeće veliko slovo u nastavku ulaznog niza itd. Novokreirani
    niz ispišite na zaslon. U nastavku se nalazi primjer:

Ulazni niz: ifeFemFEkej83FkW
Izlazni niz: FeFkFkW
"""
def fVeliko(start):
    global nizIzlazni
    for i in range(start, kraj):
        if nizZnakova[i].isupper():
            nizIzlazni += nizZnakova[i]
            return i
    return -1

def fMalo(start):
    global nizIzlazni
    for i in range(start, kraj):
        if nizZnakova[i].islower():
            nizIzlazni += nizZnakova[i]
            return i
    return -1

nizZnakova = input("Unesi niz znakova malih Velikih slova... : ")
print("Ulazni niz:", nizZnakova)

nizIzlazni = ""
pocetakPretrage = 0
kraj = len(nizZnakova)
trazim = 'v'
while pocetakPretrage < kraj:
    if trazim == 'v':
        pocetakPretrage = fVeliko(pocetakPretrage)
        if pocetakPretrage == -1:
            break
        else:
            pocetakPretrage += 1
            trazim = 'm'
    elif trazim == 'm':
        pocetakPretrage = fMalo(pocetakPretrage)
        if pocetakPretrage == -1:
            break
        else:
            pocetakPretrage += 1
            trazim = 'v'

print("Izlazni niz:", nizIzlazni)