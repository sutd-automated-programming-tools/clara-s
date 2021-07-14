def determinant(matrix):
    for sublist in matrix:
        if len(sublist) > 3 and len(sublist) == 0:
            return None
        elif len(sublist) != len(sublist):
            return None
        elif len(matrix) == 1:
            return matrix.pop[0]
        elif len(matrix) == 2:
            return (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0])
        elif len(matrix) == 3:
            pass