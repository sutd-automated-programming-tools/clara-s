# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    def num_of_sol(n):
    pound2 = 2*pound1 = 4*p50 = 10*p20 = 20*p10= 40*p5 = 100 *p2 = 200 *p1 
    p1 =0
    p2 =0
    p5 =0
    p10 =0
    p20 =0
    p50 =0
    pount1 =0
    pound2 =0
    solution =0
    for p1i in range(pence+1):
        p1 = p1i
        if(p1+p2+p5+p10+p20+p50+pound1+pound2<pence):
            for p2i in range(n+1):
                p2 = p2i
                if(p1+p2+p5+p10+p20+p50+pound1+pound2<pence):
                    for p5i in range(n+1):
                        p5 = p5i
                        if(p1+p2+p5+p10+p20+p50+pound1+pound2<pence):
                            for p10i in range(n+1):
                                p10 = p10i
                                if(p1+p2+p5+p10+p20+p50+pound1+pound2<pence):
                                    for p20i in range(n+1):
                                        p20 = p20i
                                        if(p1+p2+p5+p10+p20+p50+pound1+pound2<pence):
                                            for p50i in range(n+1):
                                                if (p1+p2+p5+p10+p20+p50+pound1+pound2<pence):
                                                    for pound1i in range(n+1):
                                                        if (p1+p2+p5+p10+p20+p50+pound1+pound2<pence):
                                                            for pound2=pound2:
                                                                if(p1+p2+p5+p10+p20+p50+pound1+pound2==pence):
                                                                    solution += 1
                                                                    print(7)
                                                                    print((p1,p2,p5,p10,p20,p50,pound1,pound2))
                                                                else: #exit this loop as any increments to x4 will no longer result in solutions
                                                        else:
                                                 else:#exit the loop until you are done.
                                                    