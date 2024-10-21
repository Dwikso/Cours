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

def repetition(liste):
    liste2 = []
    for i in range(len(liste)):
        if liste[i] in liste2:
            return liste[i]
        else:
            liste2.append(liste[i])
    return -1

l = [1,2,3,5,7,5,2,12,1]
print(repetition(l))


def intrus(liste):
    unique = 0
    for num in liste:
        unique ^= num
    return unique


l = [1,2,3,5,7,5,2,1,3]
print(intrus(l))

def intervalle_est_dans_liste(liste,n,m):
    for i in range(n,m+1):
        if i not in liste:
            return False
    return True


l = [4,1,2,3,5,7,5,2,1,3,6,9]
print(intervalle_est_dans_liste(l,3,12))
print(intervalle_est_dans_liste(l,3,6))

