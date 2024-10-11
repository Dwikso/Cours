import random
import time


def cree_liste():
    n = 10000000
    liste = list(range(n))
    liste.append(n)
    random.shuffle(liste)
    return liste


def tri_insertion(l):
    start_time = time.time()
    for i in range(1,len(l)):
        ref = l[i]
        j = i-1
        while j >= 0 and l[j] > ref:
            l[j+1] = l[j]
            l[j] = ref
            j -= 1
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Temps écoulé (tri insertion) : {elapsed_time:.8f} secondes")
    return 
    



def fussionner(a,b):
    c = []
    n,m = len(a),len(b)
    i,j = 0,0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i == len(a):
        for k in range(j, len(b)):
            c.append(b[k])
    else:
        for k in range(i, len(a)):
            c.append(a[k])
    return c

def tri_fusion(a):
    start_time = time.time()
    n = len(a)
    if n <= 1:
        return a
    m = n//2


    end_time = time.time()
    elapsed_time = end_time - start_time
    return(f"Temps écoulé (tri fusion) : {elapsed_time:.8f} secondes")


liste = cree_liste()
liste2 = liste[:]
print(tri_insertion(liste))
print(tri_fusion(liste2))
