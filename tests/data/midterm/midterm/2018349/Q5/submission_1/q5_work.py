# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    ans = 1
    for k in range(i+1):
        ans += -(ans**2-abs(num))/(2*ans)
    return round(ans,3)

def nroot_complex(n,i,num):
    if num < 0 and n%2 == 0:
        return nroot(n,i,abs(num))*1j
    elif num < 0 and n%2 == 1:
        return nroot
