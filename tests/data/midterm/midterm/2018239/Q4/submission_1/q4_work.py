def determinant(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    for i in range(len(matrix)-1):
        if len(matrix[i])>len(matrix[i+1]):
            return None
    if ((len(matrix[0]))==2 and (len(matrix[1])==2)):
        return (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])
    if len(matrix)==3:
        return (matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1]))-(matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0]))+matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
