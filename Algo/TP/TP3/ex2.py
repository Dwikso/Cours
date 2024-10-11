class Pile:
    def __init__(self):
        self.__pile = []

    def empile(self,x):
        self.__pile.append(x)

    def depile(self):
        return self.__pile.pop()

    def est_vide(self):
        return len(self.__pile) == 0

    def __str__(self):
        return str(self.__pile)

    def get_first(self):
        return self.__pile[-1]

    def __len__(self):
        return len(self.__pile)



