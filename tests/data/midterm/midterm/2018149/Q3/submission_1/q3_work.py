# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return float(s**2)

def vol_frustum(topa, bota, h):
    
    #print(bota, topa)
    volume = (h/3) * ( topa + bota + math.sqrt(topa * bota) )
    return volume

def get_volume(s1,s2,h):
    a1 = area_square(s1)
    a2 = area_square(s2)
    volume = vol_frustum(a1, a2, h)
    return volume
