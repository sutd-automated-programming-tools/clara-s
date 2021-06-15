def determinant(m):
    if len(m)>3 or len(m)<1:
        return None
    else:
        try:
            if len(m)==1:
                ans=m[0][0]
                return ans
            elif len(m)==2:
                ans=m[0][0]*m[1][1]-m[0][1]*m[1][0]
            elif len(m)==3:
                ans=m[0][0]*(m[1][1]*m[2][2]-m[2][1]*m[1][2])-m[0][1]*(m[1][0]*m[2][2]-m[2][0]*m[1][2])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])
        except:
            return None
    return ans