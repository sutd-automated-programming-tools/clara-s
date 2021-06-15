def determinant(matrix):
    for i in range(len(matrix)-1):
        if len(matrix[i]) != len(matrix[i+1]):
            return None
        else:
            continue
    row=len(matrix)
    col=len(matrix[0])
    if row==1:
        return matrix[0][0]
    if row==2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    if row==3:
        return matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])-matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[2][0]*matrix[1][2])+matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[2][0]*matrix[1][1])