# MID-TERM EXAM: QUESTION 7

def decompose(n):
    count=0
    for i1 in range(0,n+1):
        for i2 in range(0,n+1):
            for i3 in range(0,n+1):
                for i4 in range(0,n+1):
                    for i5 in range(0,n+1):
                        for i6 in range(0,n+1):
                            for i7 in range(0,n+1):
                                for i8 in range(0,n+1):
                                    if i1+i2*2+i3*5+i4*10+i5*20+i6*50+i7*100+i8*200==n:
                                        count+=1
    return count