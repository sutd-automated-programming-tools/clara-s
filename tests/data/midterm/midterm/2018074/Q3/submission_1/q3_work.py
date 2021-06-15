# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s**2

def vol_frustum(a1,a2,height):
    vol = (height/3)*(a1+a2+math.sqrt(a1*a2))
    return vol

def get_volume(top,bottom,height):
    a1 = area_square(top)
    a2 = area_square(bottom)
    vol = vol_frustum(a1,a2,height)
    return round(vol,3)
