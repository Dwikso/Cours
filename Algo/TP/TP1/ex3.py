def matrix_diag(n):
    for i in range(len(n)):
        for j in range(len(n[i])):
            print(n[i][j], end=' ')
        print()

matrix_diag([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

