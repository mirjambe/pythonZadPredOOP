"""
28. Neka program omoguci unos do trenutka kad je unesen broj -1. Korisnik unosi stringove,
    a program vraca slucajne recenice iz zbirke mogucih odgovora.
"""

set_odgovori = {'bok', 'kako je', 'sto ima novo', 'danas je lijep dan', 'sutra će kiša', 'jedva čekam božić', 'bit će bolje', 'i sutra je dan', 'nista nova'}
ulaz = 1
while ulaz != '-1':
    odg = set_odgovori.pop()
    print("\t", odg)
    set_odgovori.add(odg)
    ulaz = input("Ubaci niz, prekid s '-1 ': ")

"""    
import random

print("***Izlaz --> -1")
ulaz = ""
zbirkaOdgovora = ["Bok!", "Sto ima kod tebe?", "Kako si danas?", "Baš je lijepo ovdje.", "Jel imaš koronicu :)", "Što ima za obid?"]
while ulaz != "-1":
    ulaz = input("Unesite string: ")

    index = random.randint(0, len(zbirkaOdgovora) - 1)
    print(zbirkaOdgovora[index])
"""