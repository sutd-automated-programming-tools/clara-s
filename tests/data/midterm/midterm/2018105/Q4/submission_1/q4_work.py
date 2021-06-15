def determinant(matrix):
    for i in matrix:
        for j in i:
            if len(matrix) != len(i):
                return None
            
            else:
                if len(i) == 1:
                    det = j
                    return det
                
                if len(i) == 2:
                    det = i[0][0] * i[1][1] - i[0][1] * i[1][0]
                    return det
                
                if len(i) == 3:
                    det_1 = i[1][1] * i[2][2] - i[2][1] * i[1][2]
                    det_2 = i[1][0] * i[2][2] - i[2][0] * i[1][2]
                    det_3 = i[1][0] * i[2][1] - i[2][0] * i[1][1]
                    det = i[0][0] * det_1 - i[0][1] * det_2 + i[0][2] * det_3
                    return det