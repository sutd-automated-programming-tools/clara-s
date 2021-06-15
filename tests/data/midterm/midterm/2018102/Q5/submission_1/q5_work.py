# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num=1):
        func = num**(1/n)
        p0 = 1.0 * x0
        fder2 = 0
        for iter in range(t):
            myargs = (p0,) + args
            fder = fprime(*myargs)
            fval = func(*myargs)
            discr = fder ** 2 - 2 * fval * fder2
            if discr < 0:
                    p = p0 - fder / fder2
            else:
                    p = p0 - 2*fval / (fder + sign(fder) * sqrt(discr))
            if abs(p - p0) < tol:
                return p
            p0 = p
          
    

def nroot_complex(n,t,num=1):
    pass