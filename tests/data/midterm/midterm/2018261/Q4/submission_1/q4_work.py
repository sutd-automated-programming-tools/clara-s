def determinant(matrix):
    if len(matrix)==1:
        if len(matrix[0])==1:
            det=matrix[0][0]
            return det
        else:
            return None
    elif len(matrix)==2:
        if len(matrix[0])==2 and len(matrix[1])==2:
            det = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
            return det
        else:
            return None
    elif len(matrix)==3:
        if len(matrix[0])==3 and len(matrix[1])==3 and len(matrix[2])==3:
            a = matrix[0][0]
            b = matrix[0][1]
            c = matrix[0][2]
            detA = matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1]
            detB = matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0]
            detC =matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0]
            det = a*detA - b*detB + c*detC
            return det
        else:
            return None
    else:
        return None

