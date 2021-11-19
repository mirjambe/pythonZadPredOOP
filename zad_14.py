"""
14. Odaberite proizvoljno koordinatu T=(x,y), vrijednosti varijabli x
(stupac) i y (redak) neka budu manje od 10. Program neka ispiše
polje 10x10 čiji su svi elementi vrijednosti "-" osim koordinate T čija
je vrijednost "X".

Primjer: T=(1,1)
- - - - - - - - - -
- X - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
"""
# točka T (x, y)
x = 3
y = 2
n = 10
print(f"T=({x}, {y})")
for i in range(0, n):
    for j in range(0, n):
        if i == 2 and j == 3:
            print('x', end=' ')
        else:
            print('-', end=' ')
    print()
