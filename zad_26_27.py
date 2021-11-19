"""
26. vas omiljeni carobni aparat za kavu je podivljao. aparat treba ispitivati korisnika za kavu sve dok on ne unese "Q" ili 0.
    aparat prihvaca samo kovanice od 2kn ili 5kn.
    kada korisnik ubaci kovanicu od 5kn, aparat nausmicno izbacuje dvije kave.
    kada korisnik ubaci kovanicu od 2kn, aparat nasumicno izbaci jednu kavu.
    ako aparat sakupi 20kn, on se magicno napuni za 3 (nasumicne) kave.
    neka set sljedeceg oblika simbolizira pocetnu kolicinu kave u aparatu:
    dict_kava = {"turska": 4, "latte": 3, "espresso": 7, "makiyato": 5}.

27. nadogradite prethodni zadatak na nacin da ubacite u aparat i opciju za dodavanje mlijeka, secera ili meda u kavu.
    kada korisnik ubaci kovanicu, aparat ga treba pitati zeli li kavu sa dodatkom ili ne.
    postavite vrijednost svakog dodatka na 5, koristeci fromkeys.
    ukoliko korisnik zatrazi kavu sa sladilom kojega vise nema u aparatu, treba ispisati odgovarajucu poruku
    te ponuditi korisniku opciju bez dodatka ili povrat novca,
    nakon cega zavrsava sa izvodjenjem. u svim slucajevima treba se ispisati kakva je kava isporucena,
    sa kojim sladilom, koliko novca je ubaceno te koliki je iznos novca u aparatu nakon isporuke kave.
"""
import random


def fskuhajKvavu():
    vrsta = random.choice(list(dict_kava.keys()))
    while dict_kava[vrsta] <= 0:
        vrsta = random.choice(list(dict_kava.keys()))
    dict_kava[vrsta] -= 1
    print(f"Kuham kavu... {vrsta}")

def fdopuniAparat():
    print("Dopuna aparata s 3 random odabrane kave...")
    for i in range(1, 4):
        vrsta = random.choice(list(dict_kava.keys()))
        dict_kava[vrsta] += 1
    print("Nakon nadopune...", dict_kava)

def fdodatak():
    ulaz = input("Zelite dodatak da/ne: ")
    kuhamKavu = 'da'
    if ulaz == 'da':
        dodatak = input("Odaberite dodatak mlijeko/secer/med ")
        if dodatak not in list (dict_dodatak.keys()) or dict_dodatak[dodatak] == 0:
            print("Nema tog dodatka...")
            kuhamKavu = input("Da li zelite kavu bez dodataka, da/ne: ")
        else:
            dict_dodatak[dodatak] -= 1
            print("Dodali ste:", dodatak)
            print("Preostali dodatcki su", dict_dodatak)
            kuhamKavu = 'da'
    return kuhamKavu

ulaz = 1
dict_kava = {"turska": 4, "latte": 3, "espresso": 7, "makiyato": 5}
saldo = 0
tuple_dodatak = ('mlijeko', 'secer', 'med')
kol = 5
dict_dodatak = dict.fromkeys(tuple_dodatak, kol)

while ulaz != 'Q' and ulaz !='0':

    ulaz = input("Ako hoćeš kavu, ubaci 2 ili 5 kn\nIzlaz Q  ili 0\nUlaz: ")
    ulaz = ulaz.upper()
    #print("Trenutno:", dict_kava)
    if ulaz == "2":
        kavaDaNE = fdodatak()
        if kavaDaNE == "ne":
            break
        fskuhajKvavu()
        saldo += int(ulaz)
    elif ulaz == "5":
        kavaDaNE = fdodatak()
        if kavaDaNE == "ne":
            break
        fskuhajKvavu()
        fskuhajKvavu()
        saldo += int(ulaz)
    print("Nakon kuhanja: ", dict_kava)
    if saldo >= 20:
        fdopuniAparat()
        saldo = 0



