def determinant(matrix):
    #matrix = [[n],[n]]
    if len(matrix) == 1:
        det = matrix
        return det
    print(determinant([[100]]))
    elif len(matrix) == 2:
        if len(matrix[0]) == len(matrix[1]):
            det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
            return det
        else:
            return None
        print(matrix)
    elif len(matrix) == 3:
        if len(matrix[0]) == len(matrix[1]) and len(matrix[1]) == len(matrix[2]):
            det =  matrix[0][0] * ((matrix[1][1] * matrix[2][2])- (matrix[2][1]* matrix[1](2])) - matrix[0][1] * ((matrix[1][0] * matrix[2][2] )-(matrix[2][0] * matrix[2][1] ) + matrix[0][2] * ((matrix[1][0] * matrix[2][1]) - (matrix[2][0] * matrix[1][1]))
            return det
        else:
            return None