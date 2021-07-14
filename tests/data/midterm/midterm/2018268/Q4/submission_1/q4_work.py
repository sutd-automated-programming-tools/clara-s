def determinant(matrix):
    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            return None
        else:
            if len(matrix) == 3:
                first_term = matrix[0][0] * (matrix[1][1]*matrix[2][2] - matrix[2][1]*matrix[1][2])
                second_term = matrix[0][1] * (matrix[1][0]*matrix[2][2] - matrix[2][0]*matrix[1][2])
                third_term = matrix[0][2] * (matrix[1][0]*matrix[2][1] - matrix[2][0]*matrix[1][1])
                return first_term - second_term + third_term
            
            if len(matrix) == 2:
                return matrix[0][0] * matrix[1][1] - matrix[1][0]*matrix[0][1]
            
            else:
                return matrix[0][0]