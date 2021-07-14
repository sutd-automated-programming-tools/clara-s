def determinant(matrix):
    M = matrix
    if len(M) == len(M[0]):
        if len(M) == 1:
            return M[0][0]
        elif len(M) == 2:
            return M[0][0]*M[1][1] - M[0][1]*M[1][0]
        elif len(M) == 3:
            a = M[0][0]
            b = M[0][1]
            c = M[0][2]
            d = M[1][0]
            e = M[1][1]
            f = M[1][2]
            g = M[2][0]
            h = M[2][1]
            i = M[2][2]
            return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
    else:
        return None