def determinant(matrix):
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0]
    elif len(matrix) == 2 and len(matrix[0]) == 2 and len(matrix[1]) == 2:
        det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        return det
    elif len(matrix) == 3 and len(matrix[0]) == 3 and len(matrix[1]) == 3 and len(matrix[2]) == 3:
        part1 = matrix[0][0] * ((matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1]))
        part2 = matrix[0][1] * ((matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0]))
        part3 = matrix[0][2] * ((matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0]))
        return part1-part2+part3
    else:
        return None