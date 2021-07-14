# MID-TERM EXAM: QUESTION 5
def nroot(n, i, num):#root of non-neg num
    x = 1
    
    if n == 2:
        count = 0
        for count in range(i):
            f_x = x ** 2 - num
            df_x = 2 ** x
            x = x - (f_x / df_x)
            count += 1
    return round(x,3)

    if n == 3:
        f_x = x ** 3 - num
        df_x = 3 * (x ** 2)
        for count in range(i+1):
            x = x - (f_x / df_x)
            count += 1
    return round(x,3)

    pass

def nroot_complex(n,t,num):
    def nroot_complex(n, i, num):#root of neg num. call nroot to do nr approx
        if num > 0:
            ans_nonneg = nroot(n, i, num)
            return ans_nonneg
        elif num < 0:
            if num % 2 == 0:
                ans_neg_even = 1j * nroot(n, i,num)
                return ans_neg_even
                pass
            else:
                ans_neg_odd = -1*nroot(n, i,num)
                return ans_neg_odd
                pass
    pass