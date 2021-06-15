def determinant(M):
    if type(M) != list :
        return None
    state = True
    j = len(M[0])
    for i in M:
        if len(i) != j:
            return None
        
        
    if len(M) == 1:
        return M[0][0]
    elif len(M) == 2:
        return M[0][0]*M[1][1] - M[1][0]*M[0][1]
    elif len(M) == 3:
        A = [  [ M[1][1],M[1][2]] , [ M[2][1], M[2][2]] ]
        B = [  [ M[1][0], M[1][2]  ],   [ M[2][0],  M[2][2]   ]]
        C = [   [M[1][0], M[1][1]],  [M[2][0],  M[2][1]]]
        return M[0][0]*determinant(A) - M[0][1]*determinant(B) + M[0][2]*determinant(C)