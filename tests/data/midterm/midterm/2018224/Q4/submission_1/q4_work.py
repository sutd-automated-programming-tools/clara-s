def determinant(matrix):
    if len (matrix)==1 and len(matrix[0])==1:
        return matrix[0][0]
    if len (matrix)==2 and len(matrix[0])==2 and len(matrix[1])==2==2:
        for i in range(2):
            ad=matrix[0][0]*matrix[1][1]
            bc=matrix[0][1]*matrix[1][0]
        ans=ad-bc
        return ans
    if len (matrix)==3 and len(matrix[0])==3 and len(matrix[1])==3 and len(matrix[2])==3:
        a=matrix[0][0]
        b=matrix[0][1]
        c=matrix[0][2]
        d=matrix[1][0]
        e=matrix[1][1]
        f=matrix[1][2]
        g=matrix[2][0]
        h=matrix[2][1]
        i=matrix[2][2]
        p1=a*(e*i-f*h)
        p2=b*(d*i-f*g)
        p3=c*(d*h-e*g)
        ans=p1-p2+p3
        return ans
    else:
        return None