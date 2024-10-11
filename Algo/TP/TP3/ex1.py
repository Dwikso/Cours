import time
from random import * 

def cree_liste():
    n = 10000
    liste = list(range(n))
    liste.append(n)
    random.shuffle(liste)
    return liste


def tri_selection(l):
    start_time = time.time()
    for i in range(len(l)):
        ind_mini = recherche_mini(l,i)
        l[i], l[ind_mini] = l[ind_mini], l[i]
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Temps écoulé (tri sélection) : {elapsed_time:.8f} secondes")
    return 

def recherche_mini(l, ind):
    assert ind < len(l)
    mini = ind
    for i in range(ind,len(l)):
        if l[i] < l[mini]:
            mini = i
    return mini


def tri_a_bulles(l):
    start_time = time.time()
    for i in range(len(l)):
        for ind in range(len(l)-i-1):
            if l[ind] > l[ind+1]:
                l[ind], l[ind+1] = l[ind+1], l[ind]
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Temps écoulé (tri a bulles) : {elapsed_time:.8f} secondes")
    return

def tri_insertion(l):
    start_time = time.time()
    for i in range(1, len(l)):
        ref = l[i]
        j = i - 1
        while j >= 0 and l[j] > ref:
            l[j + 1] = l[j]
            l[j] = ref
            j -= 1
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Temps écoulé (tri insertion) : {elapsed_time:.8f} secondes")
    return l  

def fussionner(a, b):
    c = []
    n, m = len(a), len(b)
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i == len(a):
        for k in range(j, len(b)):
            c.append(b[k])
    else:
        for k in range(i, len(a)):
            c.append(a[k])
    return c

def tri_fusion(a):
    start_time = time.time()
    n = len(a)
    if n <= 1:
        return a
    m = n // 2
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Temps écoulé (tri fusion) : {elapsed_time:.8f} secondes")
    return fussionner(tri_fusion(a[:m]), tri_fusion(a[m:]))

# liste = cree_liste()
# liste2 = liste[:]
# liste3 = liste[:]
# liste4= liste[:]
# print(tri_insertion(liste))
# print(tri_selection(liste2))
# print(tri_a_bulles(liste3))
# print(tri_fusion(liste4))

#Classe pile
class Pile :
    '''Definition d'une pile - structure de données LIFO (Last In First Out)
    '''

    def __init__(self) : 
        '''Pile -> Pile
        construit une pile vide
        '''
        # basée sur une pile
        self.__les_elts = list()
        
    
    def empiler(self,elt) :
        '''(modif) Pile, Objet -> Rien
        ajoute un élément au sommet de la pile.
        '''
        self.__les_elts.append(elt)
            
    def est_vide(self) : 
        '''Pile -> Boolean
        teste si la pile est vide. '''
        return len(self.__les_elts) == 0
  
    def sommet(self) : 
        '''Pile -> Objet
        retourne l'élément au sommet de la pile.
        '''
        assert not self.est_vide()
        return self.__les_elts[-1] 
        
    def depiler(self) : 
        '''(modif) Pile -> Objet
        enlève l'élément au sommet de la pile.
        ''' 
        assert not self.est_vide()
        elt = self.__les_elts[-1] 
        del(self.__les_elts[-1])
        return elt
    
    def __str__(self):
        return str(self.__les_elts)
    
    def __repr__(self):
        return self.__str__()

#Exercice 4

def inverse_pile(pile: Pile) -> None:
    """
    Inverse les éléments d'une pile sans la vider.
    """
    pile_temporaire = Pile()
    pile_inversee = Pile()
    while not pile.est_vide():
        pile_temporaire.empiler(pile.depiler())
    while not pile_temporaire.est_vide():
        pile_inversee.empiler(pile_temporaire.depiler())
    while not pile_inversee.est_vide():
        pile.empiler(pile_inversee.depiler())
    return pile

def tri_piles_selection(pile):
    pile_triee = Pile()

    while not pile.est_vide():
        min_val = pile.depiler()  
        pile_temp = Pile()
        while not pile.est_vide():
            current = pile.depiler()
            if current < min_val:
                pile_temp.empiler(min_val)  
                min_val = current
            else:
                pile_temp.empiler(current)  
        pile_triee.empiler(min_val)
        while not pile_temp.est_vide():
            pile.empiler(pile_temp.depiler())
    while not pile_triee.est_vide():
        pile.empiler(pile_triee.depiler())
    return inverse_pile(pile)

pile_test = Pile()
pile_test.empiler(3)
pile_test.empiler(1)
pile_test.empiler(4)
pile_test.empiler(2)
print(tri_piles_selection(pile_test))

def diviser_en_sous_liste(liste,k):
    taille = len(liste)
    sous_liste = []
    for i in range(k):
        sous_liste.append(liste[i*taille//k:(i+1)*taille//k])
    return sous_liste

def tri_mixte(liste, k):
    sous_listes = diviser_en_sous_liste(liste, k)
    sous_listes_tries = [tri_insertion(sous_liste) for sous_liste in sous_listes]
    while len(sous_listes_tries) > 1:
        sous_listes_tries.append(fussionner(sous_listes_tries.pop(0), sous_listes_tries.pop(0)))
    return sous_listes_tries[0]

def test_k(liste):
    n = len(liste)
    meilleur_temps = float('inf')
    meilleur_k = 0

    for k in range(2, n + 1):
        debut = time.time()
        tri_mixte(liste, k)
        temps_ecoule = time.time() - debut
        if temps_ecoule < meilleur_temps:
            meilleur_temps = temps_ecoule
            meilleur_k = k

        print(f"k: {k}, temps: {temps_ecoule:.8f} secondes")

    print(f"Meilleur k: {meilleur_k} avec : {meilleur_temps:.8f} secondes")

n = 1000
random_list = [randint(0,100) for _ in range(n)] 

test_k(random_list)

liste = [34, 7, 23, 32, 5, 62, 32, 2, 10, 17, 24, 27]
k = 3  
liste_triee = tri_mixte(liste, k)
print(liste_triee)


