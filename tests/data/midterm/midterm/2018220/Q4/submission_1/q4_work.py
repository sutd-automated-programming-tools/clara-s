def determinant(matrix):
    if len(matrix)==0: 
        return None
    if len(matrix)==1:
        ans1 = matrix[0]
        ans = ans1[0]
        return ans
    if len(matrix)==2:
        up=matrix[0]
        bottom=matrix[1]
        if len(up) != len(bottom):
            return None
        else:
            a=up[0]
            b=up[1]
            c=bottom[0]
            d=bottom[1]
            ans=a*d-b*c
            return ans
    if len(matrix)==3:
        up=matrix[0]
        mid=matrix[1]
        bottom=matrix[2]
        if len(up) != len(bottom) or len(up) != len(mid) or len(mid) != len(bottom) or len(up) != len(bottom) != len(mid):
            return None
        else:
            a=up[0]
            b=up[1]
            c=up[2]
            d=mid[0]
            e=mid[1]
            f=mid[2]
            g=bottom[0]
            h=bottom[1]
            i=bottom[2]
            ans=a*(e*i-h*f)-b*(d*i-f*g)+c*(d*h-e*g)
            return ans