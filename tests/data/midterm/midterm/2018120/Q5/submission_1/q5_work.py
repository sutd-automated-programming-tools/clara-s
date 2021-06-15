# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):

    x = (num)**(1/n)
    f_x = x**n - num 
    dev_f_x = n*x**(n-1)
        
    return x-f_x/dev_f_x


def nroot_complex(n,i,num):
    if n %2 ==0:
        result = str(nroot(n,i,num))
    else:
        result = -(nroot(n,i,num))
    return round(result,3)