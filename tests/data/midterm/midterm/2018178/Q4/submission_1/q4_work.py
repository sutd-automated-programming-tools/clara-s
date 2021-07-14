def determinant(m):
    row = len(m[0])
    col = len(m)
    if col < 1 or col > 3 or row != col:
        return None
    for i in m:
        if len(i) < 1 or len(i) > 3:
            return None
    
    if row == 1:
        return m[0][0]
    if row == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]

    if row == 3:
        d1 = m[0][0]*(m[1][1]*m[2][2] - m[1][2]*m[2][1])
        d2 = m[0][1]*(m[1][0]*m[2][2] - m[1][2]*m[2][0])
        d3 = m[0][2]*(m[1][0]*m[2][1] - m[1][1]*m[2][0])
        return d1-d2+d3