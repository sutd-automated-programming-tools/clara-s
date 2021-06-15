def determinant(matrix):

    m = len(matrix)
    n = len(matrix[0])

    if m >=1 and m <=3 and n >=1 and n<=3 and m==n:
        if m == 1:
            return matrix[0][0]
        elif m == 2:
            result = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
            return result
        else:
            det1 = matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1]) 
            det2 = matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0]) 
            det3 = matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
            result = det1-det2+det3
            return result 
    else:
        return None
