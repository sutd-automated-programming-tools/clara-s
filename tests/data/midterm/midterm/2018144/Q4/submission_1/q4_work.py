def determinant(matrix):
    num1 = len(matrix)
    num2 = 0
    for n in matrix:
        if len(n)!=num2 and num2!=0:
            return None
        num2 = len(n)
    if num1 != num2:
        return None
    ls = []
    if len(matrix) == 1:
        det = matrix[0][0]
    elif len(matrix) == 2:
        for i in matrix:
            ls += i
        det = ls[0]*ls[3] - ls[1]*ls[2]
    elif len(matrix) == 3:
        for j in matrix:
            ls += j
        det = ls[0]*(ls[4]*ls[8] - ls[5]*ls[7]) - ls[1]*(ls[3]*ls[8] - ls[5]*ls[6]) + ls[2]*(ls[3]*ls[7] - ls[4]*ls[6])
    return det
