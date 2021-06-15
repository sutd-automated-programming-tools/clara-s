# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x2 = num
    counter = 0
    if counter<t:
        fx = x2-num
        dfx = 2*(x2**.5)
        x2 = num**0.5 - fx/dfx
        counter += 1
    return round(x2,3)

def nroot_complex(n,t,num):
    pass