def somme_inverse_recursive(n):
    if n == 1:
        return 1
    else:
        return (1/n**2) + somme_inverse_iterative(n-1)

#print(somme_inverse_recursive(2))

def somme_inverse_iterative(n):
    somme = 0
    for i in range(1,n+1):
        somme += 1/i**2
    return somme

print(somme_inverse_iterative(2))


def n_premiers_iterative(n):
    somme = [1]
    for i in range(1,n):
        somme.append(3*somme[i-1] + 1)
    return somme

#print(n_premiers_recursive(3))

def n_premiers_recursive(n):
    if n == 1:
        return [1]
    else:
        suite = n_premiers_recursive(n-1)
        suite.append(3*suite[-1] + 1)
    return suite 
print(n_premiers_recursive(3))


def suite_n_terme(n):
    somme_u = 4
    somme_v = 5
    for i in range(n):
        somme_u, somme_v = ((somme_u + somme_v) / (2)), ((somme_u * somme_v) ** (1/2))
    return somme_u, somme_v

print(suite_n_terme(20))


def nb_occureences(chaine, lettre):
    if chaine == '':
        return 0
    else:
        if chaine[0] == lettre:
            return 1 + nb_occureences(chaine[1:], lettre)
        else:
            return nb_occureences(chaine[1:], lettre)

print(nb_occureences('Bonjour', 'o'))


def anagram(chaine1, chaine2):
    if len(chaine1) != len(chaine2):
        return False
    else:
        if chaine1 == chaine2:
            return True
        else:
            return anagram(chaine1[1:], chaine2[1:]) and anagram(chaine1[1:], chaine2[:-1])

print(anagram('gare', 'rages'))


def suite_syracuse(n, conteur=0):
    if n == 1:
        return conteur
    if n % 2 == 0:
        return suite_syracuse(n//2, conteur+1)
    else:
        return suite_syracuse(3 * n + 1, conteur+1)


print(suite_syracuse(10))
print(suite_syracuse(7))


def appartient(n, liste):
    if liste == []:
        return False
    else:
        for i in range(len(liste)):
            if n == liste[i]:
                return True
        return False

print(appartient(1, [1, 2, 3]))

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

def intersection_liste(liste1, liste2):
    intersection = []
    for element in liste1:
        if element in liste2:
            intersection.append(element)
    return intersection


print(intersection_liste([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]))
print(intersection_liste([1, 2, 3, 4, 5], [6, 5, 4, 3, 2]))
print(intersection_liste([1, 2, 3, 4, 5], [7, 8, 9, 10, 11]))
