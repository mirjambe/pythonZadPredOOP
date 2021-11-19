"""
24. zadan je rjecnik:
automobil = {
                'kilometri' : 230000,
                'oprema' : ['zimske gume', 'zracni jastuk', 'protuprovalni bacac plamena'],

            }
    a) kilometre preuredite tako da dodatno broji i kilometre do servisa. postavite vrijednost na 300.
    b) iz opreme, promijenite "zimske gume" u "ljetne gume" te "zracni jastuk" u "zracni balon"
    c) dodajte polje za unos specifikacije koja sadrzi godinu proizvodnje (1976.), potrosnju (15 litara) i max. brzinu (178 km/h)
    d) dodajte cijenu i postavite je na 45000
    e) dodajte osiguranje (npr. croatia) te postavite vrijednost na True
    f) kada se pozove funkcija 'servis', znaci da se automobil servisirao i promijenile su se sljedece vrijednosti:
        - kilometri do servisa su se postavili na 2000
        - zracni balon postao je 'novi zracni jastuk'
        - ljetne gume promijenjene su na 'cjelogodisnje gume'
        - cijenu uvecajte za 2000
"""



automobil = {
                'kilometri' : 230000,
                'oprema' : ['zimske gume', 'zracni jastuk', 'protuprovalni bacac plamena'],

            }
#a
automobil.pop('kilometri')
automobil.update({'kilometri': {'presao': 230000, 'doServisa': 300}})
print("Nakon a) automobil=",automobil)

#b
automobil['oprema'][0]= 'ljetne gume'
automobil['oprema'][1]= 'zracni balon'
print("Nakon b) automobil=",automobil)

#c
automobil.setdefault('proizveden', 1976)
automobil.setdefault('potrosnja', 15)
automobil.setdefault('maxBrzina', 178)
print("Nakon c) automobil=",automobil)

#d
automobil.update({'cijena': 45000})
print("Nakon d) automobil=",automobil)

#e
automobil.update({'osiguranje': {'valjanaPolica': True, 'kuca': 'croatia'}})
print("Nakon e) automobil=",automobil)

#f
def f_servis():
    automobil['kilometri']['doServisa'] = 2000
    automobil['oprema'][1] = 'novi zracni jastuk'
    automobil['oprema'][0] = 'cjelogodišnje gume'
    automobil['cijena'] += 2000

f_servis()
print("Nakon f) automobil=",automobil)