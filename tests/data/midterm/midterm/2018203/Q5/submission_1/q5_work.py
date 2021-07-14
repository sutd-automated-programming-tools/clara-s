# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num): # What this function needs to do is return an approximation of the nth root of num, after t iterations
    times = 0 # We first set the number of iterations to 0 as a counter
    x = 1 # We start with 1 as a starting value for our solution x
    while times < t: # This ensures that the counter only runs t times corresponding to the t iterations
        x -= ((x**n)-num)/(n*(x**(n-1))) # We assign a new value to x after each iteration, according to the given equation in the Newton-Raphson method
        times += 1 # We add 1 to the counter, signalling that one iteration has been done
    return round(x, 3) # We return the approximation after t iterations, rounded to 3 decimal places
                           
def nroot_complex(n,t,num):
    if num > 0:
        return nroot(n, t, num)
    elif num < 0 and n%2==0:
        return (nroot(n, t, num*-1))*((-1)**0.5)
    elif num < 0 and n%2!=0:
        return (nroot(n, t, num*-1))*-1