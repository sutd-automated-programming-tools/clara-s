# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    ans = 0
    for i in range(pence,-1,8):
        for j in range(pence,-1,8):
            for k in range(pence,-1,8):
                for l in range(pence,-1,8):
                    for m in range(pence,-1,8):
                        for n in range(pence,-1,8):
                            for o in range(pence,-1,8):
                                for p in range(pence,-1,8):
                                    if i + j + k + l + m + n + o + p == n:
                                        ans += 1
    return ans