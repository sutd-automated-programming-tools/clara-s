def determinant(m):
    n = len(m[0])
    for i in m:
        if len(i) != n:
            return None
    if len(m)==0 or len(m)>3:
        return None
    if len(m) == 1:
        return m[0][0]
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    if len(m) == 3:
        first = m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
        second = m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
        third = m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])
        det = first-second+third
        return det