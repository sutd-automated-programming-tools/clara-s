def decompose(pence):
    p1 = range(n,-1,-2)
    p2 = range(n,-1, -2)
    p5 = range(n,-1,-5)
    p10 = range(n, -1, -10)
    p20 = range(n,-1,-20)
    p50 = range(n, -1,-50)
    p100 = range(n,-1,-100)
    p200 = range(n,-1,-200)
    count = 0
    for i in p1:
        if p1[i] == n:
            count += 1
        if n>2:
            for j in p2:
                if p1[i] + p2[j] == n:
                    count += 1
                if n>5:
                    for k in p5:
                        if p1[i] + p2[j] + p5[k] == n:
                            count += 1
                        if n>10:
                            for g in p10:
                                if p1[i] + p2[j] + p5[k] + p10[g] == n:
                                    count += 1
                                if n>20:
                                    for h in p20:
                                        if p1[i] + p2[j] + p5[k] + p10[g] + p20[h] == n:
                                            count += 1
                                        if n>50:
                                            for u in p50:
                                                if p1[i] + p2[j] + p5[k] + p10[g] + p20[h] + p50[u]:                                                   m] == n:
                                                    count += 1
                                                if n>100:
                                                    for l in p100:
                                                if p1[i] + p2[j] + p5[k] + p10[g] + p20[h] + p50[u] + p100[l] == n:
                                                    count += 1
                                                        if n>200:
                                                            for m in p200:
                                                                if p1[i]+p2[j]+p5[k]+p10[g]+p20[h]+p50[u]+p100[l]+p200[m] == n:
                                                                    count +=1
    return count