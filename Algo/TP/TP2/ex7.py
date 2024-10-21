def suite_syracuse(n, conteur=0):
    if n == 1:
        return conteur
    if n % 2 == 0:
        return suite_syracuse(n//2, conteur+1)
    else:
        return suite_syracuse(3 * n + 1, conteur+1)


print(suite_syracuse(10))
print(suite_syracuse(7))
