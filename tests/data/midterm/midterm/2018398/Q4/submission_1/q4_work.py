def determinant(matrix):
    for i in range(len(matrix)):
        no_of_rows = len(matrix)
        row = matrix[i]
        for j in range(len(row)):
            no_of_col = len(matrix[i])
            det = matrix[i]
            if no_of_rows == no_of_col:
                if no_of_rows == 1:
                    det = matrix[0]
                elif no_of_rows == 2:
                    det = (matrix[0][0]*matrix[1][1]) - (matrix[1][0] * matrix[0][1])
                elif no_of_rows == 3:
                    pass
            else:
                return None
            return det
