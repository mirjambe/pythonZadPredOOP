"""
3.  Napiši program koji upisuje bodove n plesnih natjecanja.
    Ispiši zbroj svih bodova tako da odbaciš najbolji i najlošiji rezultat.
"""

n = 5 # broj natjecanja
listaBodova = []
for i in range(1, n+1):
    bodovi = int(input(f"Unesi bodove {i}. natjecanja: "))
    listaBodova.append(bodovi)
print("Svi unešeni bodovi:", listaBodova)
# Ukloni min i max iz liste bodova
listaBodova.remove(min(listaBodova))
listaBodova.remove(max(listaBodova))
print("Lista bez min i max vrijednosti:", listaBodova)
print("Suma bodova:", sum(listaBodova))