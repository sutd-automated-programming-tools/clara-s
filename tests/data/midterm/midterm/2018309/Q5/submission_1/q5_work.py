# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    ans = 1
    index = 0
    while index < i:
        ans = ans - (ans**n-num)/(n*ans)
        index += 1
    return round(ans,3)

def nroot_complex(n,i,num):
    if num > 0:
        ans = nroot(n,i,num)
    else:
        if n % 2 == 0:
            ans = 1
            index = 0
            while index < i:
                ans = ans - (ans**n-num)/(n*ans)
                index += 1
            ans = complex(str(round(ans))+'j')
            return ans
        elif n % 2 != 0:
            ans = 1
            index = 0
            while index < i:
                ans = ans - (ans**n-num)/(n*ans)
                index += 1
            #ans = ans.real
            return round(ans,3)