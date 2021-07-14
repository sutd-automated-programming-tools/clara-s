def decompose(pence):
    p1 = 1
    p2 = 2
    p5 = 5
    p10 = 10
    p20 = 10
    p50 = 50
    l1 = 100
    l2 = 200
    
    count = 0
    temp = pence
    
    for i in range(1,int(pence+1/p1)):
        temp = pence
        temp -= p1*i
        if temp == 0:
            count += 1
        for j in range(1,int(pence+1/p2)):
            temp -= p2*j
            if temp == 0:
                count += 1
            for k in range(1,int(pence+1/p5)):
                temp -= p5*k
                if temp == 0:
                    count += 1
                for l in range(1,int(pence+1/p10)):
                    temp -= p10*l
                    if temp == 0:
                        count += 1
                    for m in range(1,int(pence+1/p20)):
                        temp -= p20*m
                        if temp == 0:
                            count += 1
                        for o in range(1,int(pence+1/p50)):
                            temp -= p50*o
                            if temp == 0:
                                count += 1
                            for p in range(1,int(pence+1/l1)):
                                temp -= l1*p
                                if temp == 0:
                                    count += 1
                                for q in range(1,int(pence+1/l2)):
                                    temp -= l2*q
                                    if temp == 0:
                                        count += 1
    return count