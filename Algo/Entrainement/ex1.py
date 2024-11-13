def trouver_couple(liste,k):
    if liste == []:
        return (-1,-1)
    else:
        for i in range(len(liste)-1):
            for j in range(len(liste)-1):
                if liste[i]*liste[j] == k:
                    return i,j
    return (-1,-1)

liste = [1,2,3,4,5]
print(trouver_couple(liste, 4))


def suite(n):
    if n == 0:
        return 3
    elif n == 1:
        return 2
    u_prev2 = 3
    u_prev1 = 2

    for i in range(2, n + 1):
        u_current = (u_prev1 + u_prev2) / 2
        u_prev2 = u_prev1
        u_prev1 = u_current
    return u_current

print(suite(3))
print(suite(2))
print(suite(1))


def separer(n,l):
    g = 0
    for d in range(len(l)):
        if l[d] < n:
            l[g], l[d] = l[d],l[g]
    return l

l = [2,3,10,0,3,14,4,4,9,32,1]
res = separer(5,l)
print(res)
