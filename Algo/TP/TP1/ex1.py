def factorielle(n):
    somme = 0
    for i in range(1, n+1):
        somme += i
    return somme

def somme_factorielle(n):
    somme = 0
    if n == 0:
        return somme + 1
    for i in range(1, n+1):
        somme += factorielle(i)
    return somme

print(factorielle(3))
print(somme_factorielle(3))
print(somme_factorielle(0))
