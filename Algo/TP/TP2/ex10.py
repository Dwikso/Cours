def appartient(liste, n):
    if liste == []:
        return False
    if liste[0] == n:
        return True
    else:
        return appartient(liste[1:], n)

print(appartient([1, 2, 3], 1))
print(appartient([1, 2, 3], 2))
print(appartient([1, 2, 3], 3))
print(appartient([1, 2, 3], 4))
