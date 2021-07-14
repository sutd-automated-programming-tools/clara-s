def determinant(mtx):
    n = len(mtx)
    m = len(mtx[0])
    if n != m or n < 1 or n > 3:
        return None
    if n == 1:
        return mtx[0][0]
    if n == 2:
        a = mtx[0][0]
        b = mtx[0][1]
        c = mtx[1][0]
        d = mtx[1][1]
        return a*d - b*c
    if n == 3:
        a = mtx[0][0]
        b = mtx[0][1]
        c = mtx[0][2]
        d = mtx[1][0]
        e = mtx[1][1]
        f = mtx[1][2]
        g = mtx[2][0]
        h = mtx[2][1]
        i = mtx[2][2]
        temp = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - g*e)
        return temp