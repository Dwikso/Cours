import random

def n_reines(n):
    table = [[(random.randint(0,1)) for _ in range(n)] for _ in range(n)]
    print(table)
n_reines(8)
