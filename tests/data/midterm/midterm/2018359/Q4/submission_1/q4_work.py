def determinant(matrix):
    dim=len(matrix)
    if dim<1 or dim>3:
        return None
    for i in matrix:
        if len(i)!=dim:
            return None
    if dim==1:
        return matrix[0][0]
    elif dim==2:
        detval= (matrix[0][0]*matrix[1][1])- (matrix[0][1]*matrix[1][0])
        return detval
    elif dim==3:
        firstdet= matrix[0][0] * (matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1])
        seconddet= -1 * (matrix[0][1]*(matrix[1][0]*matrix[2][2] - matrix[2][0]*matrix[1][2]))
        thirddet= matrix[0][2]*(matrix[2][1]*matrix[1][0] - matrix[1][1]*matrix[2][0])
        detval= firstdet+seconddet+thirddet
        return detval