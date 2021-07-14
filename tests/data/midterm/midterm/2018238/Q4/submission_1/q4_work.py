def determinant(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if len(matrix)==1:
                return matrix[0][0]
            if len(matrix)==2:
                pass
            if len(matrix)==3:
                pass
            if len(matrix[i]) != len(matrix[j]):
                return None