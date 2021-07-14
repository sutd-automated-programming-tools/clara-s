# MID-TERM EXAM: QUESTION 5
def nroot(n,i,num):
    if num < 0:
        root = nroot_complex()
    else:
        x = 1
        counter = 0
        while counter < i:
            fn = (x**n) - num
            fdn = n*x**(n-1)
            x -= (fn/fdn)
            counter += 1
        

def nroot_complex(n,i,num):
    if num < 0:
        
    if n%2 == 0:
        ans = root*-1
    if n%2 != 0:
        ans = root*1j
    final = nroot()