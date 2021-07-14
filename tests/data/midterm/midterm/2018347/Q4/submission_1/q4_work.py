def determinant(matrix):
    if len(matrix)>3:
        return None
    if len(matrix) != len(matrix[0]):
        return None
    
    else:
        if len(matrix) == 1:
            det = matrix [0][0]
            
        elif len(matrix) == 2:
            det = matrix[0][0]*matrix[1][1] - matrix [1][0]*matrix[0][1]

        elif len(matrix) == 3:
            det1 = matrix [0][0] *(matrix[1][1]*matrix[2][2]-matrix[2][1]*matrix[1][2])
            det2 = -matrix [0][1] *(matrix[1][0]*matrix[2][2]-matrix[2][0]*matrix[1][2])
            det3 = matrix [0][2] *(matrix[1][0]*matrix[2][1]-matrix[2][0]*matrix[1][1])
            det = det1 + det2 + det3
        return det