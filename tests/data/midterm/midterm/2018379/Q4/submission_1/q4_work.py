def determinant(matrix):
    m = matrix
    if len(matrix) == 1:
        return (m[0][0])
    elif len(matrix[0]) == 2:
        m = matrix
        det = (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
        return (det)
    elif len(matrix) == 3:
        a = m[0][0]
        b = m[0][1]
        c = m[0][2]
        d = m[1][0] 
        e = m[1][1]
        f = m[1][2]
        g = m[2][0]
        h = m[2][1]
        i = m[2][2]
        det = (a*(e*i - f*h)) - (b*(d*i - f*g)) - (c*(d*h - e*g))
        return (det)
    else:
        return(None)

        
    