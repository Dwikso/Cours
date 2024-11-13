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
    
    def ajoute_maillon(self, m):
        """ListeChainee, Maillon -> None
        
        >>> lc = ListeChainee()
        >>> lc.append(-1), lc.append(5), lc.append(-3), lc.append(-8), lc.append(14)
        >>> m = Maillon(5)
        >>> lc.ajoute_maillon(m)
        >>> print(lc)
        [-1, 5, -3, -8, 14, 5]
        >>> lc.supprimer_maillon(m)
        >>> print(lc)
        [-1, 5, -3, -8, 14]"""
        if self.est_vide():
            self.__tete = m
        else :
            prec = self.__tete
            while prec.suivant() != None :
                prec = prec.suivant()
            prec.set_suiv(m)
    
    def supprimer_maillon(self, m):
        """ListeChainee, Maillon -> None
        
        >>> lc = ListeChainee()
        >>> lc.append(-1), lc.append(5), lc.append(-3), lc.append(-8), lc.append(14)
        >>> m = Maillon(5)
        >>> lc.ajoute_maillon(m)
        >>> print(lc)
        [-1, 5, -3, -8, 14, 5]
        >>> lc.supprimer_maillon(m)
        >>> print(lc)
        [-1, -3, -8, 14]"""
        if self.__tete != None:
            if self.__tete == m:
                self.__tete = self.__tete.suivant()
            else :
                prec = self.__tete
                while prec != None and prec.suivant() != m:
                    prec = prec.suivant()
                if prec != None:
                    prec.set_suiv(m.suivant())
    
    def ajoute_liste(self, liste):
        """Construit une liste chainée à partir d'une liste passée en paramètre
        
        >>> lc = ListeChainee()
        >>> lc.ajoute_liste([1, 12, 3, 8, 14])
        >>> print(lc)
        [1, 12, 3, 8, 14]"""
        assert self.est_vide()
        self.__tete = Maillon(liste[0])
        prec = self.__tete
        for i in range(1, len(liste)):
            m = Maillon(liste[i])
            prec.set_suiv(m)
            prec = prec.suivant()
    
    def plus_grand(self, n, m):
        """Calcule la plus grande valeur d'un intervalle de la liste
        
        >>> lc = ListeChainee()
        >>> lc.ajoute_liste([1, 12, 3, 8, 14])
        >>> print(lc)
        [1, 12, 3, 8, 14]
        >>> lc.plus_grand(3, 9)
        8"""
        assert not self.est_vide() and n < m
        trouve = False
        prec = self.__tete
        mawi = None
        while prec != None:
            if n <= prec.get() <= m:
                if not trouve:
                    maxi = prec.get()
                    trouve = True
                elif maxi < prec.get():
                    maxi = prec.get()
        return maxi
        
    
    def supprimer_negatifs(self):
        """Supprime les éléments négatifs de la liste
        
        >>> lc = ListeChainee()
        >>> lc.append(-1), lc.append(12), lc.append(-3), lc.append(-8), lc.append(14)
        >>> lc.supprimer_negatifs()
        >>> print(lc)
        [12, 14]"""
        if self.__tete != None:
            prec = self.__tete
            pos = 0
            while prec != None:
                if prec.get() < 0:
                    prec = prec.suivant()
                    self.delete(pos)
                else :
                    prec = prec.suivant()
                    pos += 1
    
    def supprimer_doublons(self):
        """Supprime les doublons de la liste
        
        >>> lc = ListeChainee()
        >>> lc.append(1), lc.append(12), lc.append(3), lc.append(8), lc.append(14), lc.append(3)
        >>> lc.supprimer_doublons()
        >>> print(lc)
        [1, 12, 3, 8, 14]"""
        if self.__tete != None:
            l = []
            prec = self.__tete
            l.append(prec.get())
            while prec != None and prec.suivant() != None:
                if prec.suivant().get() in l:
                    prec.set_suiv(prec.suivant().suivant())
                else :
                    prec = prec.suivant()
                    l.append(prec.get())

    def supprimer_m_apres_n(self, m, n):
        assert n > 0 and  m > 0d and n + M >= self.len()
        prec1 = self.__tete
        for i in range(m - 1):
            prec1 = prec1.suivant()
        prec2 = prec1.suivant()
        for i in range(n):
            prec2 = prec2.suivant()
        prec1.set_suiv(prec2)


    def permute(self,l):
        m = self.len()
        assert 0 <= k < m
        val = self.get(k)
        self.set(k,self.get(n-k-1))
        self.set(k, self.get(n-k-1))

    def set(self, ind, val):
        assert 0 <=ind<self.len()
        prec = self.__tete
        for i in range(ind -1):
            prec = prec.suivant()
        prec.set_suiv(Maillon(val), prec.suivant())


    def intersection(self, lc):
        m = self.len()
        m = lc.len()
        diff = n-m
        prec1 = self.__tete
        prec2 = lc.__tete
        if diff > 0:
            for i in range(diff):
                prec1 = prec.suivant()
        else:
            for i in range((-diff)):
                prec2 = prec2.suivant()
        while prec1 != None:
            if prec1 == prec2:
                return prec1
            prec1 = prec1.suivant()
            prec2 = prec2.suivant()
        return None


    def inverser(self):
        if self.__tete == None or self.__tete.suivant() == None:
            return
        prec = None
        courant, suivant = self.__tete, self.__tete
        while courant != None:
            suivant = courant.suivant()
            courant.set_suiv(prec)
            precedent = courant
            courant = suivant
    
    def fusion(self, lc2):
        """Fusionne deux listes chaînées en ajoutant les éléments de lc2 à la fin de la liste actuelle.
        
        >>> lc1 = ListeChainee()
        >>> lc1.append(1)
        >>> lc1.append(2)
        >>> lc1.append(3)
        
        >>> lc2 = ListeChainee()
        >>> lc2.append(4)
        >>> lc2.append(5)
        
        >>> lc1.fusion(lc2)
        >>> print(lc1)
        [1, 2, 3, 4, 5]
        """
        if self.__tete == None:
            self = lc
        elif lc.__tete != None:
            if self.__tete.get() > lc.__tete.get():
                self,lc = lc,self
        courant = self.__tete
        suivant = lc.__tete
        prec = courant
        while courant != None:
            if courant.get() <= suivant.get()
                prec = courant
                courant = courant.suivant()
            else:
                prec.set_suiv(suivant)
                courant,suivant = suivant,courant
            if suivant != None:
                prec.set_suiv(suivant)
