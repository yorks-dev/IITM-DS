def unique(L):
    L_uniq = [ ]
    for i in range(0, len(L)):
        if not(L[i] in L[i + 1: ]):
            L_uniq.append(L[i])
    return L_uniq

List = [1, 0, 0, 2, 1, 2, 5, 6, 6]
print(unique(List))