"""
21. Ispišite sljedeće primjere koristeći funkcije i petlju. funkcija mora primati varijabilan broj redaka koji ispisuje
    (npr. pod a), unesen broj je 7, jer ima 7 redaka. pod b) je unesen broj 5, jer ima 5 redaka)

a)
*
**
***
****
***
**
*

b)
  *
 ***
*****
 ***
  *

c)
1010101
 10101
  101
   1

d)
x x x x
x x x
x x
x
x x
x x x
x x x x
"""
znak = "*"
def f_crtajZVj(brR):
    global znak
    if brR % 2 == 0:
        brR = brR + 1
    pola = brR // 2 + 1
    i = 1
    brZv = 0
    while i <= brR:
        if i <= pola:
            brZv += 1
        else:
            brZv -= 1
        print(znak*brZv)
        i += 1

def f_crtajDi (brR):
    global znak
    if brR % 2 == 0:
        brR = brR + 1
    niz = znak
    i = 1
    while i <= brR:
        print(niz.center(brR))
        if i <= brR//2:
            niz = niz + znak * 2
        else:
            niz = niz.removeprefix(znak * 2)
        i += 1

def f_crtajO1(brR):
    maxNumInR = brR *2
    numInRow = maxNumInR
    niz = ""
    while brR >= 0:
        j = 1
        niz = ""
        while j < numInRow:
            if j % 2 != 0:
                niz += "1"
            else:
                niz += "0"
            j += 1
        print(niz.center(maxNumInR))
        numInRow -= 2
        brR -= 1

def f_crtajX(brR):
    znak = "x"
    if brR % 2 == 0:
        brR = brR + 1
    pola = brR // 2 + 1
    i = 1
    brZv = pola+1
    while i <= brR:
        if i <= pola:
            brZv -= 1
        else:
            brZv += 1
        print(znak*brZv)
        i += 1


#a
print("Rjesenje pod a)")
f_crtajZVj(8)

#b
print("Rjesenje pod b)")
f_crtajDi(8)

#c
print("Rjesenje pod c)")
f_crtajO1(6)

#d
print("Rjesenje pod d)")
f_crtajX(9)
