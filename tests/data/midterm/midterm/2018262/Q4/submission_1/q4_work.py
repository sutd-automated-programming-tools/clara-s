def determinant(matrix):
    row_length = len(matrix[0])
    if len(matrix) == 1:
            det = matrix[0][0]
            return det
    
    for row in matrix[1:]:
        if len(row) != row_length:
            return None
        
        else:
            if row_length == 2:
                det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
                return det
            elif row_length == 3:
                det1 = matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]
                det2 = matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]
                det3 = matrix[1][0] * matrix[2][1] - matrix[2][0] * matrix[1][1]
                det = matrix[0][0] * det1 - matrix[0][1] * det2 + matrix[0][2] * det3
                return det
        