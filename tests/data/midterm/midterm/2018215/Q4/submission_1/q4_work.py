def determinant(matrix):
    if len(matrix) > 3 or len(matrix) < 1:
        return None
    elif len(matrix) == 1:
        return matrix[0]
    elif len(matrix) == 2:
        ad = matrix[0][0] * matrix[1][1]
        bc = matrix[0][1] * matrix[1][0]
        return ad - bc
    elif len(matrix) == 3:
        ad_first = matrix[1][1] * matrix[2][2]
        bc_first = matrix[1][2] * matrix[2][1]
        first = matrix[0][0] * (ad_first - bc_first)
        ad_second = matrix[1][0] * matrix[2][2]
        bc_second = matrix[1][2] * matrix[2][0]
        second = matrix[0][1] * (ad_second - bc_second)
        ad_third = matrix[1][0] * matrix[2][1]
        bc_third = matrix[1][1] * matrix[2][0]
        third = matrix[0][2] * (ad_third - bc_third)
        return first - second + third