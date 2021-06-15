def determinant(m):
    det = 0
    if len(m) != len(m[0]):
        return None
    
    if len(m) == 1:
        det = m[0][0]
        
    elif len(m) == 2:
        det = m[0][0]*m[1][1] - m[0][1]*m[1][0]
        
    elif len(m) == 3:
        detA = m[1][1]*m[2][2] - m[2][1]*m[1][2]
        detB = m[1][0]*m[2][2] - m[2][0]*m[1][2]
        detC = m[1][0]*m[2][1] - m[2][0]*m[1][1]
        
        det = m[0][0]*detA - m[0][1]*detB + m[0][2]*detC
    return det