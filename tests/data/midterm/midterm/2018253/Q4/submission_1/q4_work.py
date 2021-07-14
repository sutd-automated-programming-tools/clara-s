def determinant(matrix):
    row = 0
    for i in matrix:
        row += 1
    for i in matrix:
        if len(i) == row:
            continue
        else:
            return None
    counter = 0
    for i in matrix:
        counter += 1
    if counter == 1:
        return matrix[0][0]
    elif counter == 2:
        return (matrix[0][0] * matrix[1][1] - matrix [0][1] * matrix [1][0])
    elif counter == 3:
        det1 = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix [1][2] * matrix [2][1])
        det2 = matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix [1][2] * matrix [2][0])
        det3 = matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix [1][1] * matrix [2][0])
        return det1 - det2 + det3