# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    final = 1
    itr = 0
    while itr < i:
        final = final - (final**n - num)/(n*final)
        itr += 1
    return round(final,3)
def nroot_complex(n,i,num):
    return nroot(n,i,num)