# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    val = [200,100,50,20,10,5,2,1]
    c = 0
    for i in range(pence//200+1):
        p = pence
        p2 = p-200*p//200*i
        for j in range(p2//100+1):
            p3 = p2-100*p2//100*j
            for k in range(p3//50+1):
                p4 = p3-50*p3//50*k
                for l in range(p4//20+1):
                    p5 = p4-20*p4//20*l
                    for m in range(p5//10+1):
                        p6 = p5-10*p5//10*m
                        for n in range(p6//5+1):
                            p7 = p6-5*p6//5*n
                            for o in range(p7//2+1):
                                p8 = p7-2*p7//2*o
                                c += 1
    return c