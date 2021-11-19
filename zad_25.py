"""
25. napisite funkciju koja prima string oblika "<predmet>, <cijena>, <kolicina>" (npr. "kruh, 7.5, 5"),
    koji bi simulirao policu neke trgovine. program treba razdvojiti navedeni string te zasebne elemente spremiti u rjecnik.
    rjecnik se treba spremiti u listu proizvoda. simuliraj kupovinu: kada kupac kupi proizvod (ili broj proizvoda),
    njegova kolicina se treba umanjiti za iznos. ukoliko je kolicina 0, predmet se treba ukloniti sa police.
"""


listaProizvoda = []
nizUlaz=1
while nizUlaz != '0':
    nizUlaz = input("Unesi proizvod u obliku: '<predmet>, <cijena>, <kolicina>': ")
    if nizUlaz == '0':
        break
    predmet, cijena, kolicina = nizUlaz.split(", ")
    cijena = float(cijena)
    kolicina = int(kolicina)
    dicProizvod = {'predmet': predmet, 'cijena': cijena, 'kolicina': kolicina}
    listaProizvoda.append(dicProizvod)

def ispisProizvoda():
    print("Lista proizvoda:")
    print(f"{'Predmet':10}{'Cijena':10}{'Kolicina':10}")
    for l in listaProizvoda:
        print("{:10} {:10} {:10}".format(l['predmet'], l['cijena'], l['kolicina']))
ispisProizvoda()
##########################################################################################
def kupovina():
    predmet = input("Upiši naziv artikla - predmet -> ")
    kolicina = int(input("Upiši količinu -> "))

    for l in listaProizvoda:
        if l['predmet'] == predmet:
            if kolicina > l['kolicina']:
                print(f"Nema toliko proizvoda... Kolicina proizvoda je {l['kolicina']}")
                break
            else:
                l['kolicina'] -= kolicina
        if l['kolicina'] == 0:
            listaProizvoda.remove(l)

kupovina()
ispisProizvoda()
