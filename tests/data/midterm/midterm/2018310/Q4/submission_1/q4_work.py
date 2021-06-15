def determinant(matrix):
    for i in matrix:
        if len(i) < 1 or len(i) > 3 or len(i) != len(matrix):
            return None
        elif len(i) == 1:
            return i[0]
        if len(matrix) == 2:
            return matrixMult(matrix, 0, 1, 0, 1)
        if len(matrix) == 3:
            return ((matrix[0][0] * (matrixMult(matrix, 1,2,1,2)))
                    - (matrix[0][1] * (matrixMult(matrix, 1,2,0,2)))
                    + (matrix[0][2] * (matrixMult(matrix, 1,2,0,1))))
        
def matrixMult(matrix, row1, row2, col1, col2):
    return (matrix[row1][col1] * matrix[row2][col2] - 
                    matrix[row1][col2] * matrix[row2][col1])