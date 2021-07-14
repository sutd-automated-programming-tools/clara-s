def determinant(m):
    l = len(m)
    a = len(m[0])
    
    if a != l:
        return None
    elif len(m) == 1:
        return m[0][0]
    elif len(m) == 2:
        b = (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
        return b
    elif len(m) == 3:
        c = (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])) - (m[0][1]*(m[1][0]*m[2][2]-m[2][0]*m[1][2])) + (m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
        return c
