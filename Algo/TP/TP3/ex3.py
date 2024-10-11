def fusionner(l,deb,milieu,fin):
    part1, part2 = l[deb:milieu], l[milieu:fin]
    i, j, k = 0, 0, deb
    while i < len(part1) and j < len(part2):
        if part1[i] < part2[j]:
            l[k] = part1[i]
            i += 1
        else:
            l[k] = part2[j]
            j += 1
        k += 1
    while i < len(part1):
        l[k] = part1[i]
        i, k = i + 1, k + 1
    while j < len(part2):
        l[k] = part2[j]
        j, k = j + 1, k + 1

def tri_fusion(l,deb,fin):
    if fin-deb < 2:
        return
    else:
        milieu = (deb + fin)//2
        tri_fusion(l,deb,milieu)
        tri_fusion(l,milieu,fin)
        fusionner(l,deb,milieu,fin)
    return

print(tri_fusion(cree_liste(),0,len(cree_liste())))
