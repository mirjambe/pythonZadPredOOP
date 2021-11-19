"""
8.  Napišite program koji s tipkovnice učitava proizvoljni cijeli
    troznamenkasti broj. Ako učitani broj nije troznamenkasti, ispišite
    poruku o greški i prekinite daljnje izvođenje programa. U slučaju da
    je učitani broj ispravan, ispišite prvi sljedeći troznamenkasti
    palindrom. Na primjer, ako je učitani broj 120, prvi sljedeći palindrom
    je 121.
"""
broj = int(input("Unesi neki troznamenkasti cijeli broj: "))
print("Unijeli ste broj:", broj)

if broj < 0:
    brojPoz = broj * (-1)
else:
    brojPoz = broj

if brojPoz >= 100 and brojPoz <= 999:
    print("Unijeli ste dobr broj.")

    palinBroj = str(brojPoz)
    palinBroj = list(palinBroj)
    while palinBroj[0] != palinBroj[2]:
        palinBroj = "".join(palinBroj)
        palinBroj = int(palinBroj)
        palinBroj += 1
        palinBroj = str(palinBroj)
        palinBroj = list(palinBroj)
    palinBrojStr = "".join(palinBroj)
    if brojPoz != broj:
        palinBrojStr = "-"+palinBrojStr
    print("Slijedeći palindrom unesenog broja je:",palinBrojStr)
else:
    print("Niste unijeli dozvoljen broj.")