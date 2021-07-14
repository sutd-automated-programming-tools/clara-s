def determinant(matrix):
    for line in matrix:
        if len(line)!=len(matrix):
            return None
    if len(matrix)==1:
        return matrix[0][0]
    elif len(matrix)==2:
        return (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])
    elif len(matrix)==3:
        p1 = matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])
        p2 = -matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])
        p3 = matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
        return p1+p2+p3