def determinant(matrix):
    det = 0
    for i in matrix:
        n = len(matrix[0])
        if n >= 3:
            return None  
        elif n == 1:
            det = i
            return det
        elif n == 2:
            det = i[0][0] * i[1][1] - i[0][1] * i[1][0]
            return det
        elif n == 3:
            det_sqmatrix1 = i[1][1] * i[2][2] - i[1][2] * i[2][1] 
            det_sqmatrix2 = i[1][0] * i[2][2] - i[1][2] * i[2][0]
            det_sqmatrix3 = i[1][0] * i[2][1] - i[1][1] * i[2][0]
            det = i[0][0] * det_sqmatrix1 - i[0][1] * det_sqmatrix2 + i[0][2] * det_sqmatrix3
            return det 
        