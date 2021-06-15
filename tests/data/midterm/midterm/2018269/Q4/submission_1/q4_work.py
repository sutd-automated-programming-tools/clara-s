def determinant(matrix):
    
    l = len(matrix)
    
    if l == 1:
        
        det = matrix[0][0]
        return det
              
    if l == 2:
        val1 = matrix[0][0] * matrix[1][1]
        val2 = matrix[0][1] * matrix[1][0]
        return val1 - val2
                  
    if l == 3:
        a = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        b = matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        c = matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])   
        return a - b + c
                  
    else:
        return None
    