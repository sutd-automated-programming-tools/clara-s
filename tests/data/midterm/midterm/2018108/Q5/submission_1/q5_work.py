# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    for times in range(i):
        n = n - (n**2 - num)/(2*n)
    return round(n,3)

def nroot_complex(n,i,num):
    if num > 0:
        result = nroot(n,i,num)
        return result
    elif num < 0 and n%2==0:
        result = str(int((nroot(n,i,-num))))
        return (result+"j")
    elif num < 0 and n%2 != 0:
        result = int(nroot(n,i,-num))
        return float(-result)
    

