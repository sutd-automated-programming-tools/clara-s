# MID-TERM EXAM: QUESTION 7

def decompose(n, x = 8):
    if n == 1:
        return 1 
    else:
        solutions = 0    
        for i in range(x):
            for j in range(n):
                solutions += decompose(j, i)
        return solutions