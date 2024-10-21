def fibonacci(n: int):
    if n <= 1:
        return n
    elif n >=2:
        return fibonacci(n-1) + fibonacci(n-2)

#print(fibonacci(3))

def fibo_inter(n):
    i = 0
    p,q = 0,1
    while i < n:
        i += 1
        p,q = q,p+q
    return p


def fibo(n,p=0, q=1):
    if n== 0:
        return p
    else:
        return fibo(n-1, q, p+q)


der occu_rec(mot,c):
    res = 0
    if mot == "":
        return res
    else:
        if mot[0] == c:
            res += 1
        return res + occu_rec(mot[1:],c)

print(occu_rec("abc",'a'))
