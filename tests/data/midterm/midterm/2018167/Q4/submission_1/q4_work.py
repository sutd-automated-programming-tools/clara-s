def determinant(matrix):
    if len(matrix)==1:
        for n in matrix:
            return n[0]
    if len(matrix)==2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    
    if len(matrix)==3:
        return matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])-matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[2][0]*matrix[1][2])+matrix[0][2]*(matrix[2][1]*matrix[1][0]-matrix[1][1]*matrix[2][0])
            
       