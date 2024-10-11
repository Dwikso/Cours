def intrus(liste):
    unique = 0
    for num in liste:
        unique ^= num
    return unique


l = [1,2,3,5,7,5,2,1,3]
print(intrus(l))
