def determinant(matrix):
    if len(matrix) == 1:
        return (matrix[0][0])
                
    elif len(matrix) == 2:
        for i in matrix:
            if len(matrix) != len(matrix[0]):
                return None
                    
            
            else:
                det = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
                return det
                
    elif len(matrix) == 3:
        for i in matrix:
            a = matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])
            b = matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[2][0]*matrix[1][2])
            c = matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[2][0]*matrix[1][1])

        det = a-b+c
                
        return det
    
   