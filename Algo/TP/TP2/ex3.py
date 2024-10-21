def suite_n_terme(n):
    somme_u = 4
    somme_v = 5
    for i in range(n):
        somme_u, somme_v = ((somme_u + somme_v) / (2)), ((somme_u * somme_v) ** (1/2))
    return somme_u, somme_v

print(suite_n_terme(20))
