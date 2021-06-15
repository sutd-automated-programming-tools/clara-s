def determinant(matrix):

    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            if len(matrix) ==1:
                det = matrix[0][0]
                return det
            if len(matrix) !=len(matrix[i]):
                return None
            if len(matrix) == 2:
                det = matrix[0][0]*matrix[1][1]- matrix[1][0]*matrix[0][1]

                return det
            if len(matrix) == 3:
                a = (matrix[0][0])*(matrix[1][1]*matrix[2][2]- matrix[2][1]*matrix[1][2])
                b = (matrix[0][1])*(matrix[1][0]*matrix[2][2]- matrix[2][0]*matrix[1][2])
                c = (matrix[0][2]) * (matrix[1][0] * matrix[2][1] - matrix[2][0] * matrix[1][1])
                det = a -b +c 
                
                return det