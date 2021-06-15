# MID-TERM EXAM: QUESTION 3

import math
def area_square(s):
    return s**2

def vol_frustum(t,b,h):
    oup = h*(t+b+math.sqrt(t*b))/3
    return round(oup,3)

def get_volume(s1,s2,h):
    t = area_square(s1)
    b = area_square(s2)
    oup = vol_frustum(t,b,h)
    return oup
