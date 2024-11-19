from typing import Any

def CreateMatrix(rows:int, cols:int) -> dict[Any, Any]:
    mat = {}
    i = 0
    a = 0
    while(i < rows):
        mat[i] = {}
        j = 0
        while(j < cols):
            mat[i][j] = a
            j = j+1
            a = a + 1
        i = i+1
    
    return mat

mat = CreateMatrix(5, 6)

for r in mat.keys():
    for c in mat[0].keys():
        print(mat[r][c], ", ", end="")
    print("\n")
    
print(mat[2][3])