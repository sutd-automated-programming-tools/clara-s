def determinant(M):
    if len(M) == 0 or len(M) > 4:
        return None
    for i in M:
        if len(i) != len (M):
            return None
    else:
        if len(M) == 1:
            ans = M
        if len(M) == 2:
            ans = M[0][0] * M[1][1] - M[1][0] * M[0][1]
        if len(M) == 3:
            a = M[0][0]
            b = M[0][1]
            c = M[0][2]
            d = M[1][0]
            e = M[1][1]
            f = M[1][2]
            g = M[2][0]
            h = M[2][1]
            i = M[2][2]
            ans = a*(e*1-h*f) - b*(d*i-g*f) + c*(d*h-g*e)
    return ans