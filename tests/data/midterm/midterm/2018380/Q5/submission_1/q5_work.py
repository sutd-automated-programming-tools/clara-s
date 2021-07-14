# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num): # for non negative roots 
    x = (num)**(1/n)
    y = x**n - num 
    dy = n*x**(n-1) 
    x_t = 0
    y_t = 0 
    dy_t = 0 
    for i in range (1,t+1):
        y_t = y_t - (x**n - num )
        dy_t = dy_t - (n*x**(n-1) )
        x_t= x_t- (y_t/dy_t)
    return x_t 
def nroot_complex(n,t,num):
    pass