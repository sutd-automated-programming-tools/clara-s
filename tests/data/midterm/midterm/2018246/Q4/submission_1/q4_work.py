def determinant(matrix):
    n = len(matrix)
    column = len(matrix[0])

    #check size of matrix
    if n < 1 or n > 3 or n != column:
        return None

    elif n == 1:
        det = matrix[0][0]
        return det

    elif n == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return det

    elif n == 3:
        mata = [[matrix[1][1], matrix[1][2]], [matrix[2][1], matrix[2][2]]]
        matb = [[matrix[1][0], matrix[1][2]], [matrix[2][0], matrix[2][2]]]
        matc = [[matrix[1][0], matrix[1][1]], [matrix[2][0], matrix[2][1]]]
        det = matrix[0][0] * determinant(mata) - matrix[0][1]*determinant(matb) + matrix[0][2] * determinant(matc)

        return det