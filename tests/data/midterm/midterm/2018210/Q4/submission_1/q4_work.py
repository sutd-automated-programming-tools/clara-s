
def det_2(M):
    return ((M[0][0] * M[1][1]) - (M[0][1] * M[1][0]))


def determinant(M):
    if len(M) != len(M[0]):
        return None
    elif len(M) == 1:
        return M[0][0]
    elif len(M) == 2:
        return det_2(M)
    else:
        first = M[0][0] * det_2([M[1][1:3], M[2][1:3]])
        second = M[0][1] * det_2([M[1][0::2], M[2][0::2]])
        last = M[0][2] * det_2([M[1][0:2], M[2][0:2]])
        return first - second + last
