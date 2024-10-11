def n_premiers_iterative(n):
    somme = [1]
    for i in range(1,n):
        somme.append(3*somme[i-1] + 1)
    return somme

#print(n_premiers_recursive(3))

def n_premiers_recursive(n):
    if n == 1:
        return [1]
    else:
        suite = n_premiers_recursive(n-1)
        suite.append(3*suite[-1] + 1)
    return suite 
print(n_premiers_recursive(3))
