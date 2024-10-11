def anagram(chaine1, chaine2):
    if len(chaine1) != len(chaine2):
        return False
    else:
        if chaine1 == chaine2:
            return True
        else:
            return anagram(chaine1[1:], chaine2[1:]) and anagram(chaine1[1:], chaine2[:-1])

print(anagram('gare', 'rages'))
