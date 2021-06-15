def onebyone(m):
    det = m[0][0]
    return det
 
def twobytwo(m):
    det = ((m[0][0])*(m[1][1])-((m[0][1])*(m[1][0])))
    return det
 
def threebythree(m):
    a = m[0][0]
    b = m[0][1]
    c = m[0][2]
    d = m[1][0]
    e = m[1][1]
    f = m[1][2]
    g = m[2][0]
    h = m[2][1]
    i = m[2][2]
    det = ((a*(e*i - f*h)) - (b*(d*i - f*g)) + (c*(d*h - e*g)))
    return det
    
def determinant(matrix):
    if len(matrix) == 1:
        tr = onebyone(matrix)
        return tr
    elif len(matrix) == 2:
        if len(matrix[0])==2:
            pr = twobytwo(matrix)
            return pr
        else:
            return None
    elif len(matrix) == 3:
        qr = threebythree(matrix)
        return qr
    else:
        return print("this matrix is too big/small")