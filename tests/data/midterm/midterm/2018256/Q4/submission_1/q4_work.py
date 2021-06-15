def determinant(m):
    if len(m)<1 or len(m)>3:
        return None
    else:
        for i in m:
            if len(i)!=len(m):
                return None
    
    def det2(w,x,y,z):
        ans = w*z-x*y
        return ans
          
    ans = 0
    n = len(m)
    if n == 1:
        ans = m[0][0]
    elif n == 2:
        ans = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    elif n == 3:
        a = m[0][0]
        b = m[0][1]
        c = m[0][2]
        d = m[1][0]
        e = m[1][1]
        f = m[1][2]
        g = m[2][0]
        h = m[2][1]
        i = m[2][2]
        ans = a*det2(e,f,h,i) - b*det2(d,f,g,i) + c*det2(d,e,g,h)
    return ans