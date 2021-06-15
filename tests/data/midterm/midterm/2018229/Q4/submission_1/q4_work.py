def determinant(M):
    n = len(M) 
    if n < 1 or n > 3 :
        return None 
    else:
        if n == 1:
            det = M[0][0]
        elif n == 2:
            a = M[0][0]
            b = M[0][1]
            c = M[1][0]
            d = M[1][1]
            det = (a*d) - (b*c)
            
        elif n == 3:
            a= M[0][0]
            #print(a)
            b= M[0][1]
            #print(b)
            c= M[0][2]
            #print(c)
            d= M[1][0]
            #print(d)
            e= M[1][1]
            #print(e)
            f= M[1][2]
            #print(f)
            g= M[2][0]
            #print(g)
            h= M[2][1]
            #print(h)
            i= M[2][2]
            #print(i)
            det = (a * (e*i-f*h)) - (b*(d*i-g*f)) + (c*(d*h-e*f))
            
        return det