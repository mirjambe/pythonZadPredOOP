"""
2.  Napravi obrtaljku od unesenog stringa te na svakom drugom mjestu pridruzi
    nasumičan broj.
"""
import random

stringUlaz = input("Unesi neki niz: ")
print("Uneseni string:", stringUlaz)
print("Obrnuti:", stringUlaz[::-1])

obrnutoSBrojem = stringUlaz[::-1]
obrnutoSBrojem = list(obrnutoSBrojem)
for i in range(0, len(stringUlaz), 2):
    randomNum = random.randint(1, 10)
    obrnutoSBrojem[i] += str(randomNum)
print("Obrnuti s brojem na svakom drugom slovu:", "".join(obrnutoSBrojem))
