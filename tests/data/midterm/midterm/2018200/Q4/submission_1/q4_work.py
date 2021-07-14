def determinant(matrix):
    if len(matrix) == 1:
        det = matrix[0]
        return det
    elif len(matrix) > 1 and len(matrix) <= 3:
        if len(matrix) == len(matrix[0]):
            if len(matrix) == 2:
                det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
                for k in matrix:
                    for l in k:
                        print(l)
                        
                return det
            if len(matrix) == 3:
                summ = 0
                sign = 1
                for pos,i in enumerate(matrix):
                    print(i)
                    coeff = matrix[0][pos]*sign
                    sign *= -1
                    print(coeff)
                    
                    summ = coeff*()
                    #wanted to do an iterative addition for the determinant for 3x3 matrix
                det = None
                return det
        else:
            return None
    elif len(matrix) > 1:
        return None