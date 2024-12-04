class ArbreBinaire:
    def __init__(self, racine=None):
        self.__racine = racine

    def est_vide(self):
        return self.__racine is None

    def est_dans_arbre(self, val):
        if self.est_vide():
            return False
        return self.__racine.est_dans_arbre(val)

    def maximum(self):
        if self.est_vide():
            return None
        return self.__racine.maximum()
    
    def un_fils(self):
        if self.est_vide():
            return []
        return self.__racine.un_fils()

    def internes(self):
        if self.est_vide():
            return []
        return self.__racine.internes()
    
    def feuilles_negatives(self):
        if self.est_vide():
            return []
        return self.__racine.feuilles_negatives()

    def hauteur(self):
        if self.est_vide():
            return 0
        return self.__racine.hauteur()


class Sommet:
    def __init__(self, val, fg=None, fd=None):
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
        return self.__fg is not None

    def aFD(self):
        return self.__fd is not None

    def estFeuille(self):
        return self.__fg is None and self.__fd is None

    def nb_sommets_dfs(self):
        nb1, nb2 = 0, 0
        if self.aFG():
            nb1 = self.__fg.nb_sommets_dfs()
        if self.aFD():
            nb2 = self.__fd.nb_sommets_dfs()
        return nb1 + nb2 + 1

    def insert_gauche(self, val):
        if self.__fg is None:
            self.__fg = Sommet(val)
        else:
            new_sommet = Sommet(val)
            new_sommet.__fg = self.__fg
            self.__fg = new_sommet

    def insert_droite(self, val):
        if self.__fd is None:
            self.__fd = Sommet(val)
        else:
            new_sommet = Sommet(val)
            new_sommet.__fd = self.__fd
            self.__fd = new_sommet
    
    def est_dans_arbre(self, val):
        if self.__val == val:
            return True
        if self.__fg is not None and self.__fg.est_dans_arbre(val):
            return True
        if self.__fd is not None and self.__fd.est_dans_arbre(val):
            return True
        return False

    def maximum(self):
        if self.aFD():
            return self.__fd.maximum()
        return self.__val

    def un_fils(self):
        sommets = []
        if (self.__fg is not None and self.__fd is None) or (self.__fd is not None and self.__fg is None):
            sommets.append(self.__val)
        if self.__fg is not None:
            sommets.extend(self.__fg.un_fils())
        if self.__fd is not None:
            sommets.extend(self.__fd.un_fils())
        return sommets
    
    def internes(self):
        sommets = []
        if not self.estFeuille():
            sommets.append(self.__val)
        if self.__fg is not None:
            sommets.extend(self.__fg.internes())
        if self.__fd is not None:
            sommets.extend(self.__fd.internes())
        return sommets

    def hauteur(self):
        hauteur_fg = self.__fg.hauteur() if self.__fg else 0
        hauteur_fd = self.__fd.hauteur() if self.__fd else 0
        return max(hauteur_fg, hauteur_fd) + 1
        
    def feuilles_negatives(self):
        feuilles = []
        if self.estFeuille() and self.__val < 0:
            feuilles.append(self.__val)
        if self.__fg is not None:
            feuilles.extend(self.__fg.feuilles_negatives())
        if self.__fd is not None:
            feuilles.extend(self.__fd.feuilles_negatives())
        return feuilles

racine = Sommet(10)
racine.insert_gauche(-5)
racine.insert_droite(20)

racine.fg().insert_gauche(-15)
racine.fg().insert_droite(0)

racine.fd().insert_gauche(15)
racine.fd().insert_droite(25)

arbre = ArbreBinaire(racine)

print("Est dans l'arbre (-15) :", arbre.est_dans_arbre(-15))
print("Est dans l'arbre (30) :", arbre.est_dans_arbre(30))
print("Maximum de l'arbre :", arbre.maximum())
print("Liste des sommets avec un seul fils :", arbre.un_fils())
print("Liste des sommets internes :", arbre.internes())
print("Liste des feuilles négatives :", arbre.feuilles_negatives())
print("Hauteur de l'arbre :", arbre.hauteur())

