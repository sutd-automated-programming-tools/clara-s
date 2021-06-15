def determinant(mat):
    final = 0
    if len(mat) < 1 or len(mat) > 3:
        final = None
    elif len(mat) == 1:
        final = mat[0][0]
    elif len(mat) > 1:
        for row in mat:
            if len(row) != len(mat):
                final = None
    if final != None:
        if len(mat) == 2:
            final = mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
        if len(mat) == 3:
            a = mat[0][0]
            b = mat[0][1]
            c = mat[0][2]
            d = mat[1][0]
            e = mat[1][1]
            f = mat[1][2]
            g = mat[2][0]
            h = mat[2][1]
            i = mat[2][2]
            final = a*(e*i-h*f) - b*(d*i-g*f) + c*(d*h-g*e)
    return final
    