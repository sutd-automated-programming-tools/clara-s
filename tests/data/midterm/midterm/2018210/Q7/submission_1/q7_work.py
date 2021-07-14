
def decompose(n):
    x1 = 1
    x2 = 2 
    x3 = 2 # 2 ways to decompose 5p
    x4 = 6 # 6 ways to decompose 10p, splitting into 1s, 2s or 5s (but this includes 2 more)
    x5 = 
    x6 = 50
    x7 = 100
    x8 = 200
    solution = 0
    if n == 1:
        return 1
    elif n < 2:
        return 1
    elif n%x2 == 0: