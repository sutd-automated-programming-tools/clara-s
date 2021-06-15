def det_for_2(n):
    det=n[0][0]*n[1][1]-n[0][1]*n[1][0]
    return det
def determinant(matrix):
    if len(matrix)!=len(matrix[0]):
        return None
    else:
        if len(matrix)==1:
            return matrix[0][0]
        elif len(matrix)==2:
            return det_for_2(matrix)
        elif len(matrix)==3:
            M1=[[matrix[1][1],matrix[1][2]],[matrix[2][1],matrix[2][2]]]
            M2=[[matrix[1][0],matrix[1][2]],[matrix[2][0],matrix[2][2]]]
            M3=[[matrix[1][0],matrix[1][1]],[matrix[2][0],matrix[2][1]]]
            det=matrix[0][0]*det_for_2(M1)-matrix[0][1]*det_for_2(M2)+matrix[0][2]*det_for_2(M3)
            return det
        else:
            return None