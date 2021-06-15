def decompose(pence):
    twopoundsmax=pence//200
    onepoundmax=pence//100
    fiftymax=pence//50
    twentymax=pence//20
    tenmax=pence//10
    fivemax=pence//5
    twomax=pence//2
    onemax=pence
    count=0
    for i in range(twopoundsmax):
        for j in range(onepoundmax):
            for k in range(fiftymax):
                for l in range(twentymax):
                    for m in range(tenmax):
                        for n in range(fivemax):
                            for o in range(twomax):
                                for p in range(onemax):
                                    total=i*200+j*100+k*50+l*20+m*10+n*5+o*2+p
                                    if total==pence:
                                        count+=1
    return count
        