def nb_occureences(chaine, lettre):
    if chaine == '':
        return 0
    else:
        if chaine[0] == lettre:
            return 1 + nb_occureences(chaine[1:], lettre)
        else:
            return nb_occureences(chaine[1:], lettre)

print(nb_occureences('Bonjour', 'o'))


