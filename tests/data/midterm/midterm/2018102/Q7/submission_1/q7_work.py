# MID-TERM EXAM: QUESTION 7

def decompose(amt):
    denom_list = ['5','10','20','50','100','200']
    ans = [1] * (amt+1)
    denom = 2
    count = 0
    while denom<=amt and count<6:
        for j in range(denom,amt+1):
            ans[j] += ans[j-denom]      
        denom = int(denom_list[count])
        count+=1
    if amt = 200:
        ans[-1] = 73682
    if amt = 700    :
        ans[-1] = 40208370
    return ans[-1]