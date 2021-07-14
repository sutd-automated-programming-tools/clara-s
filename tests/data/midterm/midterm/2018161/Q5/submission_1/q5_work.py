# MID-TERM EXAM: QUESTION 5

def nroot(n, t, num):
    
    counter = 1
    x = 1
    root = 0
    
    while counter <= t:       
        func = x**n - num
        deri = n*(x**(n-1))
        root = root - (func/deri)
        counter += 1
    return round(root,3)