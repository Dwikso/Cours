class ArbreBinaire:
    def __init__(self, racine = None):
        self.__racine = None

    def est_dans_arbre(self,val):
        if self.__racine.estFeuille():
            return False
        if self.__racine.get() == val:
            return True
        else:
            return self.__racine.est_dans_arbre(val)
 
    def maximum(self):
        if self.__racine is None:
            return None
        return self.__racine.maximum()
    
    def permute(self):
        self.__fg, self.__fd = self.__fd, self.__fg
        if self.aFG():
            self.__fg.permute()
        if self.aFD():
            self.__fd.permute()
    
    def miroir(self,a):
        if self.get() != a.get():
            return False
        if (self.aFG() and not a.aFD()) or (self.aFD() and not a.aFG()):
            return False
        if (not self.aFG() and a.aFD()) or (not self.aFD() and a.aFG()):
            return False
        b1,b2 = True, True
        if self.aFG():
            b1 = self.__fg.miroir(a.__fg)
        if self.aFD():
            b2 = self.__fd.miroir(a.__fd)
        return b1 and b2


class Sommet:
    def __init__(self,val,fg=None,fd=None):
        self.__val = val
        self.__fg = fg
        self.__fd = fd

    def get(self):
        return self.__val

    def fd(self):
        return self.__fd

    def fg(self):
        return self.__fg

    def aFG(self):
        return self.__fg != None

    def aFD(self):
        return self.__fd != None

    def estFeuille(self):
        return self.__fg == None and self.__fd == None

    def nb_sommets_dfs(self):
        nb1, nb2 = 0,0
        if self.aFG():
            nb1 = self.__fg.nb_sommets_dfs()
        if self.aFD():
            nb2 = self.__fd.nb_sommets_dfs()
        return nb1 + nb2 + 1

    def insert_gauche(self,val):
        if self.__fg is None:
            self.__fg = Sommet(val)
        else:
            new_sommet = Sommet(val)
            new_sommet.__fg = self.__fg
            self.__fg = new_sommet

    def insert_droite(self,val):
        if self.__fd is None:
            self.__fd = Sommet(val)
        else:
            new_sommet = Sommet(val)
            new_sommet.__fd = self.__fd
            self.__fd = new_sommet
    
    def lesFeuilles(self):
        feuilles = []
        if self.estFeuille():
            feuilles.append(self.__val)
        else:
            if self.aFG():
                feuilles_gauche = self.__fg.lesFeuilles()
                feuilles.append(feuilles)
            if self.aFD():
                feuilles_droite = self.__fd.lesFeuilles()
                feuilles.append(feuilles_droite)
        return feuilles

    def plus_grande_valeur(self):
        max_valeur = self.__val
        if self.aFG():
            max_valeur = max(max_valeur,self.__fg.plus_grande_valeur())
        if self.aFD():
            max_valeur = max(max_valeur,self.__fd.plus_grande_valeur())
        return max_valeur


    def valeur_superieur_k(self,k):
        valeurs = []
        if self.__val > k:
            valeurs.append(self.__val)
        if self.aFG():
            valeurs_gauche = self.__fg.valeur_superieur_k(k)

            for valeur in valeurs_gauche:
                valeurs.append(valeur)
        if self.aFD():
            valeurs_droite = self.__fd.valeur_superieur_k(k)
            for valeur in valeurs_droite:
                valeurs.append(valeur)
        return valeurs
    
     def miroir(self,a):
        if self(.est_vide() and not arb.est_vide()) or (not self.est_vide() and arb.est_vide()):
            return False
        if self.est_vide() :
            return self.__racine.miroir(a.__racine)
