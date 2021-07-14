# MID-TERM EXAM: QUESTION 3

import math
def area_square(s):
    return (s*s)

def vol_frustum(top_area,bottom_area,height):
    a1 = top_area
    a2 = bottom_area
    vol = (height/3)*(a1 + a2 + math.sqrt(a1*a2))
    return vol

def get_volume(s1,s2,height):
    a1 = area_square(s1)
    a2 = area_square(s2)
    res = vol_frustum(a1,a2,height)
    res = round(res,3)
    return res
