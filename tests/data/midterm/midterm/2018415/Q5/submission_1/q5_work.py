# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    if (num > 0):
        num = (num)**(1/n)
        return  round(num,3)
    
def nroot_complex(n,t,num):
    if (num < 0):
        num = (-1**(n-1)*num)**(1/n)
        return  num

   