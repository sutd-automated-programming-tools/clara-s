def determinant(matrix):
    for i in range(len(matrix)): #check if all matrix are n<3
        x=(len(matrix))
        if len(matrix[i]) != x:
            return None
    if len(matrix) > 3 or len(matrix) < 1:
        return None
    if len(matrix) == 1:
        det = matrix[0][0]
        return det
    if len(matrix) == 2:
        ad = matrix[0][0] * matrix[1][1]
        bc = matrix[0][1] * matrix[1][0]
        det = ad - bc
        return det
    if len(matrix) == 3:
        print ('here')
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        ei = matrix[1][1] * matrix [2][2]
        hf = matrix[2][1] * matrix [1][2]
        di = matrix[1][0] * matrix [2][2]
        gf = matrix[2][0] * matrix [1][2]
        dh = matrix[1][0] * matrix [2][1]
        ge = matrix[2][0] * matrix [1][1]
        det = (a *(ei-hf)) - (b*(di-gf)) + (c*(dh-ge))
        return det