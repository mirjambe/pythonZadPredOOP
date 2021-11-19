"""
12. Napišite program koji s tipkovnice učitava proizvoljni niz znakova.
    Nad učitanim nizom znakova napravite analizu je li taj niz palindrom
    ili nije. Niz je palindrom ako se isto čita slijeva nadesno ili pak
    zdesna nalijevo.
"""
nizZnakova = input("Unesi niz znakova: ")
print("Input:", nizZnakova)
print("Output:", nizZnakova[::-1])
# pr. kisik
# Uklonila prazan prostor... da mi radi za: ana voli milovana
nizZnakova = nizZnakova.replace(" ", "")
novi = nizZnakova[::-1]
novi = novi.replace(" ", "")
if nizZnakova == novi:
    print("Uneseni niz je palindrom.")
else:
    print("Uneseni niz nije palindrom.")