def determinant(matrix):
    det = None
    for i in range(len(matrix)):   
        n = len(matrix[i])
        if n < 1 or n > 3:
            break
        if i == 0:
            check = n
        if  n == check:
            det = True
        else:
            det = None
            break
    if det == True:       
        if n == 1:
            det = matrix[0][0]
        elif n == 2:
            ad = matrix[0][0]*matrix[1][1]
            bc = matrix[0][1]*matrix[1][0]
            det = ad-bc
        else:
            det = (matrix[0][0]*((matrix[1][1]*matrix[2][2]) - (matrix[1][2]*matrix[2][1]))) - (matrix[0][1]*((matrix[1][0]*matrix[2][2]) - (matrix[1][2]*matrix[2][0]))) + (matrix[0][2]*((matrix[1][0]*matrix[2][1]) - (matrix[1][1]*matrix[2][0])))
    return det