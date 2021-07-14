def determinant(matrix):
    a=len(matrix)
    b=len(matrix[0])
    if a!=b:
        return None
    else:
        if a==1:
            return matrix[0][0]
        if a==2:
            return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        if a==3:
            return matrix[0][0]*(matrix[2][2]*matrix[1][1]-matrix[2][1]*matrix[1][2])-matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])+matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])