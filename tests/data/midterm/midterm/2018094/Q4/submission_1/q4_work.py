def determinant(matrix):
    if len(matrix) < 1 or len(matrix) > 3:
        return None
    for i in matrix:
        if len(i) != len(matrix):
            return None
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    elif len(matrix) == 3:
        one = matrix[0][0] * ((matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1]))
        two = matrix[0][1] * ((matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0]))
        three = matrix[0][2] * ((matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0]))
        
        return one - two + three