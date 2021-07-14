def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        return None
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    if len(matrix) ==3:
        first_matrix = [[matrix[1][1], matrix[1][2]],[matrix[2][1], matrix[2][2]]]
        second_matrix = [[matrix[1][0], matrix[1][2]], [matrix[2][0], matrix[2][2]]]
        third_matrix = [[matrix[1][0], matrix[1][1]], [matrix[2][0], matrix[2][1]]]
        return matrix[0][0]*determinant(first_matrix)-matrix[0][1]*determinant(second_matrix)+matrix[0][2]*determinant(third_matrix)