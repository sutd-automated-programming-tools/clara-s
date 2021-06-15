# MID-TERM EXAM: QUESTION 5

def nroot(n, i, num):
    x = 1
    for v in range(1,i+1):
        f = x**n - num
        f_prime = n*(x**(n-1))
        x = x-(f/f_prime)
    return round(x,3)

def nroot_complex(n, i, num):
    if num >= 0:
        final_ans = nroot(n,i,num)
        return final_ans
    if num < 0:
        if n %2 == 0:
            num = num*-1
            final_ans1 = nroot(n,i,num)
            final_ans = final_ans1*1j
            return final_ans
        if n%2 != 0:
            num = num*-1
            final_ans1 = nroot(n,i,num)
            final_ans = -1*final_ans1
            return final_ans