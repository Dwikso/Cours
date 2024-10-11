def appartient(n, liste):
    if liste == []:
        return False
    else:
        for i in range(len(liste)):
            if n == liste[i]:
                return True
        return False

print(appartient(1, [1, 2, 3]))
