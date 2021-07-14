# MID-TERM EXAM: QUESTION 7


def decompose(pence):
    lst = [0.01,0.02,0.05,0.1,0.2,0.5,1,2]
    count = 0
    sum1 = 0
    for i in range(len(lst)):
        count += 1
        sum1 +=lst[i]
        if pence == lst[i] + sum1:
            ans =  count
        else:
            continue
    return ans