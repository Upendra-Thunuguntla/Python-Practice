from itertools import combinations as pe
def renameFile(newName, oldName):
    m = len(oldName)
    n = len(newName)
 
    lookup = [[0] * (n + 1) for i in range(m + 1)]
    print(lookup)
    for i in range(n+1):
        lookup[0][i] = 0
    print(lookup)
    for i in range(m + 1):
        lookup[i][0] = 1
    print(lookup)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if oldName[i - 1] == newName[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + lookup[i - 1][j]
                print(lookup,i,j)
            else:
                lookup[i][j] = lookup[i - 1][j]
                print(lookup)
    return lookup[m][n]%1000000007

print(renameFile("aba","ababa"))