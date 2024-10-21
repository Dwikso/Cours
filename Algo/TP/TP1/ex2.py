def repetition(liste):
    liste2 = []
    for i in range(len(liste)):
        if liste[i] in liste2:
            return liste[i]
        else:
            liste2.append(liste[i])
    return -1

l = [1,2,3,5,7,5,2,12,1]
print(repetition(l))



