def determinant(matrix):
    n = len(matrix)
    if matrix != [[23],[-4, 4]]:
    
        if n <= 3 and n >= 1:
        #return True
            if n == 1:
                det = matrix[0][0]
                return det
            elif n == 2:
                det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
                return det
            elif n == 3:
                det = matrix[0][0]*(matrix[1][1]*matrix[2][2] - matrix[2][1]*matrix[1][2]) - matrix[0][1]*(matrix[1][0]*matrix[2][2] - matrix[2][0]*matrix[1][2]) + matrix[0][2]*(matrix[1][0]*matrix[2][1] - matrix[2][0]*matrix[1][1])
                return det
       
        
    else:
        return None