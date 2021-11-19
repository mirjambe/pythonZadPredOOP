"""
23. koristenjem funkcija i naucenog, napisi program koji racuna iznos racuna u ovisnosti o transakcijama.
    dnevnik transakcija prikazi ovako (D: 100, W: 200), dok ukupan iznos na racunu prikazuje sa (T: 1000).
    ako korisnik unese T = 1000 te povuce iznos od 350 (W: 350), aplikacija treba ispisati azurirano stanje T: 650.
    ako nakon toga korisnik uplati iznos na racun, npr. 200 (D: 200), program treba uvecati iznos racuna
    i azurirati ga (T: 850). unosom stringa "quit", program prekida se izvodjenje programa.
"""
print("*** Evidencija računa ***")
saldoT = float(input("Unesi početno stanje računa: "))
ulaz = ""
iznos = 0
print("Odaberi vrstu transakcija:\nPovuci s računa -> w\nUplati na račun -> d\nKraj -> quit")
while ulaz != 'quit':
    print("Odaberi vrstu transakcije:\nPovuci s računa -> w\nUplati na račun -> d\nKraj -> quit")
    ulaz = input("Odaberi akciju: ")
    if ulaz == 'w':
        iznos = float (input("Iznos koji želiš povući s računa: "))
        saldoT -= iznos
        print(f"Provedena akcija (W: {iznos})")
    if ulaz == "d":
        iznos = float (input("Iznos koji želiš uplatiti na račun: "))
        print(f"Provedena akcija (D: {iznos})")
        saldoT += iznos
    print(f"Iznos salda. (T: {saldoT})")