def determinant(matrix):
    i = matrix
    if len(i) == 1:
        return i[0][0]
    elif len(i[0]) == 2:
        if len(i[0]) == len(i[1]):
            det1 = (i[0][0])*(i[1][1]) - (i[0][1])*(i[1][0])
            return det1
        else:
            return None
    else:
        if len(i[0]) == len(i[1]) and len(i[1]) == len(i[2]):
           det2 = (i[0][0])*(i[1][1]*i[2][2]-i[1][2]*i[2][1]) - i[0][1]*(i[1][0]*i[2][2]-i[1][2]*i[2][0]) + i[0][2]*(i[1][0]*i[2][1]-i[1][1]*i[2][0])
           return det2 
        else:
           return None