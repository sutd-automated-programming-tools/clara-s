def determinant(matrix):
    length = len(matrix)
    if length == 1:
        return matrix[0][0]
    
    elif length == 2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    
    elif length == 3:
        a =  matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])
        b = matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])
        c = matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
    return a-b+c