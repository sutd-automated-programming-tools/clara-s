def determinant(matrix):        
    n=len(matrix)
    if 0<n<4:
        m=matrix
        if n==1:
            return matrix[0][0]
        elif n==2:
            for i in m:
                if len(i)!=n:
                    return None
            det=m[0][0]*m[1][1]-m[0][1]*m[1][0]
        elif n==3:
            a,b,c=m[0][0],m[0][1],m[0][2]
            d,e,f=m[1][0],m[1][1],m[1][2]
            g,h,i=m[2][0],m[2][1],m[2][2]
            det=a*(e*i-f*h)-b*(d*i-g*f)+c*(d*h-g*e)
        return det
    
    else:
        return None
