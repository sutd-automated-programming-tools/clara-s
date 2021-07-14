def determinant(M):
    for sublist in M:
        if len(sublist) != len(M):
            return None
    if len(M) == 1:
        return M[0][0]
    elif len(M) ==2:
        det = M[0][0]*M[1][1] - M[0][1]*M[1][0]
        return det
    elif len(M) == 3:
        det1 = M[0][0]* (M[1][1]*M[2][2] - M[1][2]*M[2][1])
        det2 = M[0][1]* (M[1][2]*M[2][0] - M[1][0]*M[2][2])
        det3 = M[0][2]* (M[1][0]*M[2][1] - M[1][1]*M[2][0])
        return det1+det2+det3