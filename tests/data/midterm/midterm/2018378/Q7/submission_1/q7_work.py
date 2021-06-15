# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    sum=0
    combi1=[i for i in range(0,pence+1,1)]
    combi2=[i for i in range(0,pence+1,2)]
    combi5=[i for i in range(0,pence+1,5)]
    combi10=[i for i in range(0,pence+1,10)]
    combi20=[i for i in range(0,pence+1,20)]
    combi50=[i for i in range(0,pence+1,50)]
    combi100=[i for i in range(0,pence+1,100)]
    combi200=[i for i in range(0,pence+1,200)]
    for i in combi200:
        for j in combi100:
             for k in combi50:
                 for l in combi20:
                     for n in combi10:
                         for o in combi5:
                             for p in combi2:
                                 for q in combi1:
                                     if (i+j+k+l+n+o+p+q)==pence:
                                         sum+=1
    return sum
