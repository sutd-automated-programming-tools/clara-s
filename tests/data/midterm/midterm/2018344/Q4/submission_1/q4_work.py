def determinant(m):
    if len(m) == 1:
        return m[0][0]
    
    elif len(m) > 1:
        
        if(len(m) != len(m[0])):
            return None
            
       
        else:
            
            if(len(m) == 2):
                val = det2(m)
                return val
            
            else:
                
                m1 = []
                m2 = []
                m3 = []
                m11 = []
                m22 = []
                m33= []
                M1 = []
                M2 = []
                M3 = []
            
                m1.append(m[1][1])
                m1.append(m[1][2])
                m11.append(m[2][1])
                m11.append(m[2][2])
                M1.append(m1)
                M1.append(m11)
                m2.append(m[1][0])
                m2.append(m[1][2])
                m22.append(m[2][0])
                m22.append(m[2][2])
                M2.append(m2)
                M2.append(m22)
                m3.append(m[1][0])
                m3.append(m[1][1])
                m33.append(m[2][0])
                m33.append(m[2][1])
                M3.append(m3)
                M3.append(m33)
                
                d1 = det2(M1)
                d2 = det2(M2)
                d3 = det2(M3)
                
                val = m[0][0]*d1 + m[0][1]*d2 + m[0][2]*d3
                
                return val

                
            
    
        


def det2(m):
    val = (m[0][0] * m[1][1]) - (m[0][1]*m[1][0])
    return val




