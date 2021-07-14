# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    denom = [1,2,5,10,20,50,100,200]
    amt = 0
    ans = [1] * (pence+1)
    while amt < pence:
        for i in denom:
            for j in range(i,pence+1):
                ans[j] += ans[j-i]
                amt += i *j
    return ans[-1]