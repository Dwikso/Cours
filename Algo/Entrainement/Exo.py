from ListeChaine import *

def compte_negatif(self, cpt=0):
    if self.__tete == None:
        return cpt
    elif self.__tete.get() < 0:
        return compte_negatif(self.__tete.suivant(), cpt+1)
    else :
        return compte_negatif(self.__tete.suivant(), cpt)

l = ListeChainee()
l.append(1)
l.append(-1)
l.append(2)
l.append(-2)
l.append(3)
l.append(-3)
print(compte_negatif(l))

