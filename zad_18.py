"""
18. Ispišite sve parne brojeve između 1 i 1000 koju su istovremeno
    djeljivi i s 5 i s 13.
"""

djelitelj = 2*5*13
brojevi = []
for i in range(1, 1001):
    if i % djelitelj == 0:
        brojevi.append(i)
print(f"Brojevi iz intervala [1 - 1000] koji su djeljivi s 2, 5 i 13 su:\n{brojevi}")