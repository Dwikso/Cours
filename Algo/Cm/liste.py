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
        assert self.__tete != None
        cpt = 0
        m = self.__tete
        while cpt < i:
            assert m.__suivant() != None
            m = m.__suivant()
            cpt += 1
        return m.get()

    def delete(self,i):
        assert i < self.len()
        if i == 0:
            self.__tete = self.__tete.__suivant()
        else:
            prec = self.__tete
            for i in range(i - 1):
                prec = prec.__suivant()
            prec.set_suiv(prec.__suivant().suivant())

    def est_vide(self):
        return self.__tete == None

    def __getitem__(self,i):
        return self.get(i)

    def insert(self,i,val):
        assert i <= self.len()
        if i == 0:
            self.__tete = Maillon(val,self.__tete)
        else:
            prec = self.__tete
            for i in range(i - 1):
                prec = prec.__suivant()
            prec.set_suiv(Maillon(val,prec.__suivant()))


