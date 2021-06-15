def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        return None
    
    else:
        if len (matrix) == 1:
            det = matrix[0]
        elif len (matrix) == 2:
            det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
        elif len (matrix)  == 3:
            first_det = matrix[1][1]*matrix[2][2] - matrix[2][1]*matrix[1][2]
            second_det = matrix[1][0]*matrix[2][2] - matrix[2][0]*matrix[1][2]
            third_det = matrix[1][0]*matrix[2][1] - matrix[2][0]*matrix[1][1]
            a = matrix[0][0]
            b = matrix[0][1]
            c = matrix[0][2]
            det = a*first_det - b*second_det + c*third_det
    
    return det 