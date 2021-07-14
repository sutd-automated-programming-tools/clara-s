def nroot(n,t,num):
    x = 1
    fx = x**n - num
    fxp = n*x
    for i in range(t):
        x = x - fx/fxp
    return x