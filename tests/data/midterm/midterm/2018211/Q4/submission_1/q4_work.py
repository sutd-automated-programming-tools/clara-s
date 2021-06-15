def determinant(matrix):
    M = matrix
    
    try:
        a = len(M)
        a = len(M[0])
    except:
        return None
    
    if len(M) == 1:
        for row in M:
            if len(row) != 1:
                return None
        return M[0][0]
    if len(M) == 2:
        for row in M:
            if len(row) != 2:
                return None
        return M[0][0] * M[1][1] - M[0][1]*M[1][0]
    if len(M) == 3:
        for row in M:
            if len(row) != 3:
                return None
        return (M[0][0] * M[1][1] * M[2][2] 
                + M[1][0] * M[2][1] * M[0][2] 
                + M[2][0] * M[0][1] * M[1][2]
                - M[0][2] * M[1][1] * M[2][0]
                - M[1][0] * M[0][1] * M[2][2]
                - M[0][0] * M[2][1] * M[1][2]
               )