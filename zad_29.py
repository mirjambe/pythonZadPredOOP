"""
29. napravite program koji ce simulirati izvlacenje karti iz spila. program mora imati sljedece:
    - spil od 20 karti
    - 4 razlicite boje
    - 5 brojeva za svaku boju
    program treba imati mogucnost povlacenja 3 karte, povlacenja 1 karte, mijesanja spila, zbrajanja bodova (brojevi na kartama).
    kreirajte izbornik sa mogucnoscu izbora opcije (zapocni igru, zavrsi igru) -> ako korisnik odabere "zapocni igru",
    spil se mijesa te se povlace 3 karte. igraca se zatim pita hoce li povuci dodatnu kartu ili ne.
    ako odabere novu kartu, ona se dodaje u ruku; u suprotnom se broj bodova usporedjuje sa protivnikom.
    koristeci random varijablu (12-20), kreirajte protivnika, gdje random varijabla predstavlja njegov broj bodova.
    program treba racunati trenutni broj bodova te ako on prelazi 20, ispisati "izgubio si" i pitati korisnika zeli li
    ponovno igrati ili ne. ukoliko igrac pobijedi, treba ispisati poruku: pobijedio si i postaviti pitanje za novom igrom.
"""
import random


def fpromijesajSpil(dict_spil):
    kljucevi = list(dict_spil.keys())
    random.shuffle(kljucevi)
    promjesaneKarte = dict()
    for kljuc in kljucevi:
        promjesaneKarte.update({kljuc: dict_spil[kljuc]})
    return promjesaneKarte

def fizvuciKartu():
    karta, vrijednost = dict_spil.popitem()
    print(f"Karta: {karta}")
    return vrijednost

def fizvuci3Karte():
    suma = 0
    for i in range(0,3):
        karta, vrijednost = dict_spil.popitem()
        print(f"Karta {i+1}: {karta}")
        suma += vrijednost
    return suma

################################################################
ulaz =input("Utipkaj zapocni... kako bi počela igra...\n'zapocni' --> ")
brPobIg1 =0
brPobProt =0
while ulaz == 'zapocni':
    tuple_boja = ('crvena', 'zelena', 'plava', 'žuta')
    tuple_broj = (1, 2, 3, 4, 5)
    dict_spil = {}
    protivnikBodovi = random.randint(15,25)
    for boja in tuple_boja:
        for broj in tuple_broj:
            dict_spil.setdefault(boja+ "_" + str(broj), broj)
    print("Miješam karte...")
    dict_spil = fpromijesajSpil(dict_spil)
    dict_spil = fpromijesajSpil(dict_spil)
    dict_spil = fpromijesajSpil(dict_spil)
    print("Izvlačim 3 karte za Igrac 1...")
    Igrac1suma = fizvuci3Karte()
    print(f"Igrac 1, bodovi: {Igrac1suma}")
    ulaz = input("Zelite li dodatnu kartu, da / ne --> ")
    while ulaz != "ne":
        Igrac1suma += fizvuciKartu()
        print(f"Igrac 1, bodovi: {Igrac1suma}")
        if Igrac1suma > 20:
            print("Suma bodova > od 20...")
            break
        ulaz = input("Zelite li dodatnu kartu, da / ne --> ")
    print(f"Protivnik bodovi: {protivnikBodovi}")
    if abs(20 - protivnikBodovi) < abs(20 - Igrac1suma):
        print("Protivnik je pobijedio")
        brPobProt += 1
    elif abs(20 - protivnikBodovi) == abs(20 - Igrac1suma):
        print("Nerijeseno")
    else:
        print("POBJEDA!")
        brPobIg1 += 1
    print(f"Broj pobjeda:\nIgrac 1: {brPobIg1}  ---  Protivnik: {brPobProt}")
    ulaz = input("Igraš opeta? da / ne --> ")
    if ulaz == 'da':
        ulaz = 'zapocni'
print(f"Broj pobjeda:\nIgrac 1: {brPobIg1}  ---  Protivnik: {brPobProt}\nK R A J")