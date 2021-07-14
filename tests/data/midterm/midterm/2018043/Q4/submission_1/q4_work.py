def determinant(matrix):
    if len(matrix) != 1:
        if len(matrix) != len(matrix[0]):
            return None
    elif len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    if len(matrix) == 3:
        m1 = [[matrix[1][1],matrix[1][2]],[matrix[2][1],matrix[2][2]]]
        m2 = [[matrix[1][0], matrix[1][2]], [matrix[2][0], matrix[2][2]]]
        m3 = [[matrix[1][0], matrix[1][1]], [matrix[2][0], matrix[2][1]]]
        return matrix[0][0]*determinant(m1)-matrix[0][1]*determinant(m2)+matrix[0][2]*determinant(m3)

    if len(matrix) >=4:
        return None

