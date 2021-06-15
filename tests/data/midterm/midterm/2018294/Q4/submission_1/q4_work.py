def determinant(m):
    if len(m) == 1:
        for x in m:
            if len(x) == 1:
                return (m[0][0])
            else:
                return None
    elif len(m) == 2:
        for y in m:
            if len(y) == 2: 
                return ( (m[0][0] * m [1][1]) - ( m[0][1] * m[1][0]))
            else:
                return None
    elif len(m) == 3:
        for z in m:
            if len(z) == 3:
                a = (m[0][0]) * ((m[1][1] * m [2][2]) - ( m[1][2] * m[2][1]))
                b = (m[0][1]) * ((m[1][0] * m [2][2]) - ( m[1][2] * m[2][0]))
                c = (m[0][2]) * ((m[1][0] * m [2][1]) - ( m[1][1] * m[2][0]))
                return (a - b + c)
            else:
                return None
    else:
        return None