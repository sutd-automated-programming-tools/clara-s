def determinant(M):
    if len(M) not in range(1,4):
        print('lol')
        return None
    op = 0
    L = len(M)
    for i in range(L):
        if len(M[i]) != L:
            return None
    if L == 1:
        op += M[0][0]
    elif L == 2:
        op = M[0][0]*M[1][1] - M[0][1]*M[1][0]
    elif L == 3:
        op += M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1])
        op -= M[0][1]*(M[1][0]*M[2][2] - M[2][0]*M[1][2])
        op += M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0])
    return op