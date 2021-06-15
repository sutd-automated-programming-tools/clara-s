# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    i = t
    newx = 1
    while i < n:
        num = x**i #number is equal to the power of i
        funt = x**i - num #funt as f(x)
        funtin = i*x #f'(x)
        newx = x - funt/funtin #iteration given
        i +=1 #add till you find the nth iteration
    return newx #return the value of the nth iteration to find nroot

def nroot_complex(n,t,num):
    pass