class Maillon :

    def __init__(self, val, suiv=None):
        '''Maillon, Objet, Maillon -> Maillon
        construit un maillon d'une liste chainee.'''
        self.__val = val
        self.__suiv = suiv

    def get(self):
        return self.__val

    def suivant(self):
        return self.__suiv

    def set_suiv(self, m):
        self.__suiv = m

    def __str__(self):
        mess = str(self.__val)
        if self.__suiv != None:
            mess += ', '
        return mess


class ListeChainee :
    def __init__(self):
        self.__tete = None

    def __str__(self):
        mess = "["
        prec = self.__tete
        while prec != None:
            mess += prec.__str__()
            prec = prec.suivant()
        mess += "]"
        return mess

    def append(self, val):
        if self.est_vide():
            self.__tete = Maillon(val)
        else:
            prec = self.__tete
            while prec.suivant() != None:
                prec = prec.suivant()
            prec.set_suiv(Maillon(val))

    def len(self):
        nb = 0
        prec = self.__tete
        while prec != None:
            prec = prec.suivant()
            nb += 1
        return nb

    def get(self, ind):
        assert self.__tete != None
        cpt = 0
        m = self.__tete
        while cpt < ind:
            assert m.suivant() != None
            m = m.suivant()
            cpt += 1
        return m.get()
    
    def insert(self, val, ind):
        assert ind < self.len() 
        if ind == 0:
            self.__tete = Maillon(val, self.__tete)  
        else:
            prec = self.__tete
            for i in range(ind - 1):
                prec = prec.suivant()
            prec.set_suiv(Maillon(val, prec.suivant()))
    
    def delete(self, ind):
        assert ind < self.len()  
        if ind == 0:
            self.__tete = self.__tete.suivant()
        else:
            prec = self.__tete
            for i in range(ind - 1):
                prec = prec.suivant()
            prec.set_suiv(prec.suivant().suivant())  

    def appartient(self, val):
        courant = self.__tete
        while courant != None:
            if courant.get() == val:
                return True
            courant = courant.suivant()
        return False

    def est_vide(self):
        return self.__tete == None

    def nb_occ(self,val):
        nb = 0
        courant = self.__tete
        while courant != None:
            if courant.get() == val:
                nb += 1
            courant = courant.suivant()
        return nb
    
    def val_max(self):
        max = self.__tete.get()
        courant = self.__tete.suivant()
        while courant != None:
            if courant.get() > max:
                max = courant.get()
            courant = courant.suivant()
        return max

    def indices_min(self):
        if self.est_vide():
            return []

        courant = self.__tete
        min_valeur = courant.get()
        
        while courant is not None:
            if courant.get() < min_valeur:
                min_valeur = courant.get()
            courant = courant.suivant()

        
        indices = []
        courant = self.__tete
        index = 0
        
        while courant is not None:
            if courant.get() == min_valeur:
                indices.append(index)
            courant = courant.suivant()
            index += 1

        return indices
    
    def permute_tete_queue(self):
        if self.est_vide() or self.__tete.suivant() == None:
            return 
        
        prec = None
        courant = self.__tete
        
        while courant.suivant() != None:
            prec = courant
            courant = courant.suivant()
        
        courant.set_suiv(self.__tete.suivant())  
        prec.set_suiv(self.__tete)  
    
        self.__tete.set_suiv(None) 
        self.__tete = courant 

    def premier_repetition(self):
        if self.est_vide() or self.__tete.suivant() is None:
            return None  

        courant = self.__tete
        while courant is not None:
            valeur = courant.get()
            
            
            suivant = courant.suivant()
            while suivant is not None:
                if suivant.get() == valeur:
                    return valeur 
                suivant = suivant.suivant()
            
            courant = courant.suivant()

        return None


    def supprime_paires(self):
        if self.est_vide() or self.__tete.suivant() is None:
            return 

        index = 0
        courant = self.__tete
        precedent = None

        while courant is not None:
            if index % 2 == 0:
                if precedent is None:
                    self.__tete = courant.suivant()
                else:   
                    precedent.set_suiv(courant.suivant())
            else:
                precedent = courant
            courant = courant.suivant()
            index += 1

        



l = ListeChainee()

l.append(2)
l.append(0)
l.append(7)
l.append(2)
l.append(0)

# print(l.appartient(5))
# print(l.appartient(10))

# print(l.nb_occ(5))
# print(l.val_max())
print(l.indices_min())
print(l.supprime_paires())