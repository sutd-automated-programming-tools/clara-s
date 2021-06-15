# MID-TERM EXAM: QUESTION 5
def nroot(n, i, num):
    x =1
    k=1

    while k < i:
        fx = (x)**n - num
        fx_prime = (n)*(x)**(n-1)
        x = x - (fx/fx_prime)
        k+=1
    return round(x,3)

def nroot_complex(n, i ,num):
    if num > 0:
        ans = nroot(n, i, num)
        return ans
    
    elif num < 0:
        if n%2 == 0:
            ans = complex.imag(sqrt(nroot(n,i,num)))
            return ans
        
        else:
            ans = -1 * sqrt((nroot(n,i,num))
            return ans