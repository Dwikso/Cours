class Maillon :
    """Classe qui modélise un maillon d'une liste chainee"""    
    def __init__(self, val, suiv=None):
        """Maillon, Objet, Maillon -> Maillon
        Construit un maillon d'une liste chainee"""
        self.__val = val
        self.__suiv = suiv
    
    def get(self):
        """Maillon -> Objet
        
        >>> m = Maillon(1)
        >>> m.get()
        1
        >>> m2 = Maillon(2, m)
        >>> m2.get()
        2
        >>> m2.suivant().get()
        1"""
        return self.__val
    
    def suivant(self):
        """Maillon -> Maillon
        
        >>> m = Maillon(1)
        >>> m.suivant()
        >>> m2 = Maillon(2, m)
        >>> m2.suivant().get()
        1"""
        return self.__suiv
    
    def set_suiv(self, m):
        """Maillon, Maillon -> None
        
        >>> m = Maillon(1)
        >>> m/set_suiv(Maillon(2))
        >>> m.suivant().get()
        2"""
        self.__suiv = m

    def __str__(self):
        """Maillon -> str
        
        >>> m = Maillon(1)
        >>> print(m)
        1
        >>> m2 = Maillon(2, m)
        >>> print(m2)
        2"""
        mess = str(self.__val)
        if self.__suiv != None :
            mess += ', '
        return mess

    def contient(self,val):
        if self.__val == val:
            return True
        if self.__suiv == None:
            return False
        return self.__suiv.contient(val)

    def indices_minimum(self, end, i_m, val_m):
        if self.__suiv == None:
            if self.__val == val_m:
                end.append(i_m)
                return end
            elif self.__val < val_m:
                return [i_m]
            else:
                return end
        if self.__val == val_m:
            end.append(i_m)
            return self.__suiv.indices_minimum(end, i_m + 1, val_m)
        elif self.__val < val_m:
            return self.__suiv.indices_minimum([i_m], i_m + 1, self.__val)
        else:
            return self.__suiv.indices_minimum(end, i_m + 1, val_m)

    def permute_pairs_recursive(self):
        """Permute chaque paire de maillons de manière récursive."""
        if self.__suiv is None or self.__suiv.suivant() is None:
            return self
        premier = self
        deuxieme = self.__suiv
        premier.set_suiv(deuxieme.suivant().permute_pairs_recursive())
        deuxieme.set_suiv(premier)
        return deuxieme

    def alternate_split_recursive(self, list1, list2, toggle):
        """Méthode récursive pour alterner les maillons dans deux listes."""
        if self is None:
            return
        if toggle:
            list1.append(self.get())
        else:
            list2.append(self.get())
        if self.suivant() is not None:
            self.suivant().alternate_split_recursive(list1, list2, not toggle)

class ListeChainee :
    """Classe qui modélise une liste sous la forme recursive d'une liste chainee"""
    def __init__(self):
        """ListeChainee -> ListeChainee
        Une liste est toujours initialisee a la liste vide"""
        self.__tete = None
    
    def est_vide(self):
        """ListeChainee -> boolean
        
        >>> l = ListeChainee()
        >>> l.est_vide()
        True
        >>> l.append(1)
        >>> l.est_vide()
        False"""
        return self.__tete == None
    
    def append(self, val):
        """ListeChainee, Objet -> None
        
        >>> l = ListeChainee()
        >>> print(l)
        []
        >>> L.append(1)
        >>> print(l)
        [1]
        >>> l.append(2)
        >>> l.append(3)
        >>> print(l)
        [1, 2, 3]
        """
        if self.est_vide():
            self.__tete = Maillon(val)
        else :
            #prec : maillon auquel on va raccrocher le nouveau maillon
            prec = self.__tete
            while prec.suivant() != None :
                prec = prec.suivant()
            prec.set_suiv(Maillon(val))
        
    def __str__(self):
        """ListeChainee -> str
        
        >>> l = ListeChainee()
        >>> print(l)
        []
        >>> l.append(1)
        >>> print(l)
        [1]
        >>> l.append(2)
        >>> l.append(3)
        >>> print(l)
        [1, 2, 3]
        >>> l.len()
        3"""
        mess = "["
        prec = self.__tete
        while prec != None:
            mess += prec.__str__()
            prec = prec.suivant()
        mess += "]"
        return mess
    
    def len(self):
        """ListeChainee -> int
        
        >>> l = ListeChainee()
        >>> l.append(1)
        >>> l.append(2)
        >>> l.append(3)
        >>> l.len()
        3"""
        nb = 0
        prec = self.__tete
        while prec != None:
            prec = prec.suivant()
            nb += 1
        return nb

    def get(self, ind):
        """ListeChainee, int -> Objet
        
        >>> l = ListeChainee()
        >>> l.append(1)
        >>> l.get(0)
        1
        >>> l.append(2)
        >>> l.append(3)
        >>> l.get(2)
        2
        >>> l.get(2)
        3"""
        assert self.__tete != None
        cpt = 0
        m = self.__tete
        while cpt < ind:
            assert m.suivant() != None
            m = m.suivant()
            cpt += 1
        return m.get()
    
    def delete(self, ind):
        """ListeChainee, int -> None
        
        >>> l = ListeChainee()
        >>> l.append(1)
        >>> l.append(2)
        >>> l.append(3)
        >>> l.delete(1)
        >>> print(l)
        [1, 3]
        >>> l.delete(0)
        >>> print(l)
        [3]"""
        assert ind < self.len()
        if ind == 0:
            self.__tete = self.__tete.suivant()
        else :
            prec = self.__tete
            for i in range(ind-1):
                prec = prec.suivant()
            prec.set_suiv(prec.suivant().suivant())
    
    def insert (self, val, ind):
        """ListeChainee, Objet, int -> None
        
        >>> l = ListeChainee()
        >>> l.append(1)
        >>> l.append(2)
        >>> l.append(3)
        >>> print(l)
        [1, 2, 3]
        >>> l.insert(8, 0)
        >>> print(l)
        [8, 1, 12, 2, 3]
        >>> l.insert(15, 4)
        >>> print(l)
        [8, 1, 12, 15, 3]"""
        assert ind < self.len()
        if ind == 0:
            self.__tete = Maillon(val, self.__tete)
        else :
            prec = self.__tete
            for i in range(ind-1):
                prec = prec.suivant()
            prec.set_suiv(Maillon(val, prec.suivant()))

    def contient(self, val):
        """Verifife si un nbr est dans la liste chainee"""
        if self.__tete == None:
            return False
        if self.__tete.get() == val:
            return True
        return self.__tete.contient(val)

    def indices_minimum(self):
        l_ind = []
        if self.__tete == None:
            return l_ind
        i_m = 0
        val_m = self.__tete.get()
        return self.__tete.indices_minimum(l_ind, i_m, val_m)
        
    
    def permute_pairs(self):
        """Permute chaque paire de maillons dans la liste chaînée."""
        if self.__tete is not None:
            self.__tete = self.__tete.permute_pairs_recursive() 

    def alternate_split(self):
        """Sépare la liste en deux listes en alternant les maillons."""
        list1 = ListeChainee()
        list2 = ListeChainee()
        if self.__tete is not None:
            self.__tete.alternate_split_recursive(list1, list2, True)
            return list1, list2

l = ListeChainee()
l.append(1)
l.append(-2)
l.append(10)
l.append(5)
l.append(4)
l.append(-2)
#print(l.contient(7))
#print(l.indices_minimum())
#print(l.permute_pairs())
l.alternate_split()
print(l)
