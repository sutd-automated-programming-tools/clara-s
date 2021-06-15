def determinant(mat):
    if len(mat) == 1:
        det = mat[0][0]
        return det
    elif len(mat) == 2:
        try:
            det = mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
            return det
        except IndexError:
            return None
    elif len(mat) == 3:
        try:
            a, b, c = mat[0][0],mat[0][1],mat[0][2]
            d, e, f = mat[1][0],mat[1][1],mat[1][2]
            g, h, i = mat[2][0],mat[2][1],mat[2][2]
            deta = a*(e*i-f*h)
            detb = b*(d*i-f*g)
            detc = c*(d*h-e*g)
            return deta-detb+detc
        except IndexError:
            return None
        