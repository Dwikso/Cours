class Maillon:
    def __init__(self, val, suiv=None):
        self.__val = val
        self.__suiv = suiv

    def set_suiv(self,m):
        self.__suiv = m

    def __str__(self):
        mess = str(self.__val)
        if self.__suiv != None:
            mess += ' '
        return mess

    def delete(self, i):
        assert ind < self.len()
        if ind == 0:
            self.__suiv = self.__suiv.__suiv
        else:
            self.__suiv.delete(i - 1)

    def insert(self,val,i):
        if ind == 0:
            self.__suiv = Maillon(val,self.__suiv)
    
    def copy(self):
        l = listeChaine()
        if not self.est_vide():
            l.__tete = self.__tete.copy()
        return l

class ListeChaine:
    def __init__(self):
        self.__tete = None

    def append(self,val):
        if self.est_vide():
            self.__tete = Maillon(val)
        else:
            prec = self.__tete
            while prec.__suivant() != None:
                prec = prec.__suivant()
            prec.set_suiv(Maillon(val))

    def __str__(self):
        mess = "["
        prec = self.__tete
        while prec != None:
            mess += prec.__str__()
            prec = prec.__suivant()
        mess += "]"
        return mess
    
    def len(self):
        prec = self.__tete
        i = 0
        while prec != None:
            i += 1
            prec = prec.__suivant()
        return i
    
    def get(self,i):
        assert ind < self.len()
        if ind == 0:
            return self.__val
        return self.__suivant.get(i-1)


    def delete(self,i):
        assert i < self.len()
        if i == 0:
            self.__tete = self.__tete.__suivant()
        else:
            self.__tete.delete(i -  1)
    def est_vide(self):
        return self.__tete == None

    def __getitem__(self,i):
        return self.get(i)

    def insert(self,i,val):
        assert i <= self.len()
        if i == 0:
            self.__tete = Maillon(val,self.__tete)
        else:
            self.__tete.inser(val,i-1)


    def copy(self):
        new_list = ListeChaine()
        if not self.est_vide():
            new_list.__tete = self.__tete.copy()
        return new_list

class Pile:
    def __init__(self):
        self.l = ListeChaine()

    def est_vide(self):
        return self.l.est_vide()

    def sommet(self):
        elt = self.l.get(0)
        self.l.delete(0)
        return elt
