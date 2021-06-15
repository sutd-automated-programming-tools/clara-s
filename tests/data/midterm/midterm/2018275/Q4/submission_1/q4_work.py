def determinant(matrix):
    if len(matrix) == 1:
        if len(matrix[0]) == 1:
            det = matrix[0][0]
        else:
            return None
    elif len(matrix) == 2:
        for i in matrix:
            row = len(i)
            if row ==2:
                det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
            else:
                return None
    elif len(matrix) == 3:
        for i in matrix:
            row = len(i)
            if row ==3:
                det = matrix[0][0]*(matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1])
                - matrix[0][1]*(matrix[2][0]*matrix[2][2] - matrix[1][2]*matrix[2][0])
                + matrix[0][2]*(matrix[2][0]*matrix[2][1] - matrix[1][1]*matrix[2][0])
                
            else:
                return None 
    return det     