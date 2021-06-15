# MID-TERM EXAM: QUESTION 7

def decompose(n):
    no_2pound = n // 200
    no_1pound = n//100
    no_50p = n//50
    no_20p = n//20
    no_10p = n//10
    no_5p = n//5
    no_2p = n//2
    no_1p = n
    if no_2pound >0:
        return n%200
    if no_1pound>0:
        return n%100

def decompose(n):
    pound2=[]
    for a in range(0,n,200):
        pound2.append[a]
    pass
    print(pound2) 