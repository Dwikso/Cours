def somme_inverse_recursive(n):
    if n == 1:
        return 1
    else:
        return (1/n**2) + somme_inverse_iterative(n-1)

#print(somme_inverse_recursive(2))

def somme_inverse_iterative(n):
    somme = 0
    for i in range(1,n+1):
        somme += 1/i**2
    return somme

print(somme_inverse_iterative(2))
