class Sommet:
    def __init__(self, val, fg=None, fd=None):
        self.__val = val
        self.__fg = fg
        self.__fd = fd

    def get(self):
        return self.__val

    def fd(self):
        return self.__fg

    def aFG(self):
        return self.__fg != None

    def aFD(self):
        return self.__fd != None

    def estFeuille(self):
        return self.__fg == None and self.__fd == None


class ArbreBinaire:
    def __init__(self, racine=None):
        self.__racine = racine

    def cherche_bfs(self,valeur):
        if self.__racine != None:
            f = File()
            f.ajouter(self.__racine)
            while not f.est_vide():
                sommet = f.supprimer()
                if sommet.get() == valeur:
                    return sommet
                if sommet.aFG() != None:
                    f.ajouter(sommet.fg())
                if sommet.AFD() != None:
                    f.ajouter(sommet.fd())
            return None
        else:
            return None

    
    def cherche_dfs(self,val):
        assert self.__racine is not None
        pile = Pile()
        pile.empiler

    def nb_sommets_bfs(self):
        cpt = 0
        if self.__racine != None:
            f = File()
            f.ajouter(self.__racine)
            while not f.est_vide():
                cpt += 1
                if sommet.aFG():
                f.supprimer()
                if sommet.aFD():
                    f.supprimer()
            return cpt
        else:
            return 0

