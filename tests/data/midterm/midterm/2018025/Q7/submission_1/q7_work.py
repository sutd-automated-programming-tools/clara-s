# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    count = 0
    for i in range (1,1000):
        p1 = 1*i
        for j in range (1,1000):
             p2 = 2*j
             for k in range (1,1000):
                 p5 = 5*k
                 for l in range (1,1000):
                     p10 = 10*l
                     for m in range(1,1000):
                         p20 = 10*m
                         for n in range(1,1000):
                             p50 = 50*n
                             for o in range(1,1000):
                                 p100 = 100*o
                                 for p in range(1,1000):
                                     p200 = 200*p
                                       
                                     if p1 + p2 + p5 + p10 + p20+p50+p100 +p200 = pence:
                                        count = count+1
    return count