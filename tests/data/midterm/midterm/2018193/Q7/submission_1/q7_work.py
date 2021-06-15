# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    d=0
    for i in range(10000):
        a= int(i)
        for j in range(10000):
            b = 2*int(j)
            for k in range(1000):
                c = 5*int(k)
                for h in range(1000):
                    d = 10*int(h)
                    for g in range(1000):
                        e = 20*int(g)
                        for y in range(10000):
                            f = 50*int(y)
                            for n in range(100):
                                h = int(n)*100
                                for l in range(10):
                                    j = int(l)*200
                                    if (a+b+c+d+e+f+h+j)==pence:
                                        d+=1
                             
        
    return d