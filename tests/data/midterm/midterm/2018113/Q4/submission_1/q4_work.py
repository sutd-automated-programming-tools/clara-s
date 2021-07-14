def determinant(matrix):
    x = matrix
    len_x = len(matrix)
    len_y = len(matrix[0])
    if len_x != len_y:
        return None
    if len_x == 1:
        return x[0][0]
    elif len_x == 2:
        return x[0][0]*x[1][1] - x[0][1]*x[1][0]
    elif len_x == 3:
        output = x[0][0]*(x[1][1]*x[2][2] - x[1][2]*x[2][1]) - x[0][1]*(x[1][0]*x[2][2] - x[2][0]*x[1][2]) + x[0][2]*(x[1][0]*x[2][1] - x[1][1]*x[2][0])
        return output