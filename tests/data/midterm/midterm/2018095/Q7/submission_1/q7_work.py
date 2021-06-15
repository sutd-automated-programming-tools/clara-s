# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    n=pence
    ans = 0
    lol = n*100
    for i in range(lol+1):
        for j in range(lol+1):
            for k in range(lol+1):
                for l in range(lol+1):                    
                    for m in range(lol+1):
                        for n in range(lol+1):
                            for o in range(lol+1):
                                for p in range(lol+1):
                                    if i + j*2 + 5*k + 10*l + 20*m+50*n+100*o+200*p == lol:
                                        
                                         ans += 1
    return ans                                        
    pass