def intersection_liste(liste1, liste2):
    intersection = []
    for element in liste1:
        if element in liste2:
            intersection.append(element)
    return intersection


print(intersection_liste([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]))
print(intersection_liste([1, 2, 3, 4, 5], [6, 5, 4, 3, 2]))
print(intersection_liste([1, 2, 3, 4, 5], [7, 8, 9, 10, 11]))
