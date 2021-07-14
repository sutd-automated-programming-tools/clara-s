def determinant(m):
    for i in m:
        if len(i)== len(m):
            continue
        else:
            return
    if len(m)==1:
        return m[0][0]
    elif len(m)==2:
        return (m[0][0])*(m[1][1])- (m[0][1])*(m[1][0])
    elif len(m)==3:
        det_1 = m[0][0] * ((m[1][1])*(m[2][2])- (m[1][2])*(m[2][1]))
        det_2 = m[0][1] * ((m[1][0])*(m[2][2])- (m[1][2])*(m[2][0]))
        det_3 = m[0][2] * ((m[1][0])*(m[2][1])- (m[1][1])*(m[2][0]))
        return det_1 - det_2 + det_3
    else:
        return