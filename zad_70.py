"""
70. kreirajte password generator, koji mora sadrzavati sljedece funkcionalnosti:
    a) prilikom generiranja treba prikupiti sljedece podatke od korisnika:
        - koliko lozinki zeli napraviti
        - da li da koristi slova, brojeve, simbole
        - duljinu lozinke
        - kapitalizaciju
    b) nadogradite program tako da korisnik upise rijec (hint). od hint se treba ubaciti u nasumicnom redosljedu i kapitalizaciji u lozinku koja se generira
"""
import random

print("Generator passworda\nUnesite slijedeće podatke...")
brLozinki = int(input("Koliko lozinki zelite generirati --> "))
duljinaLoz = int(input("Dauljina lozinke --> "))
slovaVelDaNe = input("Da li koristiti velika slova, da / ne --> ")   # velika slova (65 - 90)
slovaMalDaNe = input("Da li koristiti mala slova, da / ne --> ")   # mala slova (97 - 122)
brojeviDaNe = input("Da li koristiti brojeve, da / ne --> ")   # brojevi (48 - 57)
simbolDaNe = input("Da li koristiti simbole, da / ne --> ")   # znakovi (33 - 47, 58 - 64)

skupZnakova = []
if slovaVelDaNe == 'da':
    skupZnakova.extend([i for i in range(65, 91)])
if slovaMalDaNe == 'da':
    skupZnakova.extend([i for i in range(97, 123)])
if brojeviDaNe == 'da':
    skupZnakova.extend([i for i in range(48, 58)])
if simbolDaNe == 'da':
    skupZnakova.extend([i for i in range(33, 48)])
if simbolDaNe == 'da':
    skupZnakova.extend([i for i in range(58, 65)])

skupZnakovaZ = [chr(i) for i in skupZnakova]
random.shuffle(skupZnakovaZ)
random.shuffle(skupZnakovaZ)
random.shuffle(skupZnakovaZ)
for i in range(0, brLozinki):
    lozinka = ""
    for j in range(0, duljinaLoz):
        indeks = random.randint(0, len(skupZnakovaZ)-1)
        lozinka += skupZnakovaZ[indeks]
    print(f"Lozinka {i+1} = {lozinka}")