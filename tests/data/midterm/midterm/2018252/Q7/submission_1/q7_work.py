# MID-TERM EXAM: QUESTION 7

def decompose(pence):
def decompose(n):
    a=n//1
    b=n//2
    c=n//5
    d=n//10
    e=n//20
    f=n//50
    g=n//100
    h=n//200
    count=0
    for a1 in range(a+1):
        for b1 in range(b+1):
            for c1 in range(c+1):
                for d1 in range(d+1):
                    for e1 in range(e+1):
                        for f1 in range(f+1):
                            for g1 in range(g+1):
                                for h1 in range(h+1):
                                    if a1*1+b1*2+c1*5+d1*10+e1*20+f1*50+g1*100+h1*200 == n:
                                        count +=1
    return count