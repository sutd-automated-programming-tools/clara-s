# MID-TERM EXAM: QUESTION 7
import numpy
def decompose(pence):
    count=1
    n=numpy.array([1,2,5,10,20,50,100,200])
    for i in range(pence//1):
        for o in range(pence//2):
            for p in range(pence//5):
                for q in range(pence//10):
                    for r in range(pence//20):
                        for s in range(pence//50):
                            for k in range(pence//100):
                                for t in range(pence//200):
                                    x=numpy.array([i],[o],[p],[q],[r],[s],[k],[t])
                                    if n.dot(x)==pence:
                                        count+=1
    return count