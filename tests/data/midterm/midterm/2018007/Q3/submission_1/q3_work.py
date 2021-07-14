# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return round(s*s,3)

def vol_frustum(t,b,h):
    return round((t+b+math.sqrt(t*b))*h/3,3)

def get_volume(s1,s2,h):
    A1 = area_square(s1)
    A2 = area_square(s2)
    area = vol_frustum(A1,A2,h)
    
    return round(area,3)
