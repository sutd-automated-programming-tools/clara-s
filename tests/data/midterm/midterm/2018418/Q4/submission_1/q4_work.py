def determinant(m):
    if len(m) < 1 or len(m) > 3:
        return None
    elif len(m) == 1:
        return m[0][0]
    elif len(m) == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]
    else:
        det_1 = m[0][0]*(m[1][1]*m[2][2] - m[2][1]*m[1][2])
        det_2 = m[0][1]*(m[1][0]*m[2][2] - m[2][0]*m[1][2])
        det_3 = m[0][2]*(m[1][0]*m[2][1] - m[1][1]*m[2][0])
        return det_1 - det_2 + det_3