# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    ppe1 = 1
    ppe2 = 1 + (ppe1**2)
    ppe5 = (ppe2**2) + 1
    ppe10 = (ppe5**2) + 1
    ppe20 = (ppe10**2) + 1
    ppe50 = ((ppe20 ** 2)*(ppe10)) + 1
    ppo1 = (ppe50 ** 2) + 1
    ppo2 = (ppo1 ** 2) + 1
    po2 = 0
    po1 = 0
    pe50 = 0
    pe20 = 0
    pe10 = 0
    pe5 = 0
    pe2 = 0
    pe1 = 0
    while pence >= 200:
        po2 += 1
        pence -= 200
    while pence >= 100:
        po1 += 1
        pence -= 100
    while pence >= 50:
        pe50 += 1
        pence -= 50
    while pence >= 20:
        pe20 += 1
        pence -= 20
    while pence >= 10:
        pe10 += 1
        pence -= 10
    while pence >= 5:
        pe5 += 1
        pence -= 5
    while pence >= 2:
        pe2 += 1
        pence -= 2
    while pence >= 1:
        pe1 += 1
        pence -= 1
    if pence == 0:
        goodjob = True
    else:
        goodjob = False
    possibility = (po1 * ppo1) + (po2 * ppo2) + (pe50 * ppe50) + (pe20 * ppe20) + (pe10 * ppe10) + (pe5 * ppe5) + (pe2 * ppe2) + (pe1 * ppe1)
    return possibility