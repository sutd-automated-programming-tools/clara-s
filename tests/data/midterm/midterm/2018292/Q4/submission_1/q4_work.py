def determinant(matrix):
    x = matrix[0]
    if len(x) == 1:
        d = x[0]
        return d
    elif len(x) == 2:
        d = ((x[0]*matrix[1][1]) - (x[1]*matrix[1][0]) )
        return d
    elif len(x) == 3:
        d = ( ( x[0] * ( (matrix[1][1]*matrix[2][2]) - (matrix[1][2]*matrix[2][1]) ) ) - ( x[1] * ( (matrix[1][0]*matrix[2][2]) - (matrix[1][2]*matrix[2][0]) )) + ( x[2] * ( (matrix[1][0]*matrix[2][1]) - (matrix[1][1]*matrix[2][0]) )))
        return d
    elif len(x) != len(matrix[1]):
        return None
    