class ArbreBinaire:
    def __init__(self, racine = None):
        self.__racine = racine  # La racine peut être initialisée directement ici

    def est_dans_arbre(self, val):
        if self.__racine is None:  # Si l'arbre est vide
            return False
        return self.__racine.est_dans_arbre(val)
 
    def maximum(self):
        if self.__racine is None:
            return None
        return self.__racine.maximum()

    def ajoute(self, val):
        if self.__racine is None:
            self.__racine = Sommet(val)
        else:
            self.__racine.ajoute(val)

    def supprime(self, val):
        if self.__racine is not None:
            self.__racine = self.__racine.supprime(val)

    def estABR(self):
        if self.__racine is None:
            return True
        return self.__racine.estABR()


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

    def lesFeuilles(self):
        feuilles = []
        if self.estFeuille():
            feuilles.append(self.__val)
        else:
            if self.aFG():
                feuilles += self.__fg.lesFeuilles()  # Ajout des feuilles du sous-arbre gauche
            if self.aFD():
                feuilles += self.__fd.lesFeuilles()  # Ajout des feuilles du sous-arbre droit
        return feuilles

    def plus_grande_valeur(self):
        max_valeur = self.__val
        if self.aFG():
            max_valeur = max(max_valeur, self.__fg.plus_grande_valeur())
        if self.aFD():
            max_valeur = max(max_valeur, self.__fd.plus_grande_valeur())
        return max_valeur

    def valeur_superieur_k(self, k):
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
    
    def ajoute(self, val):
        if val < self.__val:
            if self.aFG():
                self.__fg.ajoute(val)
            else:
                self.__fg = Sommet(val)
        elif val > self.__val:
            if self.aFD():
                self.__fd.ajoute(val)
            else:
                self.__fd = Sommet(val)

    def supprime(self, val):
        if val < self.__val:
            if self.aFG():
                self.__fg = self.__fg.supprime(val)
        elif val > self.__val:
            if self.aFD():
                self.__fd = self.__fd.supprime(val)
        else:  # Si on trouve le nœud à supprimer
            if not self.aFG() and not self.aFD():  # Pas de sous-arbre
                return None
            elif not self.aFG():  # Pas de sous-arbre gauche
                return self.__fd
            elif not self.aFD():  # Pas de sous-arbre droit
                return self.__fg
            else:  # Cas où il y a deux sous-arbres
                successeur = self.__fd.trouve_min()
                self.__val = successeur.get()
                self.__fd = self.__fd.supprime(successeur.get())
        return self

    def trouve_min(self):
        # Trouver le minimum dans le sous-arbre droit
        if self.aFG():
            return self.__fg.trouve_min()
        return self

    def estABR(self, min_val=None, max_val=None):
        if (min_val is not None and self.__val <= min_val) or (max_val is not None and self.__val >= max_val):
            return False

        gauche_est_abr = True
        if self.aFG():
            gauche_est_abr = self.__fg.estABR(min_val, self.__val)

        droite_est_abr = True
        if self.aFD():
            droite_est_abr = self.__fd.estABR(self.__val, max_val)

        return gauche_est_abr and droite_est_abr

    def tri_arbre(self):
        abr = ArbreBinaire
        for i in range(len(l)):
            abr.ajoute(l[i])
        l2 = abr.parcours_infixe()
        for i in range(len(l)):
            l[i] = l2[i]

    def parcours_infixe(self):
        l=[]
        if self.aFG():
            l+= self.__fg.parcours_infixe()
        l.append((self.get()))
        if self.aFD():
            l += self.__fd.toStr_infixe()
        return chaine

    def profondeur(self, val, niveau=0):
        # Si la valeur recherchée est égale à la valeur du nœud actuel
        if val == self.__val:
            return niveau  # La profondeur est le niveau actuel

        # Si la valeur recherchée est inférieure à la valeur du nœud actuel
        elif val < self.__val:
            # Si le sous-arbre gauche existe, chercher dans le sous-arbre gauche
            if self.aFG():
                return self.__fg.profondeur(val, niveau + 1)
            else:
                return -1  # La valeur n'est pas présente dans l'arbre

        # Si la valeur recherchée est supérieure à la valeur du nœud actuel
        elif val > self.__val:
            # Si le sous-arbre droit existe, chercher dans le sous-arbre droit
            if self.aFD():
                return self.__fd.profondeur(val, niveau + 1)
            else:
                return -1  # La valeur n'est pas présente dans l'arbre


# Création de l'arbre binaire de recherche (ABR)
racine = Sommet(10)
racine.insert_gauche(5)
racine.insert_droite(15)
racine.fg().insert_gauche(3)
racine.fg().insert_droite(7)
racine.fd().insert_gauche(12)
racine.fd().insert_droite

print(racine.estABR())  # Devrait renvoyer True, car l'arbre est un ABR


