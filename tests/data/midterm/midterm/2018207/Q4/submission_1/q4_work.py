def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        return None
    
    else:
        if len(matrix) == 1:
            return matrix[0][0]
        
        elif len(matrix) == 2:
            return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        
        elif len(matrix) == 3:
            c1 = matrix[0][0]*determinant([[matrix[1][1],matrix[1][2]],[matrix[2][1],matrix[2][2]]])
            c2 = matrix[0][1]*determinant([[matrix[1][0],matrix[1][2]],[matrix[2][0],matrix[2][2]]])
            c3 = matrix[0][2]*determinant([[matrix[1][0],matrix[1][1]],[matrix[2][0],matrix[2][1]]])
            
            return c1 - c2 + c3