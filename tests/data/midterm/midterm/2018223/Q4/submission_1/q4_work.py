def determinant(matrix):
    for i in matrix:
        if len(matrix) != i:
            return None
        if i == 1:
            det = matrix[0]
        if i == 2:
            det = matrix [0][0]*matrix [1][1] - matrix [0][1]*matrix [1][0]  
        if i == 3:

            det = matrix [0][0]*matrix [1][1] - matrix [0][1]*matrix [1][0]
        return det