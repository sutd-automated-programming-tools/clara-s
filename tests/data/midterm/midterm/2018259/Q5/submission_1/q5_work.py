# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    xsq=num
    func= xsq - num
    derivat=2*xsq
    for digit in range(n):
        x = xsq - (func/derivat)
        return x
