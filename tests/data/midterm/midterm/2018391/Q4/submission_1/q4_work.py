def determinant(matrix):
    if len(matrix)==1:
        for i in matrix:
            determinant(matrix)=i
    elif len(matrix)==4:
        for i in matrix:
            determinant(matrix)=matrix[0]*matrix[3]-matrix[1]*matrix[2]
    elif len(matrix)==9:
        for i in matrix:
            determinant(matrix)=matrix[0]*matrix[4]*matrix[8]-matrix[5]*matrix[7]-matrix[1]*matrix[3]*matrix[8]-matrix[5]*matrix[6]+matrix[2]*matrix[3]*matrix[7]-matrix[4]*matrix[6]
    return (determinant(matrix))
    else:
        return None
