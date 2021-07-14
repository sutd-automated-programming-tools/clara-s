# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    n = pence
    p1 = 1
    p2 = 2
    p5 = 5
    p10 = 10
    p20 = 20
    p50 = 50
    p100 = 100
    p200 = 200
    
    soln = 0
    for a in range(n+1):
        p1=a
        if(p1+p2+p5+p10+p20+p50+p100+p200 < pence):
            for b in range(n+1):
                p2=b
                if(p1+p2+p5+p10+p20+p50+p100+p200 < pence):
                    for c in range(n+1):
                        p5=c
                        if(p1+p2+p5+p10+p20+p50+p100+p200 < pence):
                            for d in range(n+1):
                                p10=d
                                if(p1+p2+p5+p10+p20+p50+p100+p200 < pence):
                                    for e in range(n+1):
                                        p50=e
                                        if(p1+p2+p5+p10+p20+p50+p100+p200 < pence):
                                            for f in range(n+1):
                                                p100 = f
                                                if(p1+p2+p5+p10+p20+p50+p100+p200 < pence):
                                                    for f in range(n+1):
                                                        p200 = g
                                                        if(p1+p2+p5+p10+p20+p50+p100+p200 == pence):
                                                        solution+=1
                                                        p200 = 0
                                                        break
                                                    
                                        else:
    return soln                                      