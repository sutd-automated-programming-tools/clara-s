# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    if pence == 1:
        return 1
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    c = [i for i in coins if i <= pence][::-1]
    num = 0
    for i in c:
        for time in range(1, pence // i):
            num += decompose(pence - i*time)
    return num