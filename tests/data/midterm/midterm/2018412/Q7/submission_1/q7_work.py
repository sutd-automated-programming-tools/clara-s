# MID-TERM EXAM: QUESTION 7

def decompose(pence, x = 8):
    if x == 1:
        return 1
    if pence == 0:
        return 1
    else:
        num = 0
        for i in range(x):
            for j in range(pence):
                num += num_of_sol(j, i)
        return num