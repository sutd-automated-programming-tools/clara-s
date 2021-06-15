# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x**n = num
    x= num**(1/n) + ((x**n-num)/(n*x))
    return x
    pass

def nroot_complex(n,t,num):
    pass

def nroot(n,num):
    answer= num**(1/n)
    #num= x - ((x**n -num)/(n*x))
    return answer

print(nroot(2,2))