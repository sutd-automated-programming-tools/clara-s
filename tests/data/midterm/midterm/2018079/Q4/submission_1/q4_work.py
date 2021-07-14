def determinant(matrix):
    length_matrix = len(matrix)
    length_line = len(matrix[0])
    ans = 0
    
    
    if length_matrix == 1:
        x = matrix[0]
        ans = x[0]
        return ans
    
    length_check = len(matrix[1])
    if length_line == length_check:
        pass
    else: 
        return None
    
    if length_matrix == 2:
        y1 = matrix[0]
        y2 = matrix[1]
        A = y1[0]
        B = y1[1]
        C = y2[0]
        D = y2[1]
        det = (A*D)-(B*C)
        return det
    elif length_matrix == 3:
        z1 = matrix[0]
        z2 = matrix[1]
        z3 = matrix[2]
        a = z1[0]
        b = z1[1]
        c = z1[2]
        d = z2[0]
        e = z2[1]
        f = z2[2]
        g = z3[0]
        h = z3[1]
        i = z3[2]
        det1 = (a*((e*i)-(f*h)))-(b*((d*i)-(f*g)))+(c*((d*h)-(e*g)))
        return det1
    else:
        return None