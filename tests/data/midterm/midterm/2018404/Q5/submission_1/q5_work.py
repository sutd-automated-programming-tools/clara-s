# MID-TERM EXAM: QUESTION 5

import math
import cmath


def nroot(n, i, num):
    return nroot(n, i, num)

def nroot_complex(n, i, num):
    
    
    if num >= 0:
        return nroot(n, i, num)
    elif num < 0 and (n % 2 == 0):
        return nroot_complex(n, i, num)
    else:
        num < 0 and (n % 2 - 1 == 0)
        return nroot_complex(n, i, num)
