class ListeChaineeRec:
    def __init__(self):
        """ListeChaineeRec -> ListeChaineeRec"""
        self.__tete = None

    def len(self):
        """ListeChaineeRec -> int"""
        if self.est_vide():
            return 0
        else :
            return self.__tete.len()
    
    def append(self, val):
        """ListeChaineeRec (inout), Objet -> None
        
        >>> l = ListeChaineeRec()
        >>> print(l)
        []
        >>> l.append(1)
        >>> print(l)
        [1]
        >>> l.append(2)
        >>> l.append(3)
        >>> print(l)
        [1, 2, 3]"""
        if self.est_vide():
            self.__tete = MaillonRec(val)
        else :
            self.__tete.append(val)
    
    def get(self, ind):
        """ListeChaineeRec, int -> Objet
        
        >>> l = ListeChaineeRec()
        >>> l.append(1)
        >>> l.get(0)
        1
        >>> l.append(2)
        >>> l.append(3)
        >>> l.get(1)
        2
        >>> l.get(2)
        3"""
        assert ind < self.len()
        return self.__tete.get(ind)
    
    def set(self, ind, val):
        """ListeChaineeRec, int, Objet -> None
        
        >>> l = ListeChaineeRec()
        >>> l.append(1)
        >>> l.get(0)
        1
        >>> l.set(0, 5)
        >>> l.append(2)
        >>> l.append(3)
        >>> l.get(2)
        3
        >>> l.set(2, 10)
        >>> print(l)
        [5, 2, 10]"""
        assert ind < self.len()
        self.__tete.set(ind, val)

    def delete(self, ind):
        """ListeChainneeRec, int, None
        
        >>> l = ListeChaineeRec()
        >>> l.append(1)
        >>> l.append(2)
        >>> l.append(3)
        >>> l.delete(0)
        >>> print(l)
        [1, 3]
        >>> l.delete(0)
        >>> print(l)
        [3]"""
        assert ind < self.len()
        if ind == 0:
            self.__tete = self.__tete.suivant()
        else :
            self.__tete.delete(ind - 1)
    
    def insert(self, val, ind):
        """Liste!chaineeRec, Objetn int -> None
        
        >>> l = ListeChaineeRec()
        >>> l.append(1)
        >>> l.append(2)
        >>> l.append(3)
        >>> print(l)
        [1, 2, 3]
        >>> l.insert(8, 0)
        >>> print(l)
        [8, 1, 2, 3]
        >>> l.insert(12, 2)
        >>> print(l)
        [8, 1, 12, 2, 3]
        >>> l.insert(15, 4)
        >>> print(l)
        [8, 1, 12, 2, 15, 3]"""
        assert ind < self.len()
        if ind == 0:
            self.__tete = MaillonRec(val, self.__tete)
        else :
            self.__tete.insert(val, ind - 1)
    
    def copy(self):
        """ListeChaineeRec -> ListeChaineeRec"""
        l = ListeChaineeRec()
        if not self.est_vide():
            l.__tete = self.__tete.copy()
        return l
    
    def construire(self,l):
        assert self.est_vide()
        if len(l) != 0:
            self.__tete = MaillonRec(l[0])
            self.__tete.construire(l[1:])

    def maxi(self):
        assert not self.est_vide()
        return self.__tete.maxi()

    def insert_liste(self,l,pos):
        assert assert 0 <=pos < self.len()
        if len(l) != 0:
            if pos == 0:
                self.__tete = MaillonRec(l[0], self.__tete)
                self.__tete.insert_liste(l[:], 1)
            else:
                self.__tete.insert_liste(l,pos)

    def supprimer_negatifs(self):
        if not self.est_vide():
            while self.__tete != None and self.__tete.get() < 0:
                self.__tete = self.__tete.suivant()
            if self.__tete != None:
                self.__tete.supprimer_negatifs()

class MaillonRec:
    def __init__(self, val, suiv = None):
        """MaillonRec, Objet, MaillonRec -> MaillonRec"""
        self.__val = val
        self.__suiv = suiv
    
    def len(self):
        """MaillonRec -> int"""
        if self.__suiv == None:
            return 1
        else :
            return 1 + self.__suiv.len()
        
    def __str__(self):
        """MaillonRec -> str
        
        >>> m = MaillonRec(1)
        >>> print(m)
        1
        >>> m2 = MaillonRec(2, m)
        >>> print(m2)
        2, 1"""
        mess = str(self.__val)
        if self.__suiv != None:
            mess += ", " + self.__suiv.__str__()
        return mess
    
    def append(self, val):
        """MaillonRec, Objet -> None"""
        if self.__suiv == None:
            self.__suiv = MaillonRec(val)
        else :
            self.__suiv.append(val)
    
    def get(self, ind):
        """MaillonRec, ind -> Objet"""
        assert ind < self.len()
        if ind == 0:
            return self.__val
        else :
            return self.__suiv.get(ind - 1)
    
    def set(self, ind, val):
        """MaillonRec (inout), int, Objet -> None"""
        assert ind < self.len()
        if ind == 0:
            self.__val = val
        else :
            self.__suiv.set(ind - 1, val)
    
    def delete(self, ind):
        """MaillonRec, int -> None"""
        assert ind < self.len()
        if ind == 0:
            self.__suiv = self.__suiv.__suiv
        else :
            self.__suiv.delete(ind - 1)
    
    def insert(self, val, ind):
        """MaillonRec, Objet, int -> None"""
        assert ind < self.len()
        if ind == 0:
            self.__suiv = MaillonRec(val, self.__suiv)
        else :
            self.__suiv.insert(val, ind - 1)
    
    def copy(self):
        """MaillonRec -> MaillonRec"""
        m = MaillonRec(self.__val)
        if self.__suiv is not None:
            m.__suiv = self.__suiv.copy()
        return m

    def construire(self,l):
        if len(l) != 0:
            m = MaillonRec(l[0])
            self.__suiv = m
            self.__suiv.construire(l[1:])

    def maxi(self):
        if self.__suiv == None:
            return self.__val
        maxi1 = self.__suiv.maxi()
        return max(self.__val, maxi1)

    def insert_liste(self,l,pos):
        if len(l) != 0:
            if pos == 1:
                self.__suiv = MaillonRec(l[0], self.__suiv)
                self.__suiv.insert_liste(l,pos-1)

    def supprimer_negatifs(self):
        if self.__suiv != None:
            if self.__suiv.__val < 0:
                self.__suiv = self.__suiv.__suiv
                self.supprimer_negatifs()
            else:
                self.__suiv.supprimer_negatifs()
