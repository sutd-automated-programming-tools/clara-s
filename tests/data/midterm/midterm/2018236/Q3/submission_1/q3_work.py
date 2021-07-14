# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s**2

def vol_frustum(A1, A2, h):
    
    return h*(A1 + A2 + math.sqrt(A1*A2))/3 

def get_volume(s1, s2, h):
    
    A1 = area_square(s1)
    A2 = area_square(s2)
    return round(vol_frustum(A1,A2,h) , 3)
