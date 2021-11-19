"""
19. Napisi program koji unosi n brojeva i od znamenke desetice svakog broja stvara
    novi broj.
"""

n = 5
brojevi = []
for i in range(1, n+1):
    broj = (input(f"Unesi {i}. broj -> "))
    brojevi.append(broj)

print("Uneseni brojevi su:", brojevi)
brOdDesetica = ""
for br in brojevi:
    if len(br) >= 2:
        brOdDesetica += br[len(br)-2]
print(f"Broj slozen od znamenki desetica je {brOdDesetica}")
