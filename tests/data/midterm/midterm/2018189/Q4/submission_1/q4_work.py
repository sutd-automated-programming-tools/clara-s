def determinant(matrix):
    m = matrix
    if len(m) != len(m[0]): return None
    
    if len(m) == 1:
        return m[0][0
                   ]
    if len(m) == 2:
        return (m[0][0]*m[1][1])-(m[0][1]*m[1][0])
    
    if len(m) == 3:
        d1 = ((m[1][1]*m[2][2])-(m[1][2]*m[2][1]))
        d2 = ((m[1][0]*m[2][2])-(m[1][2]*m[2][0]))
        d3 = ((m[1][0]*m[2][1])-(m[1][1]*m[2][0]))
        
        return m[0][0]*d1 - m[0][1]*d2 + m[0][2]*d3