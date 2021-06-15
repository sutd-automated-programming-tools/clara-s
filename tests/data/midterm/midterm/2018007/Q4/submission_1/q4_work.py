def determinant(x):
    leng = len(x)
    if leng == 1:
        return x[0][0]
    elif leng == 2:
        if len(x[0]) == 2 and len(x[1]) == 2:
            det = x[0][0]*x[1][1]-x[0][1]*x[1][0]
            return det
        else:
            return None
    elif leng == 3:
        if len(x[0]) == 3 and len(x[1]) == 3 and len(x[2]) == 3:
            det1 = x[1][1] * x[2][2] - x[1][2] * x[2][1]
            det2 = x[1][0] * x[2][2] - x[1][2] * x[2][0]
            det3 = x[1][0] * x[2][1] - x[1][1] * x[2][0]
            
            det = x[0][0] * det1 - x[0][1] * det2 + x[0][2] * det3
            
            return det
        else:
            return None