def determinant(M):
    n = len(M)
    if n>3 or n<1:
        return None

    else:
        if n==1:
            return M[0][0]
        if n ==2:
            if len(M[0])!=len(M[1]):
                return None
            else:
                ans = M[0][0]*M[1][1]-M[1][0]*M[0][1]
                return ans
        if n ==3:
            if len(M[0])!=len(M[1]) or len(M[0])!=len(M[2])or len(M[2])!=len(M[1]):
                return None
            else:
                a1 = M[0][0]*(M[1][1]*M[2][2]-M[2][1]*M[1][2])
                a2 = M[0][1]*(M[1][0]*M[2][2]-M[2][0]*M[1][2])
                a3 = M[0][2]*(M[1][0]*M[2][1]-M[2][0]*M[1][1])
                return( a1-a2+a3)
