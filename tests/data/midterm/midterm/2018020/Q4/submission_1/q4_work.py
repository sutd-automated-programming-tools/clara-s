def determinant(matrix):
    n = len(matrix)
    n21 = 1
    n22 = 1
    n31 = 1
    n32 = 1
    n33 = 1
    
    for e in matrix:
        if len(e) <= 3 and n <= 3 and len(e) == n:
            if len(e) == 1:
                out = e[0]
            elif len(e) == 2:
                n21 = n21 * e[0]
                n22 = n22 * e[1]
                out = n21 + n22
            elif len(e) == 3:
                n31 = n31 * e[0]
                n32 = n32 * e[1]
                n33 = n33 * e[2]
                out = n31 + n32 + n33
                
        else:
            out = None
            
    return out