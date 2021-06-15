# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    ans = 0
    for i in range(pence+1):
        for j in range(int(pence/2) + 1):
            for k in range(int(pence/5) + 1):
                for m in range(int(pence/10) + 1):
                    for n in range(int(pence/20) + 1):
                        for b in range(int(pence/50) + 1):
                            for v in range(int(pence/100) + 1):
                                for c in range(int(pence/200) + 1):
                                    if i + 2*j + 5*k + 10*m +20*n + 50*b + 100*v + 200*c == pence:
                                        ans = ans + 1
    return ans
