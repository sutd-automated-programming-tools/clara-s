def determinant(matrix):
    n=len(matrix)
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix):
            return None
    if n <=3 and n>=1:
        if n ==1:
            det = matrix[0][0]
        elif n ==2:
            det = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        elif n ==3:
            det = matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])-matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])+matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
        return det
    else:
        return None