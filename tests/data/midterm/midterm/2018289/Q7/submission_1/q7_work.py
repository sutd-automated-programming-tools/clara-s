# MID-TERM EXAM: QUESTION 7

from scipy.special import comb

def decompose(n):
    x = 8
    return int(comb(n+x-1 , x-1, exact=False, repetition=False))
