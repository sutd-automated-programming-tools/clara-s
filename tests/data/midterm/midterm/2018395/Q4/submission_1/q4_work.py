def determinant(matrix):
    c = []
    d = 0
    
    if len(matrix) == 1:
        for i in matrix:
            for j in i:
                d = d + j
        return d
    
    elif len(matrix) == 2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    
    elif len(matrix) == 3:
        
        e = (matrix[0][0]* (matrix[1][1]*matrix[2][2]-matrix[2][1]*matrix[1][2]))-(matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[2][0]*matrix[1][2]))+(matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[2][0]*matrix[1][1]))

        return e
    
  