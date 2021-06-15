# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    count=t
    n=float(n)
    num=float(num)
    x_power=num**(n)
    f=x_power-num
    f1=2*num
    while count!=0:
        count=count-1
        ans=ans-f/f1
        return ans


def nroot_complex(n,t,num):
    pass