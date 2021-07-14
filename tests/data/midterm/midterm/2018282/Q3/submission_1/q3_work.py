# MID-TERM EXAM: QUESTION 3
from math import sqrt
def area_sqaure(s1):
    A1 = s1 ** 2 
    A1_out = round(A1, 3)
    return A1_out
def area_square(s2):
    A2 = s2 ** 2
    A2_out = round(A2,3)
    return A2_out


def vol_frustum(A1, A2, H):
    V = H / 3 (A1_out + A2_out + sqrt(A1_out * A2_out))
    V_out = round(V, 3)
    return V_out

def get_volume(s1, s2, H):
    finalv = H / 3 (s1 ** 2 + s2 **2 + sqrt(s1 ** 2 * s2 ** 2))
    finalv_out = round(finalv, 3)
    return finalv_out
    
