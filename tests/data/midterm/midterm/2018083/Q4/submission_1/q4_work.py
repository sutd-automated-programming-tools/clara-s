def determinant(matrix):
    out=[]
    length=len(matrix)
    if not (1<=length<=3):
        return None
    for i in matrix:
        if len(i)!=length:
            return None
    if length == 1:
        return matrix[0][0]
    elif length == 2:
        out=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        return out
    else:
        out=matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])-matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])+matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
        return out