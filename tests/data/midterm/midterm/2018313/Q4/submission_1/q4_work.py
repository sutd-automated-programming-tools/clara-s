def determinant(M):
    if len(M) == 1 and len(M[0]) == 1:
        return M[0][0]
    elif len(M) == 2 and len(M[0]) == 2 and len(M[1]) == 2:
        dett = M[0][0]*M[1][1] - M[0][1]*M[1][0]
        return dett
    elif len(M) == 3 and len(M[0]) == 3 and len(M[1]) == 3 and len(M[2]) == 3:
        dett = M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1]) - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
        return dett
    else: 
        return None
    