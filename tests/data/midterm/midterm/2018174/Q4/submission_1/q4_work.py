def determinant(matrix):
    
    for i in range(len(matrix[0]):
        if i == 1:
            return matrix
        if i == 2:
            mm = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
            return mm
        else:
            return None 