def determinant(matrix):
    for i in range(len(matrix) - 1):
        if len(matrix[i]) != len(matrix[i+1]):
            return None
    if len(matrix[0]) == 1:
        return matrix[0][0]
    if len(matrix[0]) == 2:
        det = (matrix[0][0]*matrix[1][-1]) - (matrix[0][-1]*matrix[1][0])
        return det
    ls = []
    if len(matrix[0]) == 3:
        for i in range(len(matrix)):
            for u in range(len(matrix[i])):
                ls.append(matrix[i][u])
    print(ls)
    det1 = ls[0]*((ls[4]*ls[8]) - (ls[7]*ls[5])) - ls[1]*((ls[3]*ls[8]) - (ls[6]*ls[5])) + ls[2]*((ls[3]*ls[7]) - (ls[6]*ls[4]))
    return det1