def matrix_modify(M):
    for row_no, row in enumerate(M):
        M[row_no] = row[:1] + [-1] + row[1:]


M = [[5, 2, 3], [6, 7, 8], [9, 8, 7]]
matrix_modify(M)
print(M)
