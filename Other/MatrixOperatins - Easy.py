def MatrixOperations(matrix):
    colPos, rowPos, colMid, rowMid = 0,0,0,(len(matrix)//2)+1
    for index, row in enumerate(matrix):
        if index==1:
            colMid = (len(row)//2)+1
        if 1 in row:
            rowPos=index+1
            for idx, ele in enumerate(row):
                if ele == 1:
                    colPos = idx+1
                    break
    return abs(colMid-colPos)+abs(rowMid-rowPos)

print(MatrixOperations([[0],[1],[0]]))