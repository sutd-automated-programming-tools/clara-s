def determinant(matrix):
    testN = len(matrix[0])
    for a in matrix:
        if len(a) != testN:
            return None
    if testN == 1:
        det = matrix[0][0]
    elif testN == 2:
        det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    elif testN ==3:
        a =matrix[0][0]
        b =matrix[0][1]
        c =matrix[0][2]
        d =matrix[1][0]
        e =matrix[1][1]
        f =matrix[1][2]
        g =matrix[2][0]
        h =matrix[2][1]
        i =matrix[2][2]
        #det = matrix[0][0]*(matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1])- matrix[0][1](matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0])+matrix[0][2]*(matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0])
        det = a*(e*i - h*f) - b*(d*i - g*f) + c*(d*h - e*g)
    return det