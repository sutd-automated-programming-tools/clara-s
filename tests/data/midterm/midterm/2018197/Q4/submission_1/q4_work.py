def determinant(m):
    for i in range(len(m)):
        if len(m[i])!=len(m):
            return None
        elif len(m)>3 or len(m[i])>3:
            return None
    if len(m)==1:
        det=m[0][0]
    elif len(m)==2:
        det=m[0][0]*m[1][1]-m[0][1]*m[1][0]
    elif len(m)==3:
        deta=m[0][0]*(m[1][1]*m[2][2]-m[2][1]*m[1][2])
        detb=-m[0][1]*(m[1][0]*m[2][2]-m[2][0]*m[1][2])
        detc=m[0][2]*(m[1][0]*m[2][1]-m[2][0]*m[1][1])
        det=deta+detb+detc
    return det