def determinant(matrix):
    def check_dim(matrix):
        for i in matrix:
            a = len(i)
            n = len(matrix)
            if (a != n) or (n > 3) or (n < 1):
                n = False
                break
        return n
    
    n = check_dim(matrix)
    print (n)
    if n == False:
        det = None
    elif n == 1:
        det = matrix[0][0]
    elif n == 2:
        det = matrix[0][0]*matrix[1][1] - matrix [0][1]*matrix[1][0]
    else:
        det_a = matrix[1][1]*matrix[2][2] - matrix [1][2]*matrix[2][1]
        det_b = matrix[1][0]*matrix[2][2] - matrix [1][2]*matrix[2][0]
        det_c = matrix[1][0]*matrix[2][1] - matrix [1][1]*matrix[2][1]
        det = matrix[0][0]*det_a - matrix[0][1]*det_b + matrix[0][2]*det_c
    return det