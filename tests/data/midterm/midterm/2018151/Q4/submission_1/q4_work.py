def determinant(m):
    if len(m)>3:
        return (None)
    for i in m:
        if len(i) != len(m):
            return (None)
    if len(m) == 1:
        return ( m[0][0])
    if len(m) ==2:
        ad = m[0][0] * m[1][1]
        bc = m[0][1] * m[1][0]
        return(ad-bc)
    if len(m) ==3:
        ad1 = m[1][1]*m[2][2]
        bc1 = m[2][1]*m[1][2]
        
        ad2 = m[1][0]*m[2][2]
        bc2 = m[2][0]*m[1][2]
        
        ad3 = m[1][0]*m[2][1]
        bc3 = m[2][0]*m[1][1]
        
        det= m[0][0]*(ad1-bc1)-m[0][1]*(ad2-bc2)+m[0][2]*(ad3-bc3)
        return (det)
        