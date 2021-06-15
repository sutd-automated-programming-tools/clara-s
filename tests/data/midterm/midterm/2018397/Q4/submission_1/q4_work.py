def determinant(matrix):
    n = len(matrix)
    if n == 1:
        matrix = []
        determinant = matrix[0]
        return determinant
    
    if n == 2:
        matrix = []
        determinant = matrix[0]*matrix[3] - matrix[1]*matrix[2]
        return determinant
