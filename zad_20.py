"""
20. Napisi program koji unosi n brojeva i sastavlja novi broj od najvece znamenke u svakom od
brojeva
"""
n = 5
brojevi = []
for i in range(1, n+1):
    broj = (input(f"Unesi {i}. broj -> "))
    brojevi.append(broj)

print("Uneseni brojevi su:", brojevi)
brOdNejvece = ""
for br in brojevi:
    brOdNejvece += max(br)

print(f"Broj slozen od najveće znamenke pojedina broja je: {brOdNejvece}")