# MID-TERM EXAM: QUESTION 7
def decompose(n):
    count = 0
    for a in range(n,-1,-1):
        for b in range(n,-1,-2):
            for c in range(n,-1,-5):
                for d in range(n,-1,-10):
                    for e in range(n,-1,-20):
                        for f in range(n,-1,-50):
                            for g in range(n,-1,-100):
                                for h in range(n,-1,-200):
                                    if n%a== 0 or n%b==0 or n%c == 0 or n%d == 0 or n%e == 0or n%f == 0or n%g == 0or n%h == 0
                                        count += 1
    return count