def intervalle_est_dans_liste(liste,n,m):
    for i in range(n,m+1):
        if i not in liste:
            return False
    return True


l = [4,1,2,3,5,7,5,2,1,3,6,9]
print(intervalle_est_dans_liste(l,3,12))
print(intervalle_est_dans_liste(l,3,6))

