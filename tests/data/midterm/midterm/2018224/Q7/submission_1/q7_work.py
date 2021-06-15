# MID-TERM EXAM: QUESTION 7

def decompose(n):
    ans=0
    for a in range(n+1):
        for b in range(n+1):
            for c in range(n+1):
                for d in range(n+1):
                    for e in range(n+1):
                        for f in range(n+1):
                            for g in range(n+1):
                                if a*1+b*2+c*3+d*4+e*5+f*6+g*7==n:
                                    ans=ans+1
    return ans