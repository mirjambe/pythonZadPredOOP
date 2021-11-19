"""
71. napravite tipicnog "chat bota" neke drzavne firme. bot treba primati input korisnika te ako se odredjena rijec u
    stringu poklapa sa nekim od njemu predefiniranih stringova ili rijeci, ispisati odgovarajucu poruku.
    npr. ako je korisnik unio "pozdrav, ja sam Alen i radim za mirovinsko osiguranje".
    bot treba kao prvi string ispisati: "pozdrav, ja sam bot i napravljen pomocu AI",
    zatim (zbog rijeci mirovinsko),
    ispisati: " hrvatski zavod za mirovinsko osiguranje je trenutno na pauzi".
    unesite po zelji 20ak razlicitih stringova te simulirajte neki razgovor/temu po zelji.
"""
odgovori = {'uvod': 'Pozdrav, ja sam bot napravljen pomocu AI',
            'mirovninsko': ['hzzmo je trenkutno na pauzi', 'ostavite svoj kontakt broj'],
            'teleoperater': ['pozdrav, zanima vas super opcija', 'samo danas', '10GB za samo 30kn?', 'naruči odmah']
            }
ulaziOdKorisnika = []
ulaz = input("Kraj --> 0\nUnesi neki string --> ")
while ulaz != '0':
    ulaz = input("Kraj --> 0\nUnesi neki string --> ")
    if ulaz.find("mirovinsk") >= 0:
        print(odgovori['uvod'])
        ulaz = input("Unesi neki string --> ")
        ulaziOdKorisnika.append(ulaz)
        for i in range(0, len(odgovori['mirovninsko'])):
            print(odgovori['mirovninsko'][i])
            ulaz = input("Unesi neki string --> ")
            ulaziOdKorisnika.append(ulaz)
        break
    if ulaz.find("tele") >= 0:
        print(odgovori['uvod'])
        ulaz = input("Unesi neki string --> ")
        ulaziOdKorisnika.append(ulaz)
        for i in range(0, len(odgovori['teleoperater'])):
            print(odgovori['teleoperater'][i])
            ulaz = input("Unesi neki string --> ")
            ulaziOdKorisnika.append(ulaz)
        break
