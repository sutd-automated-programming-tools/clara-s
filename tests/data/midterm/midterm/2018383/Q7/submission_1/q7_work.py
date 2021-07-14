# MID-TERM EXAM: QUESTION 7

def decompose(amt):
    denom = [2,5,10,20,50,100,200]
    ans = [1] * (amt+1)
    for i in denom:
        for j in range(i,amt+1):
            ans[j] += ans[j-i]
    return ans[-1]